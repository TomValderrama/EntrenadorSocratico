# Comandos y proceso mental

Referencia de flujos comunes de git y terminal, con el razonamiento detrás de cada paso.

---

## Crear un repo desde local hacia GitHub, dentro de un directorio padre que ya es repo

**Situación:** Tenés una carpeta `/proyectos/` que ya es un repo de git, y dentro querés crear `/proyectos/mi-app/` como su propio repo independiente en GitHub.

**Proceso mental:**
- Git permite repos anidados. El repo padre simplemente ignora el contenido del hijo (lo ve como un directorio sin trackear).
- El hijo necesita su propio `git init`, su propio historial, y su propio remote en GitHub.
- No usar `git submodule` a menos que quieras que el padre lo gestione activamente — para repos independientes, no hace falta.

**Pasos:**

```bash
# 1. Entrar a la carpeta del proyecto hijo
cd mi-app

# 2. Inicializar git local
git init

# 3. Agregar archivos y hacer el primer commit
git add .
git commit -m "Initial commit"

# 4. Crear el repo en GitHub y conectarlo (requiere gh CLI instalado)
gh repo create mi-app --public --source=. --remote=origin --push

# Alternativa sin gh CLI:
# Crear el repo manualmente en github.com, luego:
git remote add origin https://github.com/usuario/mi-app.git
git branch -M main
git push -u origin main
```

**Por qué funciona:**
El repo padre ve la carpeta `mi-app/` como un directorio no trackeado (aparece en `git status` como untracked). Si no querés que aparezca ahí, agregalo al `.gitignore` del padre.

**Paso extra importante — ignorar el hijo desde el padre:**

```bash
# Desde el repo padre (ej: pelicanos/)
echo "mi-app/" >> .gitignore
git add .gitignore
git commit -m "Ignorar mi-app (repo independiente)"
```

Esto evita que el repo padre vea `mi-app/` como contenido sin trackear y mantiene los dos repos completamente separados.

**Ejemplo concreto de este proyecto:**
`pelicanos/` es el repo padre. `pelicanos/EntrenadorSocratico/` es su propio repo en GitHub. Se agregó `EntrenadorSocratico/` al `.gitignore` de `pelicanos/` para que no interfieran.

---
