# Nexus Viewer

A browser-based workspace for editing and previewing HTML, Markdown and JavaScript in a single interface. It combines a code editor, live rendering panel and console-style output.

<p align="center">
  <a href="https://tzayadet.github.io/visor/"><img src="https://img.shields.io/badge/LIVE_DEMO-OPEN-00a86b?style=flat-square" alt="Live demo"></a>
  <a href="https://github.com/tzayadet/visor"><img src="https://img.shields.io/badge/SOURCE-GITHUB-161b22?style=flat-square&logo=github" alt="Source code"></a>
</p>

## Features

- Dedicated editing modes for HTML, Markdown and JavaScript.
- Live preview and manual JavaScript execution.
- Console-style output for results and errors.
- Local file loading and content export.
- Line and character counters.
- Responsive interface with a terminal-inspired visual style.

## Run locally

No installation or backend is required for basic use. Clone the repository and open `index.html` in a modern browser.

The Markdown renderer is loaded from a CDN, so Markdown preview requires an internet connection.

## Project structure

The application is a static browser project built with HTML, CSS and JavaScript. It uses the browser File API and Blob API for local file handling and export.

## Live demo

[Open Nexus Viewer](https://tzayadet.github.io/visor/)

The published version runs entirely in the browser. It does not include a remote backend or server-side storage.

## Security notes

The application can execute JavaScript entered into its editor. Only run code you trust. Do not paste credentials, access tokens or sensitive information into untrusted scripts or documents.

## License

See the repository for its current licensing information.
