# ✏️ Lección 01 — Tu primer commit

**Nivel:** 🟢 Básico · **Tipo:** Ejercicio · **Tiempo:** ~5 min

---

## 🎯 Qué vas a aprender
Un **commit** es una foto de tu proyecto en un momento dado. Para crearlo hay
**dos pasos**:
1. `git add` → elegís *qué* cambios entran en la foto (los pasás al *staging area*).
2. `git commit` → sacás la foto y le ponés un mensaje.

Mucha gente cree que `commit` guarda todo automáticamente. **No.** Git solo
mete en el commit lo que vos pusiste en *staging* con `add`. Entender esa
separación es la base de todo lo demás.

```
  tu edición        git add           git commit
 (working tree) ───────────▶ (staging) ──────────▶ (historial)
```

---

## 📋 La tarea
Vas a crear un archivo y hacer tu primer commit con él.

### Paso 1 — Creá un archivo
Creá un archivo `sobre-mi.md` con una línea sobre vos. Por ejemplo:
```bash
echo "# Hola, soy [tu nombre] y estoy aprendiendo Git." > sobre-mi.md
```

### Paso 2 — Mirá el estado
```bash
git status
```
Deberías ver `sobre-mi.md` en rojo bajo **"Untracked files"** (Git lo ve pero
todavía no lo sigue).

### Paso 3 — Agregalo al staging
```bash
git add sobre-mi.md
git status
```
Ahora `sobre-mi.md` aparece en verde bajo **"Changes to be committed"**.

### Paso 4 — Hacé el commit
```bash
git commit -m "docs: agregar sobre-mi"
```

### Paso 5 — Verificá
```bash
git log --oneline
```
Deberías ver tu commit arriba de todo. 🎉

---

## ✅ ¿Lo lograste?
- `git log --oneline` muestra tu commit `docs: agregar sobre-mi`.
- `git status` dice **"nothing to commit, working tree clean"**.

---

## 🧠 Para pensar
- ¿Qué pasa si editás `sobre-mi.md` otra vez *después* del commit y hacés
  `git status`? (Spoiler: vuelve a aparecer como modificado — la foto anterior
  no cambia.)
- Probá `git add .` para agregar *todo* de una. Útil, pero peligroso: metés en
  la foto cosas que quizás no querías.

---

## 💡 Solución
```bash
echo "# Hola, soy Daniel y estoy aprendiendo Git." > sobre-mi.md
git add sobre-mi.md
git commit -m "docs: agregar sobre-mi"
```

➡️ **Siguiente:** volvé a `main` con `git switch main` y seguí con
`lesson/02-amend`.
