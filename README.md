# 🎓 Práctica Git & GitHub — de cero a avanzado

Un repositorio **interactivo** para aprender Git haciéndolo, no leyéndolo.
Hacés un **fork**, y cada rama es una lección con su consigna, sus comandos y su solución.

---

## 🚀 Cómo se usa

1. **Fork** de este repo a tu cuenta de GitHub.
2. Clonalo:
   ```bash
   git clone https://github.com/TU_USUARIO/practica-git-github.git
   cd practica-git-github
   ```
3. Empezás siempre en `main` (este índice). Para cada lección, te movés a su rama:
   ```bash
   git switch lesson/01-primer-commit
   ```
4. Abrís el archivo **`START-HERE.md`** de esa rama. Ahí está todo: qué vas a
   aprender, la tarea, los comandos y cómo verificar que lo hiciste bien.
5. Cuando termines, volvés a `main` y pasás a la siguiente.

> 💡 Cada lección es autocontenida. Si te trabás, cada ejercicio tiene su
> solución en un tag `solution/<lección>` que podés comparar con tu resultado.

---

## 🧭 Los dos tipos de lección

| Icono | Tipo | Qué hacés |
|-------|------|-----------|
| ✏️ | **Ejercicio** | La rama está en un estado *"antes"*. Vos ejecutás los comandos y llegás al *"después"*. |
| 📖 | **Estudio** | El historial ya está construido. Vos lo inspeccionás (log, blame, firmas) para entender qué pasó. |

---

## 📚 Currículum

### 🟢 Nivel básico — el commit
| # | Lección | Tipo | Concepto |
|---|---------|------|----------|
| 01 | `lesson/01-primer-commit` | ✏️ | `add` + `commit`: tu primer commit |
| 02 | `lesson/02-amend` | ✏️ | `commit --amend`: corregir el último commit |
| 03 | `lesson/03-referencias` | ✏️ | Referenciar issues y links en el mensaje (`Closes #12`) |
| 04 | `lesson/04-conventional-commits` | ✏️ | Convención `feat:`, `fix:`, `chore:`… |
| 05 | `lesson/05-commits-verificados` | 📖 | Firmados (✔ Verified) vs no verificados |

### 🟢 Nivel básico — el historial
| # | Lección | Tipo | Concepto |
|---|---------|------|----------|
| 06 | `lesson/06-lineal-vs-merge` | 📖 | Historial lineal vs con merges |
| 07 | `lesson/07-rebase-vs-merge` | ✏️ | Qué cambia entre `rebase` y `merge` |

### 🟡 Nivel intermedio — ramas y colaboración
| # | Lección | Tipo | Concepto |
|---|---------|------|----------|
| 08 | `lesson/08-crear-ramas` | ✏️ | Crear y moverse entre ramas |
| 09 | `lesson/09-mergear-ramas` | ✏️ | Integrar una rama en otra |
| 10 | `lesson/10-conflictos` | ✏️ | Resolver conflictos de merge |
| 11 | `lesson/11-squash-vs-merge` | 📖 | Squash merge vs merge commit |
| 12 | `lesson/12-como-funciona-github` | 📖 | Fork, remote, push, Pull Request |
| 13 | `lesson/13-solicitar-cambios` | 📖 | Code review: pedir cambios en una PR |

### 🔴 Nivel avanzado
| # | Lección | Tipo | Concepto |
|---|---------|------|----------|
| 14 | `lesson/14-cherry-pick` | ✏️ | Traer un commit puntual de otra rama |
| 15 | `lesson/15-worktree` | ✏️ | Varias ramas checkeadas a la vez |
| 16 | `lesson/16-git-blame` | 📖 | Quién cambió cada línea y por qué |

---

## ✅ Requisitos previos
- Git instalado (`git --version`).
- Una cuenta de GitHub.
- Una terminal. (Opcional: un editor como VS Code.)

---

*Empezá por [`lesson/01-primer-commit`](../../tree/lesson/01-primer-commit). ¡Suerte!*
