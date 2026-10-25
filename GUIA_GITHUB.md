# Guía de entrega y práctica

## 1. Crear el repositorio

En GitHub crea un repositorio público llamado `text_analyzer`, sin README,
licencia ni .gitignore iniciales: ya se incluyen. Copia su URL HTTPS.
En PowerShell, desde la carpeta extraída:

```powershell
Set-Location "$HOME\Documents\GitHub\text_analyzer"
git init -b main
git add .
git commit -m "feat: agregar analizador con pruebas y CI"
$repoUrl = Read-Host "Pega la URL HTTPS de tu repositorio"
git remote add origin $repoUrl
git push -u origin main
```

Si Git pide identidad, configura tu nombre y correo de GitHub con
`git config user.name "Tu nombre"` y `git config user.email "Tu correo"`.
Repite el commit y el push. Usa la autenticación que solicite Git; no coloques
tokens en archivos del proyecto.

## 2. Revisar la primera ejecución

Abre la pestaña Actions, workflow CI, job quality. Confirma instalación,
Ruff, formato y pytest. Guarda el enlace y una captura de la ejecución verde.
Si falla, abre el paso rojo y lee el primer error relevante.

## 3. Proteger main

En Settings > Branches crea una regla de protección clásica para `main`.
Activa Require a pull request before merging y Require status checks to pass
before merging. Selecciona el check `quality`, después de su primera ejecución.
Activa Require branches to be up to date before merging y Do not allow
bypassing the above settings. No permitas force pushes ni borrado de la rama.
Guarda y captura la configuración. Estas reglas están disponibles en repositorios
públicos con GitHub Free; en privados su disponibilidad depende del plan.

Si trabajas solo, no exijas aprobación de otra persona. Si tienes colaborador,
invítalo y exige una aprobación para demostrar revisión real. Un PR propio no
sustituye una revisión externa.

## 4. Pull Request con fallo controlado

Crea una rama de práctica:

```powershell
git switch -c feature/prueba-ci
@'
from analyzer import count_words


def test_regresion_palabras():
    assert count_words("Hola mundo") == 3
'@ | Set-Content -Encoding utf8 tests/test_regression.py
.\.venv\Scripts\python.exe -m ruff format tests/test_regression.py
git add tests/test_regression.py
git commit -m "test: demostrar deteccion de un conteo incorrecto"
git push -u origin feature/prueba-ci
```

En GitHub abre Compare & pull request hacia `main`. El resultado esperado
correcto es 2, pero la prueba exige 3 para demostrar un fallo deliberado.
En Actions identifica `AssertionError` y `assert 2 == 3`.
Captura el job rojo y el PR con merge bloqueado. No desactives la protección.

## 5. Corregir en la misma rama

Abre `tests/test_regression.py` y cambia únicamente `== 3` por `== 2`.

```powershell
.\.venv\Scripts\python.exe -m ruff check .
.\.venv\Scripts\python.exe -m ruff format --check .
.\.venv\Scripts\python.exe -m pytest
git add tests/test_regression.py
git commit -m "test: corregir expectativa de conteo"
git push
```

El mismo PR se actualiza. Espera CI verde, pide revisión si corresponde y
fusiona desde GitHub. Guarda enlaces al PR, sus commits y ambas ejecuciones.
Después:

```powershell
git switch main
git pull --ff-only
git branch -d feature/prueba-ci
```

Si usaste Squash merge, Git puede rechazar el borrado local porque conserva
commits distintos. Puedes conservar la rama; no necesitas forzar su borrado.

## 6. Interpretar errores

| Resultado | Interpretación y corrección |
| --- | --- |
| AssertionError | Compara resultado esperado y real. Corrige el código o la expectativa según el requisito. |
| ModuleNotFoundError | Verifica dependencias y ejecuta desde la raíz con `python -m pytest`. |
| Cobertura inferior al 80 % | Agrega pruebas de escenarios y rutas faltantes; no reduzcas el umbral. |
| Ruff F401 | Elimina el import no utilizado. |
| Would reformat | Ejecuta Ruff format y confirma el cambio. |
| Check pendiente | Comprueba nombre `quality`, eventos y que Actions esté habilitado. |

## 7. Evidencias que debes obtener

- URL pública del repositorio y licencia.
- Captura de ejecución local y cobertura.
- Rama feature y PR con descripción.
- Pipeline fallido con su error visible.
- Merge bloqueado por el check obligatorio.
- Commit de corrección y pipeline exitoso.
- Protección de main y PR fusionado.
- Comentarios de revisión, si participó un colaborador.

No presentes resultados locales como ejecuciones de GitHub. Este ejercicio
crea un proyecto propio abierto; si la rúbrica exige aportar a un proyecto de
terceros, necesitarás además un PR en ese proyecto.

## Referencias oficiales

- https://docs.github.com/en/actions/tutorials/build-and-test-code/python
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks
- https://github.com/actions/setup-python
