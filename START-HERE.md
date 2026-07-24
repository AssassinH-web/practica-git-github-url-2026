# 📖 Lección 05 — Commits verificados vs no verificados

**Nivel:** 🟢 Básico · **Tipo:** Estudio + Setup · **Tiempo:** ~10 min

---

## 🎯 Qué vas a aprender
El campo "autor" de un commit es **texto libre**: cualquiera puede poner tu
nombre y tu email. No prueba nada.

```bash
git -c user.name="Linus Torvalds" -c user.email="torvalds@linux.com" commit ...
```
☝️ Eso crea un commit "de Linus" sin que él exista en la ecuación. Da miedo, ¿no?

Un **commit firmado** resuelve esto: se firma criptográficamente con una clave
(GPG o SSH) que solo vos tenés. GitHub muestra un badge **`Verified`** ✔️ cuando
la firma coincide con una clave que registraste en tu cuenta.

| Estado en GitHub | Significa |
|------------------|-----------|
| **Verified** ✔️ | Firmado con una clave registrada por el autor |
| **Unverified** ⚠️ | Firmado, pero la clave no está registrada / no coincide |
| *(sin badge)* | No está firmado — el autor es solo texto |

---

## 🔍 Estudio: inspeccionar firmas
Para ver si un commit está firmado:
```bash
git log --show-signature -1
```
- **Sin firma:** solo ves autor, fecha y mensaje.
- **Con firma válida:** aparece algo como
  ```
  gpg: Good signature from "Daniel <daniel@...>"
  ```
  o, con SSH:
  ```
  Good "git" signature for daniel@... with ED25519 key SHA256:...
  ```

Verificá un commit puntual:
```bash
git verify-commit HEAD    # falla si no está firmado o la firma es inválida
```

---

## 🛠️ Setup: firmá tus propios commits (SSH — la vía más simple)

> Recomendado: firmar con SSH reutiliza la clave que ya usás para push.

### 1. ¿Tenés una clave SSH? Si no, creala:
```bash
ls ~/.ssh/id_ed25519.pub || ssh-keygen -t ed25519 -C "tu-email@ejemplo.com"
```

### 2. Configurá Git para firmar con SSH:
```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true   # firma TODOS los commits
```

### 3. Registrá la clave en GitHub **como Signing Key**:
GitHub → *Settings → SSH and GPG keys → New SSH key* →
**Key type: `Signing Key`** (¡no `Authentication`!) → pegá el contenido de
`~/.ssh/id_ed25519.pub`.

### 4. Probá:
```bash
git commit --allow-empty -m "chore: primer commit firmado"
git log --show-signature -1
```
Cuando pushees este commit a tu fork, debería salir **Verified** ✔️ en GitHub.

---

## ✅ ¿Entendiste?
- Sabés por qué el autor de un commit **no** prueba identidad.
- Sabés distinguir Verified / Unverified / sin firma.
- Configuraste firma SSH y viste tu firma con `git log --show-signature`.

---

## 🧠 Para pensar
- **Verified** no dice que el código sea bueno; dice que **quién dice ser el
  autor, lo es**. Es integridad de autoría, no calidad.
- Podés exigir firma en `main` con *branch protection → Require signed commits*.

➡️ **Siguiente:** `git switch main` y seguí con `lesson/06-lineal-vs-merge`.
