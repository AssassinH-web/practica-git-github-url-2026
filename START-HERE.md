# ✏️ Lección 02 — Corregir el último commit con `--amend`

**Nivel:** 🟢 Básico · **Tipo:** Ejercicio · **Tiempo:** ~5 min

---

## 🎯 Qué vas a aprender
`git commit --amend` **reemplaza** el último commit por uno nuevo. Sirve para:
- Corregir el **mensaje** (typo, mensaje poco claro).
- Agregar un archivo que **te olvidaste** de incluir.

⚠️ **Importante:** `amend` no "edita" el commit, lo **rehace** (nuevo hash). Por eso
solo se usa en commits que **todavía no pusheaste** (o que sos el único que tiene).
Amendear algo ya compartido reescribe la historia de los demás → problemas.

---

## 🔍 El escenario
Esta rama ya tiene un commit con **dos errores**, hechos a propósito:
1. El mensaje tiene typos: `docs: agrega nots recueridas`.
2. Te olvidaste de agregar el archivo `autor.md`.

Miralo:
```bash
git log --oneline -1
cat notas.md
```

---

## 📋 La tarea

### Parte A — Arreglar el mensaje
```bash
git commit --amend -m "docs: agrega notas requeridas"
```
Verificá:
```bash
git log --oneline -1
```
El mensaje quedó corregido y el **hash cambió** (es un commit nuevo).

### Parte B — Agregar el archivo olvidado
```bash
echo "Autor: [tu nombre]" > autor.md
git add autor.md
git commit --amend --no-edit
```
`--no-edit` mantiene el mensaje actual sin abrir el editor.

Verificá que `autor.md` entró en el commit:
```bash
git show --stat HEAD
```
Deberías ver **`notas.md`** y **`autor.md`** en el mismo commit.

---

## ✅ ¿Lo lograste?
- `git log --oneline -1` muestra `docs: agrega notas requeridas`.
- `git show --stat HEAD` lista `notas.md` **y** `autor.md`.

---

## 🧠 Para pensar
- Compará el hash del commit antes y después. Son distintos: `amend` crea un
  commit nuevo y "abandona" el viejo (queda huérfano, recuperable con `reflog`).
- ¿Y si querés corregir un commit que **no es** el último? Ahí ya no alcanza
  `amend`; se usa `rebase -i` (lo vemos más adelante).

---

## 💡 Solución
```bash
git commit --amend -m "docs: agrega notas requeridas"
echo "Autor: [tu nombre]" > autor.md
git add autor.md
git commit --amend --no-edit
```

➡️ **Siguiente:** `git switch main` y seguí con `lesson/03-referencias`.
