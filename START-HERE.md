# ✏️ Lección 09 — Mergear ramas (fast-forward vs merge commit)

**Nivel:** 🟡 Intermedio · **Tipo:** Ejercicio · **Tiempo:** ~10 min

---

## 🎯 Qué vas a aprender
`git merge otra-rama` trae los cambios de `otra-rama` **a la rama donde estás
parado**. Hay dos resultados posibles:

**Fast-forward (FF)** — cuando tu rama **no avanzó** desde que salió la feature.
Git solo "corre el puntero" hacia adelante. **No crea merge commit**:
```
antes:  A ── B ── C  (feature)
        └ main
después: A ── B ── C  (main y feature juntas)  ← main solo se movió a C
```

**Merge commit (no-FF / three-way)** — cuando **ambas** ramas avanzaron, o cuando
lo forzás con `--no-ff`. Crea un commit con **dos padres**:
```
A ── B ─────── M  (main)
      \       /
       C ── D     (feature)
```

---

## 🔍 El escenario
Esta rama (`lesson/09-mergear-ramas`) tiene una rama compañera `lesson/09-feature`
que le agregó commits. Esta rama **no avanzó**, así que un merge normal será
**fast-forward**.

```bash
git log --oneline --graph --all
```

---

## 📋 La tarea

### Parte A — Merge fast-forward
Parado en `lesson/09-mergear-ramas`:
```bash
git merge lesson/09-feature
git log --oneline --graph
```
👀 **No hay merge commit**: la rama simplemente avanzó hasta la feature. Fijate
el mensaje de Git: dice `Fast-forward`.

Deshacelo para probar la otra forma:
```bash
git reset --hard ORIG_HEAD
```

### Parte B — Forzar un merge commit
```bash
git merge --no-ff lesson/09-feature -m "merge: integra feature (no-ff)"
git log --oneline --graph
```
👀 Ahora **sí** hay merge commit (rombo), aunque la historia permitía un FF.
`--no-ff` es útil para dejar registrado "acá se integró una rama".

Confirmá los dos padres del merge:
```bash
git log --merges -1 --pretty="%h padres:%p"
```

---

## ✅ ¿Lo lograste?
- Hiciste un merge **fast-forward** (sin merge commit) y viste el mensaje `Fast-forward`.
- Lo deshiciste con `reset --hard ORIG_HEAD`.
- Forzaste un **merge commit** con `--no-ff` y confirmaste sus dos padres.

---

## 🧠 Para pensar
- ¿Por qué a algunos equipos les gusta `--no-ff` siempre? Porque el merge commit
  agrupa visualmente "todo lo que trajo esa feature/PR" en un punto del historial.
- GitHub, al mergear una PR con "Create a merge commit", hace exactamente un
  `--no-ff`. Lo vas a ver en la lección 11.

---

## 💡 Solución
```bash
git merge lesson/09-feature            # fast-forward
git reset --hard ORIG_HEAD
git merge --no-ff lesson/09-feature -m "merge: integra feature (no-ff)"
```

➡️ **Siguiente:** `git switch main` y seguí con `lesson/10-conflictos`.
