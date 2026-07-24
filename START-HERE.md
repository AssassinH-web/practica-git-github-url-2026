# ✏️ Lección 11 — Squash merge vs merge commit

**Nivel:** 🟡 Intermedio · **Tipo:** Ejercicio · **Tiempo:** ~10 min

---

## 🎯 Qué vas a aprender
Cuando integrás una rama con **muchos commits chiquitos y desprolijos** ("wip",
"arreglo", "ahora sí"), tenés dos maneras de meterla en la principal:

**Merge commit** (`--no-ff`) → conserva **todos** los commits de la feature + un
merge commit que los une:
```
main:  A ─────────────── M
        \               /
         wip ─ fix ─ ok        (los 3 quedan en la historia)
```

**Squash merge** (`--squash`) → **aplasta** los 3 commits en **uno solo** y lo
commiteás vos con un mensaje limpio. Los commits originales **no** entran a main:
```
main:  A ── S     (S = un único commit con TODO el cambio de la feature)
```

| | Merge commit | Squash |
|---|---|---|
| Commits de la feature en main | Sí (todos) | No (se funden en 1) |
| Historia de main | Con rombos, detallada | Lineal, limpia |
| Ideal para | Conservar el detalle del trabajo | Un commit por feature/PR |

---

## 🔍 El escenario
`lesson/11-feature` tiene **3 commits desprolijos** sobre `feature.txt`. Miralos:
```bash
git log --oneline lesson/11-feature
```

---

## 📋 La tarea

### 🔵 Camino 1 — Merge commit (conserva los 3)
Parado en `lesson/11-squash-vs-merge`:
```bash
git merge --no-ff lesson/11-feature -m "merge: integra feature"
git log --oneline --graph
```
👀 Ves los **3 commits** de la feature + el merge commit.

Deshacelo:
```bash
git reset --hard ORIG_HEAD
```

### 🟢 Camino 2 — Squash merge (los funde en 1)
```bash
git merge --squash lesson/11-feature
git status          # los cambios están en staging, SIN commitear todavía
git commit -m "feat: agrega la feature completa"
git log --oneline --graph
```
👀 Ahora hay **un solo commit** con todo el cambio. Los "wip"/"fix" **no están**.
Fijate también que `--squash` **no** hace el commit solo: lo hacés vos (ese es el
punto, escribís un mensaje limpio).

---

## ✅ ¿Lo lograste?
- Con el camino 1 viste los 3 commits + merge commit en el grafo.
- Lo deshiciste con `reset --hard ORIG_HEAD`.
- Con el camino 2 quedó **un único commit** limpio y sin los "wip".

---

## 🧠 Para pensar
- En GitHub, al mergear una PR, el botón ofrece las 3 opciones:
  **"Create a merge commit"** (= `--no-ff`), **"Squash and merge"** (= `--squash`),
  y **"Rebase and merge"** (= rebase, lección 07). Es la misma decisión.
- Squash pierde el detalle intermedio: si esos pasos importan para depurar
  después, quizás no quieras aplastarlos. Para una PR de feature típica, squash
  deja `main` bien prolijo.

---

## 💡 Solución
```bash
# Camino merge commit
git merge --no-ff lesson/11-feature -m "merge: integra feature"
git reset --hard ORIG_HEAD
# Camino squash
git merge --squash lesson/11-feature
git commit -m "feat: agrega la feature completa"
```

➡️ **Siguiente:** `git switch main` y seguí con `lesson/12-como-funciona-github`.
