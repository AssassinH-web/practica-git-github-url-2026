# ✏️ Lección 15 — `git worktree`: varias ramas a la vez

**Nivel:** 🔴 Avanzado · **Tipo:** Ejercicio · **Tiempo:** ~10 min

---

## 🎯 Qué vas a aprender
Normalmente tenés **una** rama checkeada por repo: para cambiar de rama hacés
`git switch`, que **reemplaza** los archivos de tu carpeta.

Un **worktree** te deja tener **otra rama checkeada en OTRA carpeta**, al mismo
tiempo, compartiendo el mismo `.git`:

```
practica-git-github/          ← rama actual (lesson/15-worktree)
practica-hotfix/              ← worktree: otra rama, otra carpeta, mismo repo
```

**Para qué sirve:** estás a mitad de algo en una rama y entra un hotfix urgente.
En vez de `stash` + `switch` + volver, abrís un worktree aparte, arreglás el
hotfix ahí, y tu trabajo original queda **intacto** en su carpeta.

---

## 🔍 Comandos clave
| Comando | Qué hace |
|---------|----------|
| `git worktree add <ruta> <rama>` | Checkea `<rama>` en la carpeta `<ruta>` |
| `git worktree add <ruta> -b <nueva>` | Crea una rama nueva y la checkea ahí |
| `git worktree list` | Lista todos los worktrees del repo |
| `git worktree remove <ruta>` | Elimina un worktree |

Regla: **una rama no puede estar checkeada en dos worktrees a la vez**. Git te
frena si lo intentás (te protege de pisar la misma rama desde dos lados).

---

## 📋 La tarea

### Paso 1 — Creá un worktree para otra rama
Desde la carpeta del repo (parado en `lesson/15-worktree`):
```bash
git worktree add ../practica-hotfix lesson/01-primer-commit
git worktree list
```
Ahora existe una carpeta hermana `../practica-hotfix` con la rama
`lesson/01-primer-commit` checkeada, **sin** haber tocado tu carpeta actual.

### Paso 2 — Trabajá en el worktree
```bash
cd ../practica-hotfix
git branch          # estás en lesson/01-primer-commit, en OTRA carpeta
ls                  # ves los archivos de ESA rama
cd -                # volvé a tu carpeta original (sigue en lesson/15-worktree)
```
👀 Tu carpeta original nunca cambió de rama. Dos ramas vivas al mismo tiempo.

### Paso 3 — Limpiá
```bash
git worktree remove ../practica-hotfix
git worktree list   # ya no aparece
```

---

## ✅ ¿Lo lograste?
- `git worktree list` mostró dos worktrees.
- Entraste a `../practica-hotfix` y viste otra rama checkeada sin afectar la carpeta original.
- Removiste el worktree con `git worktree remove`.

---

## 🧠 Para pensar
- worktree vs `stash`: stash guarda tu trabajo a medias y cambia de rama en la
  misma carpeta; worktree te deja **ambas cosas abiertas en paralelo**. Para
  builds largos o comparar dos ramas lado a lado, worktree gana.
- El `.git` es **compartido**: los commits que hagas en cualquier worktree están
  en el mismo repositorio. No son clones separados.
- No borres la carpeta de un worktree con `rm -rf`: usá `git worktree remove`
  (y `git worktree prune` si quedó colgado), así Git limpia sus referencias.

---

## 💡 Solución
```bash
git worktree add ../practica-hotfix lesson/01-primer-commit
git worktree list
git worktree remove ../practica-hotfix
```

➡️ **Siguiente:** `git switch main` y seguí con `lesson/16-git-blame`.
