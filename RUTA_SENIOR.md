# Ruta a Senior — con proyecto capstone

Este documento extiende `PLAN_ESTUDIO.md`. Los nudos de conocimiento me dan el **piso**
(de "científico que scriptea" a "programador"). Esta ruta me lleva del piso al **techo**:
de programador a **senior**, usando agentes de IA como aceleradores **sin desaprender**.

El vehículo es un proyecto que **aún no existe** y que justifica cada habilidad senior:

> ## Proyecto capstone: **Qimera open source**
> Un pipeline/editor de batimetría multihaz (MBES) libre, alternativa a QPS Qimera.
> Conecta con lo que ya tengo (`mbes-pipeline`, lectura de `.s7k`) y con mi compromiso de
> coordinar el fork comunitario de Kluster.

Un capstone así es perfecto para ir junior → senior porque **obliga** a arquitectura,
performance con datos grandes, tests, empaquetado y trabajo en comunidad. No se puede
hacer a punta de scripts sueltos.

---

## La idea central

**Senior no es "escribir código rápido".** Es **juicio**: arquitectura, tradeoffs, depurar
lo raro, saber qué es "bueno", revisar, ser dueño del resultado. El agente hace barata la
*implementación* — y eso **sube el precio del juicio**. Las habilidades senior valen *más*
en el mundo con agentes, no menos.

**El peligro:** usar el agente para saltarme los peldaños que construyen ese juicio. La
regla que lo evita:

> **Delego lo que ya sabría hacer; lucho con lo que aún no.**
> El agente es para no perder tiempo en lo resuelto, no para evitar la lucha que construye al senior.

---

## Las 3 fases (con agentes)

### Fase 1 — Aprendiendo (ahora)
Agente como **tutor, no como autor** (el EntrenadorSocratico). Minimizo la generación de
código. Completo `PLAN_ESTUDIO.md`.

### Fase 2 — Consolidando
Uso el agente, pero **escribo yo el 20% difícil** (lógica central, decisiones) y le delego
el 80% aburrido (boilerplate, conversiones repetitivas).
- **Regla de explicabilidad:** no mergeo una línea que no pueda explicar. Si no puedo, le
  pido al agente que me la *enseñe* ("¿por qué X en vez de Y?"), no que solo la escriba.
- **Yo escribo el test/la spec; el agente implementa.** Así soy dueño del criterio de "correcto".

### Fase 3 — Senior
Dirijo al agente como un tech lead dirige a un junior. Soy dueño de: arquitectura,
descomposición, spec, revisión y verificación. El agente implementa bajo mi criterio.
- Reviso todo como si fuera un PR ajeno: busco el bug, el caso borde, la duplicación.
- Uso el agente para **explorar** alternativas ("dame 3 diseños y sus tradeoffs"); **yo decido**.
- Codeo sin agente periódicamente, como mantenimiento del músculo.

---

## Currículo senior mapeado al capstone

Cada milestone del Qimera open source entrena una competencia senior. El orden es
incremental: cada uno depende del anterior.

| # | Milestone del proyecto | Competencia senior que entrena | Cómo entran los agentes |
|---|---|---|---|
| **M1** | **Diseño de arquitectura**: definir módulos (I/O, corrección, limpieza, grillado, exportación), interfaces entre ellos, formatos de datos internos | Pensar el sistema antes de codear; tradeoffs; descomposición | Explorar 2-3 arquitecturas con el agente; **yo** elijo y justifico |
| **M2** | **Lectores de formatos** (.s7k Reson/Norbit; luego Kongsberg .all/.kmall) sobre una interfaz común | Abstracción; diseñar para la extensión; leer specs binarias | Agente implementa el parser bajo mi interfaz y mis tests |
| **M3** | **Correcciones**: SVP (velocidad del sonido), navegación/SBET, marea, refracción | Correctitud numérica; validar contra verdad conocida | Yo escribo los tests de correctitud; agente implementa |
| **M4** | **Limpieza de nube de puntos**: rechazo de outliers (automático + criterios manuales) | Algoritmos; performance con millones de puntos | Yo defino el algoritmo; agente optimiza; **yo** verifico |
| **M5** | **Grillado** (CUBE u otro) + **incertidumbre** (TPU) | Algoritmos de referencia; reproducir un paper | Agente ayuda a leer el paper; yo implemento el núcleo |
| **M6** | **Exportación**: BAG, GeoTIFF, XYZ | Interoperabilidad; estándares (IHO) | Delegable casi entero; yo reviso conformidad |
| **M7** | **Tests + CI**: cobertura, GitHub Actions, datos de prueba | Calidad sistemática; confianza para refactorizar | Agente genera tests; yo decido qué es suficiente |
| **M8** | **Empaquetado**: `pyproject.toml`, instalable, versionado, docs | Hacer software usable por otros | Delegable; yo defino la API pública |
| **M9** | **Performance**: profiling, dask/numba para nubes > RAM | Optimizar con datos; medir antes de optimizar | Agente propone; yo mido y decido |
| **M10** | **Visualización / editor 3D** de la nube | Lo más difícil; UX; integrar todo | Yo dirijo la arquitectura; agente implementa piezas |
| **M11** | **Comunidad open source**: coordinación con forks de Kluster (Brian Miles, Alex Schimel, UKHO, BSH), issues, PRs, gobernanza | Mentoría, revisión, ownership — la marca del senior | El agente no puede hacer esto por mí; es 100% juicio humano |

---

## Cómo sé que llegué a senior

No es un título ni una cantidad de código. Son señales:

- **Puedo explicar cada decisión de arquitectura** y por qué descarté las alternativas.
- **Reviso código (mío o de un agente) y encuentro lo que está mal** antes de que falle.
- **Escribo el test/la spec primero**: soy dueño del criterio de correcto.
- **Resuelvo problemas nuevos** que no están en ningún repo ni en ningún tutorial.
- **Otros usan lo que construí** y puedo mantenerlo y guiar a quien contribuye.
- **Uso el agente para ir más rápido en lo que ya domino**, y aún puedo trabajar sin él.

Usado así, llego a senior **más rápido** que sin agente: automatizo la práctica de lo que
ya domino y concentro mi energía en juicio, diseño y depuración — justo lo que el agente
*no* puede tener por mí.
