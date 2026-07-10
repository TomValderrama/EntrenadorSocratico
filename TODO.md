# TODO — EntrenadorSocratico

Lista de acciones surgida del Claude Council del 2026-07-08 (sha `4bd6ef43`). Detalle completo en
`council-report-20260708-154033Z-q4bd6ef43.html` y `council-transcript-20260708-154033Z-q4bd6ef43.md`.

Veredicto en una línea: el diseño central de `main.py` (solo preguntas, nunca respuestas) está bien
orientado y no hay que reescribirlo. Lo que falta es robustez y persistencia, no andamiaje pedagógico.

## Ahora (próximas 48h)

- [ ] Envolver la llamada de streaming en `main.py` con `try/except` (`RateLimitError`,
      `APIConnectionError`, `APIStatusError`) sin perder `history` en memoria si falla.
- [ ] Guardar `history` a un archivo JSON al cerrar la sesión y cargar el más reciente al abrir
      (arregla que el currículo "reinicie en cero" cada sesión).
- [ ] Test de complacencia (Red Team / Dissent): la próxima vez que el tutor confirme "ya lo
      entendiste" en un nodo, ir de inmediato a escribir ese código en el repo real sin asistencia.
      Un solo dato dice si el riesgo de falsos positivos es teórico o real.

## Condicional

- [ ] Si el test de complacencia falla (confirmó algo que no era cierto): agregar al
      `SYSTEM_PROMPT` la regla "no confirmes un nodo sin que el usuario pegue la salida real de
      haber ejecutado el código". Todavía no requiere darle `code_execution` al tutor.

## No hacer (consenso fuerte del consejo)

- [x] ~~Construir seguimiento de nodos/Bloques, generación automática de "problema nuevo",
      calibración de dificultad~~ — descartado. RICE score más bajo de todas las opciones y
      viola el ROI que ya definiste en `PLAN_ESTUDIO.md`.

## Para pensar más adelante, sin apuro

- [ ] Evaluar si correr el tutor dentro de un harness de agente (como Claude Code, usando
      `PLAN_ESTUDIO.md` como memoria persistente) reemplaza a `main.py` por completo. Quedó
      como punto ciego del consejo, sin debate real.
- [ ] Evaluar bajar de `claude-opus-4-8` a Sonnet 5 para este chat (sin tool-use) — ~40% más
      barato con calidad similar para este caso de uso.

## Housekeeping

- [x] Decidir sobre los archivos del reporte del consejo — ya quedaron commiteados (`eb61916`).
