# Licenciatura en Paleontología — FCEN UBA

Sitio web de la Licenciatura en Paleontología de la Facultad de Ciencias Exactas y Naturales (UBA).
Es un sitio **estático** (HTML, CSS y JavaScript, sin frameworks ni compilación), con la misma lógica que el sitio de la Licenciatura en Biotecnología: se puede alojar en cualquier servidor web copiando la carpeta tal cual.

## Páginas

| Archivo | Contenido |
|---|---|
| `index.html` | Portada |
| `ingresantes.html` | Qué es la carrera, perfil, incumbencias, cómo ingresar |
| `carrera.html` | Plan de estudios: recorrido, mapa de correlatividades interactivo, materias, optativas y electivas |
| `estudiantes.html` | Plan de materias y tutor, programas, equivalencias |
| `tesis.html` | Tesis de Licenciatura: pasos, reglamento, formularios, Premio Camacho |
| `comision.html` | Comisión de Carrera y actas de reuniones |
| `documentos.html` | Resoluciones, reglamentos, modelos de carta y enlaces |
| `doctorado.html` | Doctorado de la UBA, área Paleontología |

## Cómo editar

- **Textos**: hay dos formas.
  - *Cambios chicos*: directamente en el archivo `.html` de la página.
  - *Cambios en el menú, el encabezado o el pie, o en varias páginas a la vez*: editar `_fuente/paginas.py` (contenido) o `_fuente/build.py` (menú, encabezado y pie) y regenerar todas las páginas con
    ```bash
    python3 _fuente/build.py
    ```
    Ojo: al regenerar se pisan los `.html`, así que un cambio hecho a mano en un `.html` hay que pasarlo también a `_fuente/paginas.py`.
- **Plan de estudios** (materias, horas, correlatividades, equivalencias): **solo** en el bloque de datos al principio de `js/plan.js`. Con esos datos se dibujan el diagrama y la tabla de `carrera.html`.
- **Colores y tipografías**: variables al principio de `css/style.css` (`:root`).
- **Ilustraciones de fósiles**: `imgs/fosiles.svg`. Son provisorias y ocupan el lugar de las fotos (los recuadros dicen «Foto: … (provisoria)»).
- **Documentos descargables**: en la carpeta `archivos/` (ver más abajo).

## Archivos a migrar desde el sitio viejo

Los PDF (programas, actas, reglamentos, etc.) están todavía en el sitio viejo `paleo.gl.fcen.uba.ar`.
`MIGRACION_ARCHIVOS.md` tiene la tabla completa con el link de cada uno y el nombre con el que hay que guardarlo, y `descargar_archivos.sh` los baja automáticamente con esos nombres. Hasta que se suban a `archivos/`, esos enlaces del sitio dan error 404.

## Ver el sitio en la computadora

```bash
python3 -m http.server 8000
```

y abrir <http://localhost:8000> en el navegador.
