# 📖 Lección 06 — Historial lineal vs con merges

**Nivel:** 🟢 Básico · **Tipo:** Estudio · **Tiempo:** ~8 min

---

## 🎯 Qué vas a aprender
Hay dos "formas" que puede tener la historia de un proyecto:

**Lineal** — una sola fila de commits, uno atrás del otro:
```
A ── B ── C ── D   (main)
```

**Con merges** — ramas que se separan y se vuelven a unir en un *merge commit*:
```
A ── B ─────── M   (main)
      \       /
       C ── D      (feature)
```
El commit `M` (el merge commit) tiene **dos padres**: `B` y `D`. Eso es lo que
hace que la historia se "abra" y se "cierre".

Ni uno ni otro es "mejor" siempre:
- **Lineal** → historia fácil de leer, `git bisect` limpio. Cuesta más mantenerla.
- **Con merges** → conserva el contexto de "esto se hizo en una rama aparte",
  pero el `git log` se llena de rombos.

---

## 🔍 Estudio: mirá el historial de ESTA rama
Esta rama tiene **un merge commit** hecho a propósito. Miralo con gráfico:
```bash
git log --oneline --graph
```
Vas a ver algo así:
```
*   M  merge: integra feature/login
|\
| * D  feat(login): valida password
| * C  feat(login): formulario de login
* | B  feat: home page
|/
* A  feat: base app
```
- La línea que se abre (`|\`) y se cierra (`|/`) es la rama `feature/login`.
- El commit de arriba (`M`) es el **merge commit**: fijate que junta las dos ramas.

Confirmá que `M` tiene **dos padres**:
```bash
git log --merges -1 --pretty="%h %p %s"
```
La columna `%p` va a mostrar **dos hashes** (los dos padres).

---

## 🔬 Comparación
Abrí en otra terminal (o después) una rama de ejercicio anterior, por ejemplo:
```bash
git switch lesson/04-conventional-commits
git log --oneline --graph
```
Ahí **no hay rombos**: es historia lineal. Volvé con `git switch lesson/06-lineal-vs-merge`.

---

## ✅ ¿Entendiste?
- Reconocés un merge commit en `git log --graph` (el rombo `|\ ... |/`).
- Sabés que un merge commit tiene **dos padres**.
- Podés explicar el tradeoff lineal vs merges.

---

## 🧠 Para pensar
- ¿Cómo se logra historia lineal aunque trabajes en ramas? → con **rebase**
  (lección 07) o con **squash merge** (lección 11).
- El merge commit es el único commit "sin cambios propios": no edita archivos,
  solo une dos líneas de historia.

➡️ **Siguiente:** `git switch main` y seguí con `lesson/07-rebase-vs-merge`.
