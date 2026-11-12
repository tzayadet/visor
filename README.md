# NEXUS::VIEWER

Editor y visor en navegador para trabajar con **HTML, Markdown y JavaScript** desde una única interfaz de estilo terminal.

**Demo:** https://tzayadet.github.io/visor/  
**Código:** https://github.com/tzayadet/visor

## Funcionalidades

- Edición de HTML, Markdown y JavaScript mediante modos independientes.
- Previsualización y renderizado automático del contenido.
- Ejecución manual de JavaScript y panel de salida.
- Consola visual para revisar resultados y errores.
- Carga de archivos locales y exportación del contenido.
- Contador de líneas y caracteres, reloj y fondo animado Matrix.
- Interfaz adaptable con controles de edición y limpieza.

## Uso

Abre la [demo](https://tzayadet.github.io/visor/) o descarga el repositorio y abre `index.html` en un navegador moderno.

No necesita instalación ni un servidor propio para su uso básico. La librería Marked se carga desde CDN para interpretar Markdown, por lo que esa función requiere conexión a Internet.

## Seguridad

El visor permite ejecutar JavaScript. Utiliza únicamente código de confianza y revisa el contenido antes de ejecutarlo. No introduzcas credenciales, tokens ni información sensible en documentos o scripts de terceros.

## Tecnologías

- HTML5 y CSS3
- JavaScript
- Marked.js
- File API y Blob API del navegador

## Despliegue

La página se publica mediante GitHub Pages. Es una aplicación de navegador estática: no incluye backend ni almacenamiento remoto propio.

## Licencia

Consulta el estado de licencia del repositorio.
