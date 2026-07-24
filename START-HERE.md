# ✏️ Lección 14 — `cherry-pick`: traer un commit puntual

**Nivel:** 🔴 Avanzado · **Tipo:** Ejercicio · **Tiempo:** ~10 min

---

## 🎯 Qué vas a aprender
`git cherry-pick <hash>` copia **un commit específico** de otra rama y lo aplica
sobre la tuya, como un commit nuevo. No traés toda la rama: solo ese cambio.

```
otra-rama:  A ── B ── C ── D
                      ▲
                      │ cherry-pick C
tu-rama:    X ── Y ── C'      (C' = mismo cambio que C, hash nuevo)
```

**Caso típico:** hay un bugfix urgente en una rama de desarrollo y lo necesitás
**ya** en producción, sin arrastrar el resto de los cambios de esa rama.

⚠️ Igual que rebase, cherry-pick **crea un commit nuevo** (hash distinto). Si
después mergeás las dos ramas, Git suele reconocer que es el mismo cambio, pero
puede duplicarlo — usalo con criterio.

---

## 🔍 El escenario
La rama `lesson/14-source` tiene 3 commits. **Solo uno** te interesa: el hotfix.
Miralos:
```bash
git log --oneline lesson/14-source
```
Vas a ver algo como:
```
xxxxxxx feat: cosa que NO querés todavía
yyyyyyy fix: corrige el bug crítico   ← este querés
zzzzzzz chore: otra cosa que NO querés
```

---

## 📋 La tarea

### Paso 1 — Identificá el hash del hotfix
```bash
git log --oneline lesson/14-source
```
Copiá el hash del commit **`fix: corrige el bug crítico`**.

### Paso 2 — Traelo a esta rama
Parado en `lesson/14-cherry-pick`:
```bash
git cherry-pick <HASH_DEL_FIX>
```

### Paso 3 — Verificá
```bash
git log --oneline -2
```
El `fix: corrige el bug crítico` ahora está **en tu rama**, arriba de todo, con
un **hash distinto** al original (compará con el de `lesson/14-source`).

Fijate que los otros dos commits de `lesson/14-source` **no** vinieron: trajiste
solo el que querías.

---

## ✅ ¿Lo lograste?
- `git log --oneline -2` muestra `fix: corrige el bug crítico` en tu rama.
- Su hash es **distinto** del original en `lesson/14-source`.
- No trajiste los otros dos commits.

---

## 🧠 Para pensar
- ¿Varios commits? `git cherry-pick A^..B` trae un rango.
- Si el cherry-pick choca, se resuelve igual que un conflicto de merge
  (lección 10) y después `git cherry-pick --continue`. Para cancelar:
  `git cherry-pick --abort`.
- Alternativa moderna a arrastrar cambios entre ramas sin cambiar de directorio:
  los **worktrees** (lección 15).

---

## 💡 Solución
```bash
git log --oneline lesson/14-source        # copiá el hash del "fix"
git cherry-pick <HASH_DEL_FIX>
git log --oneline -2
```

➡️ **Siguiente:** `git switch main` y seguí con `lesson/15-worktree`.
