from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


class ViewerValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = []
        self.references = []
        self.inline_scripts = []
        self.current_script = None
        self.preview_sandboxes = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])

        reference_key = "src" if tag in {"script", "img", "iframe", "source"} else "href"
        reference = attrs.get(reference_key)
        if reference:
            self.references.append(reference)

        if tag == "iframe" and attrs.get("id") == "previewFrame":
            self.preview_sandboxes.append(set((attrs.get("sandbox") or "").split()))

        if tag == "script":
            self.current_script = [] if "src" not in attrs else None

    def handle_data(self, data):
        if self.current_script is not None:
            self.current_script.append(data)

    def handle_endtag(self, tag):
        if tag == "script" and self.current_script is not None:
            self.inline_scripts.append("".join(self.current_script))
            self.current_script = None


def main():
    parser = ViewerValidator()
    parser.feed((ROOT / "index.html").read_text(encoding="utf-8"))

    duplicates = sorted({value for value in parser.ids if parser.ids.count(value) > 1})
    if duplicates:
        raise SystemExit(f"Duplicate HTML IDs: {duplicates}")

    if not parser.preview_sandboxes:
        raise SystemExit("Preview iframe sandbox attribute was not found.")
    for permissions in parser.preview_sandboxes:
        if "allow-scripts" not in permissions:
            raise SystemExit("Preview iframe must allow scripts for the editor.")
        if "allow-same-origin" in permissions:
            raise SystemExit("Preview iframe must not combine scripts with same-origin access.")
        if "allow-popups" in permissions:
            raise SystemExit("Preview iframe must not allow popups by default.")

    missing = []
    for reference in parser.references:
        parsed = urlsplit(reference)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        target = (ROOT / unquote(parsed.path)).resolve()
        if not target.exists():
            missing.append(reference)
    if missing:
        raise SystemExit("Missing local references: " + ", ".join(missing))

    node = shutil.which("node")
    if parser.inline_scripts and not node:
        raise SystemExit("Node.js is required to syntax-check inline JavaScript.")

    with tempfile.TemporaryDirectory() as temp_dir:
        for index, source in enumerate(parser.inline_scripts, start=1):
            if not source.strip():
                continue
            script_path = Path(temp_dir) / f"inline-{index}.js"
            script_path.write_text(source, encoding="utf-8")
            subprocess.run([node, "--check", str(script_path)], check=True)

    print(
        f"Validated HTML IDs, {len(parser.inline_scripts)} inline script(s), "
        "local references and preview iframe sandbox."
    )


if __name__ == "__main__":
    main()
