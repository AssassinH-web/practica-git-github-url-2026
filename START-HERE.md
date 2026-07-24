# 📖 Lección 12 — Cómo funciona GitHub (fork, remote, push, PR)

**Nivel:** 🟡 Intermedio · **Tipo:** Estudio + práctica en tu fork · **Tiempo:** ~15 min

---

## 🎯 Qué vas a aprender
Git vive en **tu máquina**. GitHub es un **servidor** que hospeda copias de tu
repo para compartirlas. Las piezas:

```
   upstream (repo original)
        │  fork
        ▼
   origin (TU fork en GitHub)  ◀──push/pull──▶  tu repo local (tu compu)
```

| Concepto | Qué es |
|----------|--------|
| **remote** | Un repo "de allá" al que tu repo local apunta (una URL con nombre) |
| **origin** | Por convención, tu fork en GitHub (de donde clonaste) |
| **upstream** | Por convención, el repo original del que hiciste fork |
| **fork** | Tu copia personal de otro repo, en tu cuenta de GitHub |
| **push** | Subir tus commits locales a un remote |
| **pull** | Bajar commits del remote a tu local (`fetch` + `merge`) |
| **PR (Pull Request)** | Pedido de "traigan mis cambios a su rama" — con review |

---

## 🔍 Estudio: mirá tus remotes
Ya hiciste fork y clonaste este repo, así que ya tenés un `origin`:
```bash
git remote -v
```
Vas a ver algo como:
```
origin  https://github.com/TU_USUARIO/practica-git-github.git (fetch)
origin  https://github.com/TU_USUARIO/practica-git-github.git (push)
```

### Agregá el `upstream` (el repo original)
Así podés traer actualizaciones del repo del que hiciste fork:
```bash
git remote add upstream https://github.com/USUARIO_ORIGINAL/practica-git-github.git
git remote -v          # ahora ves origin Y upstream
```

---

## 📋 La tarea — el ciclo completo push + PR

### Paso 1 — Creá una rama y un commit
```bash
git switch -c mi-aporte
echo "- Daniel estuvo acá" >> saludos.txt
git add saludos.txt
git commit -m "docs: agrega mi saludo"
```

### Paso 2 — Pusheá la rama a TU fork (origin)
```bash
git push -u origin mi-aporte
```
`-u` (o `--set-upstream`) ata tu rama local a la remota: después alcanza con
`git push` a secas. En la salida, GitHub te da un **link para abrir la PR**.

### Paso 3 — Abrí la Pull Request
Andá a tu fork en GitHub. Va a aparecer un banner **"Compare & pull request"**.
- **base**: la rama de destino (a dónde querés que entren los cambios).
- **compare**: `mi-aporte` (tu rama con los cambios).
- Poné título y descripción → **Create pull request**.

### Paso 4 — Mantené tu fork al día (sincronizar con upstream)
```bash
git fetch upstream
git switch main
git merge upstream/main      # o: git rebase upstream/main
git push origin main
```

---

## ✅ ¿Entendiste?
- Distinguís `origin` (tu fork) de `upstream` (el original).
- Pusheaste una rama a tu fork y abriste una PR.
- Sabés cómo bajar cambios del upstream a tu fork.

---

## 🧠 Para pensar
- Una PR **no** es de Git: es una función de GitHub montada arriba de un simple
  "esta rama quiere entrar en aquella". Por eso vive en el servidor, no en tu `.git`.
- `git fetch` **no** toca tus archivos: solo baja info del remote. `git pull` sí
  los actualiza (fetch + merge). Cuando dudes, `fetch` primero y mirá con `log`.

➡️ **Siguiente:** `git switch main` y seguí con `lesson/13-solicitar-cambios`.
