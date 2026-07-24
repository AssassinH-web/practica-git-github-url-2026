# ✏️ Lección 03 — Referenciar issues y links en los commits

**Nivel:** 🟢 Básico · **Tipo:** Ejercicio · **Tiempo:** ~7 min

---

## 🎯 Qué vas a aprender
Un mensaje de commit no es solo texto: GitHub lo **lee** y crea enlaces. Con las
palabras justas, un commit puede **cerrar un issue automáticamente**.

### Palabras clave que cierran issues
Si en el mensaje (o en la PR) escribís una de estas seguida de `#numero`, GitHub
cierra ese issue cuando el commit llega a la rama por defecto:

| Palabra | Ejemplo |
|---------|---------|
| `Closes` | `Closes #12` |
| `Fixes` | `Fixes #12` |
| `Resolves` | `Resolves #12` |

### Referencias que enlazan (sin cerrar)
- `Refs #12` o simplemente `#12` → crea un link al issue, no lo cierra.
- `usuario/repo#12` → referencia un issue de **otro** repo.
- Pegar el hash de un commit (`a1b2c3d`) → GitHub lo convierte en link.

### Estructura de un buen mensaje
```
tipo: resumen corto en imperativo (≤ 50 chars)

Explicación opcional de POR QUÉ, no del qué.
El diff ya dice qué cambió.

Closes #12
```
La **línea en blanco** entre título y cuerpo es obligatoria: sin ella, Git trata
todo como un solo título gigante.

---

## 🔍 El escenario
En este repo hay un "issue #1" (ver `ISSUES.md`) que dice que el saludo de
`app.js` está mal escrito. Vas a arreglarlo y **cerrar el issue desde el commit**.

```bash
cat ISSUES.md
cat app.js
```

---

## 📋 La tarea

### Paso 1 — Arreglá el bug
Editá `app.js` y corregí el saludo (`"Holaa"` → `"Hola"`).

### Paso 2 — Commiteá referenciando el issue
Como el mensaje tiene título + cuerpo, usá `-m` dos veces (cada `-m` es un párrafo):
```bash
git add app.js
git commit -m "fix: corrige el saludo mal escrito" -m "Closes #1"
```
O abrí el editor con `git commit` a secas y escribí las dos partes a mano.

### Paso 3 — Verificá
```bash
git log -1
```
Deberías ver el título y, debajo, la línea `Closes #1`.

---

## ✅ ¿Lo lograste?
- `git log -1` muestra el cuerpo con `Closes #1` en una línea separada del título.
- `app.js` ya dice `"Hola"`.

---

## 🧠 Para pensar
- Cuando hagas el fork real y abras una PR con este commit, GitHub va a mostrar
  "This will close #1" y cerrará el issue al mergear. Ese es el pago real.
- Trailers extra útiles: `Co-authored-by: Nombre <email>` (acredita a otra
  persona en el commit) y `Signed-off-by:` (usado en proyectos con DCO).

---

## 💡 Solución
```bash
# editá app.js: "Holaa" -> "Hola"
git add app.js
git commit -m "fix: corrige el saludo mal escrito" -m "Closes #1"
```

➡️ **Siguiente:** `git switch main` y seguí con `lesson/04-conventional-commits`.
