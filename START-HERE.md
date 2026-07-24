# ✏️ Lección 04 — Conventional Commits

**Nivel:** 🟢 Básico · **Tipo:** Ejercicio · **Tiempo:** ~10 min

---

## 🎯 Qué vas a aprender
**Conventional Commits** es una convención para el título del commit:

```
tipo(scope opcional): descripción en imperativo
```

Con esto, herramientas automáticas generan changelogs y deciden la versión
(semver) sola. Además, leer el historial se vuelve trivial.

### Los tipos más usados
| Tipo | Cuándo | ¿Sube versión? |
|------|--------|----------------|
| `feat` | Nueva funcionalidad | minor (0.**1**.0) |
| `fix` | Corrección de bug | patch (0.0.**1**) |
| `docs` | Solo documentación | no |
| `refactor` | Cambio interno sin cambiar comportamiento | no |
| `test` | Agregar o corregir tests | no |
| `chore` | Tareas de mantenimiento (deps, config) | no |
| `style` | Formato, espacios (sin lógica) | no |
| `perf` | Mejora de rendimiento | patch |

### El `scope` (opcional)
Acota el área: `feat(auth): ...`, `fix(api): ...`.

### Breaking changes
Un cambio que rompe compatibilidad se marca con `!` y/o footer:
```
feat(api)!: cambia el formato de la respuesta

BREAKING CHANGE: el campo `user` ahora es un objeto, no un string.
```
Esto sube la versión **major** (**1**.0.0).

---

## 🔍 El escenario
Esta rama tiene un mini-proyecto (`calc.js`, `README.md`). Vas a hacer **3
cambios** y commitear cada uno con el **tipo correcto**.

```bash
cat calc.js
```

---

## 📋 La tarea (3 commits, uno por cambio)

### Commit 1 — una funcionalidad nueva → `feat`
Agregá una función `restar` a `calc.js`. Luego:
```bash
git add calc.js
git commit -m "feat(calc): agrega la función restar"
```

### Commit 2 — un bug → `fix`
En `calc.js`, la función `sumar` está mal (usa `-` en vez de `+`). Corregila y:
```bash
git add calc.js
git commit -m "fix(calc): corrige sumar que restaba"
```

### Commit 3 — documentación → `docs`
Agregá una línea al `README.md` explicando la calculadora, y:
```bash
git add README.md
git commit -m "docs: documenta el uso de la calculadora"
```

### Verificá
```bash
git log --oneline -3
```

---

## ✅ ¿Lo lograste?
`git log --oneline -3` muestra, de arriba hacia abajo:
```
docs: documenta el uso de la calculadora
fix(calc): corrige sumar que restaba
feat(calc): agrega la función restar
```

---

## 🧠 Para pensar
- El **imperativo** ("agrega", no "agregado" ni "agregando") es el estándar:
  el commit completa la frase *"Este commit, al aplicarse, va a…"*.
- ¿Por qué separar en 3 commits y no uno solo? Porque cada commit es una unidad
  revertible y legible. Un `git revert` del fix no toca la feature.

---

## 💡 Solución
```bash
# 1. agregá restar() a calc.js
git add calc.js && git commit -m "feat(calc): agrega la función restar"
# 2. corregí sumar() (- por +)
git add calc.js && git commit -m "fix(calc): corrige sumar que restaba"
# 3. documentá en README.md
git add README.md && git commit -m "docs: documenta el uso de la calculadora"
```

➡️ **Siguiente:** `git switch main` y seguí con `lesson/05-commits-verificados`.
