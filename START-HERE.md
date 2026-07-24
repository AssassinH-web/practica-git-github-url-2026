# ✏️ Lección 07 — `rebase` vs `merge`

**Nivel:** 🟢 Básico · **Tipo:** Ejercicio · **Tiempo:** ~12 min

---

## 🎯 Qué vas a aprender
Tenés dos ramas que **divergieron** (cada una avanzó por su lado). Hay dos formas
de integrarlas, y dan historiales distintos:

**`merge`** — crea un *merge commit* que une las dos líneas. **No reescribe** nada:
```
A ── M1 ── M2 ─────── X   (esta rama)
      \              /
       F1 ── F2 ─────       (feature)   →  X = merge commit (2 padres)
```

**`rebase`** — "levanta" los commits de feature y los **vuelve a aplicar** encima
de la otra rama. La historia queda **lineal**, sin merge commit:
```
A ── M1 ── M2 ── F1' ── F2'   (feature, ya rebasada)
```
Ojo: `F1'` y `F2'` son commits **nuevos** (hash distinto): rebase reescribe historia.

> **🔑 La regla de oro del rebase:** nunca rebasees commits que ya **compartiste**
> (pusheados a una rama que otros usan). Rebasear historia compartida rompe el
> repo de los demás. Rebase es para tu trabajo local, aún privado.

---

## 🔍 El escenario
Esta rama (`lesson/07-rebase-vs-merge`) y la rama `lesson/07-feature` divergieron
desde un commit base. Editan **archivos distintos**, así que no habrá conflictos
(eso es la lección 10).

Observá la divergencia:
```bash
git log --oneline --graph --all
```
Vas a ver que las dos ramas salen del mismo commit base y siguen caminos separados.

---

## 📋 La tarea — probá los DOS caminos

### 🔵 Camino 1 — MERGE (crea merge commit)
Estás parado en `lesson/07-rebase-vs-merge`. Traé la feature con merge:
```bash
git merge lesson/07-feature -m "merge: integra feature"
git log --oneline --graph
```
👀 Fijate el **rombo** y el merge commit arriba.

Ahora **deshacelo** para probar el otro camino (ORIG_HEAD = dónde estabas antes del merge):
```bash
git reset --hard ORIG_HEAD
git log --oneline --graph    # volvió a como estaba
```

### 🟢 Camino 2 — REBASE (historia lineal)
Ahora rebaseamos la **feature** encima de esta rama:
```bash
git switch lesson/07-feature
git rebase lesson/07-rebase-vs-merge
git log --oneline --graph
```
👀 **No hay rombo**: los commits de feature quedaron en fila, encima de los de
esta rama. Historia lineal.

Volvé:
```bash
git switch lesson/07-rebase-vs-merge
```

---

## ✅ ¿Lo lograste?
- Viste el **merge commit** (rombo) con el camino 1, y lo deshiciste con `reset --hard ORIG_HEAD`.
- Viste la **historia lineal** con el camino 2 (rebase).
- Podés explicar que rebase **reescribe** (hashes nuevos) y merge **no**.

---

## 🧠 Para pensar
- Después de rebasear la feature, si ahora hicieras `git merge lesson/07-feature`
  desde esta rama, sería un **fast-forward** (sin merge commit), porque la feature
  ya es descendiente directa. Probalo.
- Equipos que quieren `main` **lineal** → rebase antes de mergear, o *squash merge*
  (lección 11). Equipos que quieren registrar "esto vino de tal rama" → merge commit.

---

## 💡 Solución
```bash
# Camino merge
git merge lesson/07-feature -m "merge: integra feature"
git reset --hard ORIG_HEAD
# Camino rebase
git switch lesson/07-feature
git rebase lesson/07-rebase-vs-merge
git switch lesson/07-rebase-vs-merge
```

➡️ **Siguiente:** `git switch main`. ¡Terminaste el nivel básico! Sigue el
intermedio con `lesson/08-crear-ramas`.
