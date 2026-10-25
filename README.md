# Text Analyzer

Proyecto integrador de Python, pytest e integración continua. Biblioteca de lógica
backend con una interfaz de consola; no incluye servidor HTTP ni base de datos.
Python 3.11 o superior. CI se ejecuta con Python 3.11.

## Funciones y límites

- Conteo de palabras: grupos alfanuméricos Unicode. Guiones, apóstrofes y guiones bajos separan palabras; números cuentan.
- Caracteres: puntos de código después de normalizar a NFC. No equivale necesariamente a símbolos visuales: un emoji compuesto puede contar varias unidades.
- Sin espacios: omite espacios, tabulaciones y saltos de línea.
- Oraciones: segmentos con letras o números separados por `.`, `!` o `?`. No distingue abreviaturas ni decimales. Los saltos de línea no separan oraciones.
- Texto vacío: todos los conteos son cero. Tipos distintos de `str`: `TypeError`.

## Instalación en Windows (PowerShell)

Extrae esta carpeta en `$HOME\Documents\GitHub\text_analyzer`.
Instala Python 3.11 o superior y Git si no están disponibles.
No necesitas activar el entorno virtual.

```powershell
Set-Location "$HOME\Documents\GitHub\text_analyzer"
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe main.py "Hola mundo."
```

Resultado: `words=2`, `characters=11`, `characters_without_spaces=10`, `sentences=1`.

## Validación local

```powershell
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
.\.venv\Scripts\python.exe -m pytest
```

Para corregir formato: `.\.venv\Scripts\python.exe -m ruff format .`.
pytest mide líneas y ramas, incluye la biblioteca y la consola, genera
`coverage.xml` y termina con error si la cobertura total es menor al 80 %.
Las dependencias de desarrollo están fijadas en `requirements-dev.txt`.

## Publicación y práctica

Sigue `GUIA_GITHUB.md`. El YAML por sí solo no protege la rama: configura
el check obligatorio `quality` en GitHub. El paquete no acredita una ejecución
remota, una revisión externa ni una contribución aceptada por otro proyecto.

## Estructura

- `analyzer/`: lógica reutilizable.
- `tests/`: pruebas unitarias y de consola.
- `main.py`: entrada de consola.
- `pyproject.toml`: configuración de calidad y cobertura.
- `.github/workflows/ci.yml`: workflow para todos los pushes y PRs.
- `CONTRIBUTING.md`: reglas para colaboradores.
- `GUIA_GITHUB.md`: publicación, PR, fallo controlado y evidencias.
- `VALIDACION_LOCAL.txt`: resultados reales obtenidos al preparar este paquete.

## Licencia

MIT. Consulta `LICENSE`.
