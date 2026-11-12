<p align="center">
  <img src="https://img.shields.io/badge/WEB_WORKSPACE-NEXUS_VIEWER-101010?style=for-the-badge&labelColor=050805&color=00FF41" alt="Nexus Viewer"/>
  <img src="https://img.shields.io/badge/HTML_CSS_JS-BROWSER_IDE-101010?style=for-the-badge&logo=javascript&logoColor=00FF41" alt="JavaScript"/>
</p>

# Nexus Viewer

Browser-based workspace for editing and previewing HTML, Markdown and JavaScript in one interface. It combines an editor, live rendering panel and console-style output.

<p align="center">
  <a href="https://tzayadet.github.io/visor/"><strong>LIVE DEMO ↗</strong></a> ·
  <a href="https://github.com/tzayadet/visor"><strong>SOURCE CODE</strong></a>
</p>

[![Quality checks](https://github.com/tzayadet/visor/actions/workflows/quality.yml/badge.svg)](https://github.com/tzayadet/visor/actions/workflows/quality.yml)

## Features

- Dedicated editing modes for HTML, Markdown and JavaScript.
- Live preview and manual JavaScript execution.
- Console-style output for results and errors.
- Local file loading and content export.
- Line and character counters.
- Responsive interface with a terminal-inspired visual style.

## Use it

Open the [live demo](https://tzayadet.github.io/visor/) or clone the repository and open `index.html` in a modern browser.

No installation or backend is required for basic use. The Markdown renderer is loaded from a CDN, so Markdown preview requires an internet connection.

## Technology

- HTML5 and CSS3
- JavaScript
- Marked.js
- File API and Blob API

## Security notes

The application can execute JavaScript entered into its editor. Preview content runs inside a sandboxed iframe without same-origin or popup permissions. Only run code you trust. Do not paste credentials, access tokens or sensitive information into untrusted scripts or documents.

## Scope

The published version runs entirely in the browser. It does not include a remote backend or server-side storage.

## Validation

The quality workflow checks inline JavaScript syntax, local asset references, duplicate HTML IDs and preview iframe sandbox permissions:

```bash
python scripts/validate_site.py
```

Requires Python 3.11+ and Node.js 22+.

## Deployment

Static website published through GitHub Pages.

## License

See the repository for its current licensing information.
