# Plan de estudio — Nudos de conocimiento

Guía de sesiones para el EntrenadorSocratico. El objetivo no es repetir lo que ya
existe en mis repos, sino **alcanzar el nivel para escribirlo yo solo, sin agente**, y
sobre todo para **resolver problemas nuevos** que aún no he tocado.

## Cómo usar este plan

- **Una sesión = un nodo** (o un sub-nodo). Historial de la API reiniciado por sesión
  para que el costo no se dispare.
- **Cada bloque se valida sobre mi propio código real**, no con ejercicios de juguete.
- **Regla de oro — problema nuevo al cierre:** cada bloque termina con un problema que
  *no* está en mis repos. Si solo puedo rehacer lo que ya hice, no aprendí: memoricé.
  La señal de aprendizaje real es resolver "el problema de al lado".
- **Regla de explicabilidad:** no doy un nodo por cerrado hasta poder explicarle el
  principio a otra persona con mis palabras.

## Prioridad

Ordenado por **ROI = (delta entre mi nivel autónomo y mi código asistido) × (frecuencia
de uso)**. No por dificultad. Los bloques **0 → 1 → 2 → 3 son el 70% del valor**: si solo
hiciera esos cuatro, ya doy el salto de "científico que scriptea" a "programador".

---

### Bloque 0 — Modelo de datos de Python (fundamento)

**Nodos:** nombres vs. objetos · mutabilidad y referencias · scope y namespaces · por qué
`import` va arriba · comprehensions (list/dict/set).

**Por qué yo:** mis funciones importan dentro del cuerpo (`ocean-data-analysis/preprocessing.py`).
Es síntoma de no tener claro el namespace. Es la base de todo lo demás.

**Proyecto de validación:** arreglar los imports de `ocean-data-analysis` y entender
*por qué* funcionaba igual antes.

**Problema nuevo:** explicar qué pasa al mutar una lista pasada como argumento por default.

---

### Bloque 1 — NumPy / pandas idiomático (mi mayor delta)

**Nodos:** vectorización (por qué evita el `for`) · `.loc`/`.iloc` · `groupby` · `merge` ·
manejo de `NaN` · interpolación nativa (`.interpolate()`, `.fillna()`, `.shift()`).

**Por qué yo:** mis `interpolate` e `interpolate2` son loops manuales de lo que pandas
hace en una línea. Es mi pan diario, mal hecho. Aquí está el delta más grande.

**Proyecto de validación:** reemplazar `interpolate`/`interpolate2` por **una** función
vectorizada y demostrar que da el mismo resultado.

**Problema nuevo:** limpiar datos de oxígeno (miniDOT) con huecos irregulares **y**
outliers — algo que no está resuelto en mis repos.

---

### Bloque 2 — De script a software (el salto a "profesional")

**Nodos:** DRY / eliminar duplicación · diseñar funciones (una cosa, argumentos claros) ·
estructura de módulos · `__init__.py` · layout `src/`.

**Por qué yo:** tengo `Checkpoints/`, `v2/` y copy-paste por todos lados. Sé resolver, no
sé *organizar*.

**Proyecto de validación:** unificar las 3 copias de `AutoInformeCorrientes` en
`rutinas-pelicanos` en un solo módulo sin duplicación.

**Problema nuevo:** diseñar desde cero la estructura de módulos de un proyecto que aún no
existe (ver `RUTA_SENIOR.md`).

---

### Bloque 3 — Tests con pytest (la red de seguridad)

**Nodos:** `assert` · fixtures · parametrización · qué testear y qué no · tests como
documentación viva · TDD básico.

**Por qué yo:** **cero tests en 23 repos.** Es la diferencia más grande entre mi código y
uno senior. Y sin tests, refactorizar da miedo.

**Proyecto de validación:** escribir tests para `mbes-pipeline` que verifiquen la
conversión s7k → xyz.

**Problema nuevo:** escribir el test *antes* del código de una función que aún no existe.

---

### Bloque 4 — Robustez: errores, logging, pathlib, config

**Nodos:** `try/except` y excepciones propias · `logging` vs `print` · `pathlib` · archivos
de config / `.env` · no hardcodear rutas.

**Por qué yo:** mi código nuevo (`procesar_s7k.py`) ya los usa, pero me los escribió el
agente. Necesito *poder* escribirlos.

**Proyecto de validación:** reproducir el patrón de `logging`/`argparse` de
`procesar_s7k.py` desde cero, **sin mirarlo**.

**Problema nuevo:** diseñar el manejo de errores de un pipeline que procesa 100 archivos y
no debe morir si uno falla.

---

### Bloque 5 — xarray / netCDF idiomático (multiplicador de velocidad)

**Nodos:** `DataArray` vs `Dataset` · indexado por coordenadas · `groupby`/`resample` ·
operaciones sobre dimensiones · I/O netCDF.

**Por qué yo:** lo uso para ERA5, CROCO, modelos. Bien dominado, multiplica mi velocidad real.

**Proyecto de validación:** reescribir una rutina de `Vientos` (asimilación ERA5) con
`xarray` limpio.

**Problema nuevo:** combinar dos datasets con grillas temporales distintas.

---

### Bloque 6 — Colaboración: git, type hints, docstrings

**Nodos:** branches · pull requests · `.gitignore` · type hints · `mypy` · docstrings
(NumPy style).

**Por qué yo:** ya tengo `comandos.md` (buena base). Falta branches/PRs y tipado. Esto es
trabajar con otros — y la base de un proyecto open source.

**Proyecto de validación:** hacer un PR real sobre `mbes-pipeline` con type hints y
revisarlo yo mismo como si fuera de un junior.

**Problema nuevo:** revisar un PR ajeno (de un fork de Kluster) y dejar comentarios.

---

### Bloque 7 — Especialización (el techo, no la base)

**Nodos:** geopandas/rasterio/folium · profiling · cuándo vectorizar / numba / dask ·
APIs (Claude, GEE).

**Por qué yo:** dominio ya fuerte. Esto es pulir, por eso va al final.

**Proyecto de validación:** optimizar el generador de `Mapas`.

**Problema nuevo:** procesar una nube de puntos más grande que la RAM.

---

### Bloque 8 — ML aplicado a datos oceanográficos

**Nodos:** cuándo usar ML vs estadística clásica · feature engineering con pandas/xarray ·
`scikit-learn` (LinearRegression, RandomForest, GradientBoosting) · validación cruzada
temporal (por qué no aleatoria con series de tiempo) · métricas de regresión (RMSE, R²,
residuos) · cuándo DL no es necesario.

**Por qué yo:** tengo datos de oxígeno disuelto (miniDOT), temperatura, salinidad,
variables atmosféricas (ERA5) y salidas de modelos (CROCO, SWAN, WRF). El paso natural
es construir modelos predictivos que conecten esas fuentes. ML clásico cubre el 90%
de estos casos — no necesito redes neuronales profundas.

**Proyecto de validación:** modelo predictivo de oxígeno disuelto en función de
temperatura, profundidad, viento y época del año. Validar con split temporal (no
aleatorio). Comparar Random Forest vs regresión lineal e interpretar los residuos.

**Problema nuevo:** el modelo funciona bien en el período de entrenamiento pero falla
en otra estación del año. Diagnosticar por qué y proponer solución.

---

## El método de preguntas (para el tutor y para mí)

Un buen diálogo socrático **no es un número de mensajes, es una estructura**. Un nodo nuevo
y difícil puede ser 20-40 intercambios; un refuerzo, 3-4. Fases:

1. **Activar** lo que ya sé
2. **Tropezar** con un caso concreto (correr código y ver que falla)
3. **Diagnosticar** mi modelo mental
4. **Contraejemplos** ("¿y si...?")
5. **Generalizar** — formular la regla con mis palabras
6. **Transferir** — aplicarla a algo nuevo
7. **Metacognición** — ¿cómo lo supe? ¿cuándo NO aplica?

Las fases 5-7 son donde se fija el aprendizaje. Técnicas que suben la calidad: **lucha
productiva** (estar atascado un rato es donde se aprende), **dirigido por el error**,
**enseñar de vuelta**, **nunca confirmar antes de tiempo**, **usar mi propio código como material**.
