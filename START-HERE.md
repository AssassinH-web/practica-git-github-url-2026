# 📖 Lección 05 — Commits verificados vs no verificados

**Nivel:** 🟢 Básico · **Tipo:** Estudio + Setup · **Tiempo:** ~10–15 min

---

## 🎯 Qué vas a aprender

El campo **autor** de un commit es texto configurable: cualquier persona puede
poner otro nombre y otro correo.

```bash
git -c user.name="Linus Torvalds" \
    -c user.email="torvalds@linux.com" \
    commit --allow-empty -m "commit de ejemplo"
```

☝️ Ese commit puede mostrar a “Linus Torvalds” como autor aunque él no lo haya
creado. Por eso, el nombre y el correo por sí solos **no prueban identidad**.

Un **commit firmado** agrega una firma criptográfica creada con una clave privada.
GitHub muestra **Verified** ✔️ cuando la firma coincide con una clave pública
registrada en la cuenta del autor.

| Estado en GitHub | Significa |
|---|---|
| **Verified** ✔️ | GitHub comprobó la firma con una clave registrada |
| **Unverified** ⚠️ | Hay firma, pero GitHub no pudo validarla |
| *(sin badge)* | El commit no está firmado |

> **Verified confirma autoría e integridad, no calidad del código.**

---

## 🔍 Estudio: inspeccionar firmas

Para revisar el último commit:

```bash
git log --show-signature -1
```

- **Sin firma:** solo aparecen autor, fecha y mensaje.
- **Con firma SSH válida:** aparece algo parecido a:

```text
Good "git" signature for usuario@ejemplo.com with ED25519 key SHA256:...
```

También podés verificar el commit actual:

```bash
git verify-commit HEAD
```

---

## 🛠️ Setup: firmá tus propios commits con SSH

### 1. Revisá si ya tenés una clave SSH

#### Git Bash, Linux o macOS

```bash
ls ~/.ssh/id_ed25519.pub
```

#### Windows CMD

```bat
dir "%USERPROFILE%\.ssh"
```

Si no existe `id_ed25519.pub`, creala:

```bash
ssh-keygen -t ed25519 -C "tu-email@ejemplo.com"
```

> Nunca compartás el archivo privado `id_ed25519`.  
> El archivo que se registra en GitHub es `id_ed25519.pub`.

---

### 2. Configurá Git para firmar con SSH

#### Git Bash, Linux o macOS

```bash
git config --global gpg.format ssh
git config --global user.signingkey ~/.ssh/id_ed25519.pub
git config --global commit.gpgsign true
```

#### Windows CMD

```bat
git config --global gpg.format ssh
git config --global user.signingkey "%USERPROFILE%\.ssh\id_ed25519.pub"
git config --global commit.gpgsign true
```

`commit.gpgsign true` hace que los nuevos commits se firmen automáticamente.

---

### 3. Configurá la verificación local

Este paso evita el error:

```text
gpg.ssh.allowedSignersFile needs to be configured
```

#### Windows CMD

Este comando toma automáticamente el correo configurado en Git y crea el archivo
`allowed_signers`:

```bat
for /f "delims=" %E in ('git config --global user.email') do for /f "delims=" %K in ('type "%USERPROFILE%\.ssh\id_ed25519.pub"') do @echo %E %K>"%USERPROFILE%\.ssh\allowed_signers"
```

Después indicá a Git dónde está el archivo:

```bat
git config --global gpg.ssh.allowedSignersFile "%USERPROFILE%\.ssh\allowed_signers"
```

> Si tu clave pública tiene otro nombre, reemplazá `id_ed25519.pub` por el nombre
> correcto.

#### Git Bash, Linux o macOS

```bash
echo "$(git config --global user.email) $(cat ~/.ssh/id_ed25519.pub)" \
  > ~/.ssh/allowed_signers

git config --global gpg.ssh.allowedSignersFile ~/.ssh/allowed_signers
```

---

### 4. Registrá la clave en GitHub como Signing Key

Copiá el contenido de la clave pública.

#### Git Bash, Linux o macOS

```bash
cat ~/.ssh/id_ed25519.pub
```

#### Windows CMD

```bat
type "%USERPROFILE%\.ssh\id_ed25519.pub" | clip
```

Luego entrá a:

**GitHub → Settings → SSH and GPG keys → New SSH key**

Configurá:

```text
Title: Firma de commits - mi computadora
Key type: Signing Key
Key: pegar el contenido de id_ed25519.pub
```

---

### 5. Creá un commit firmado

```bash
git commit --allow-empty -m "chore: primer commit firmado"
```

Como la firma automática está activada, el commit quedará firmado.

Comprobalo:

```bash
git log --show-signature -1
git verify-commit HEAD
```

Subilo a tu fork:

```bash
git push
```

En GitHub debería aparecer **Verified** ✔️.

---

## 🧪 Comparar un commit firmado y uno no firmado

Commit firmado:

```bash
git commit --allow-empty -m "chore: commit firmado"
```

Commit no firmado:

```bash
git -c commit.gpgsign=false commit --allow-empty -m "chore: commit no firmado"
```

Después:

```bash
git push
```

En GitHub podrás comparar:

```text
commit firmado       → Verified
commit no firmado    → sin badge
```

---

## ✅ ¿Entendiste?

- Sabés por qué el nombre del autor no prueba identidad.
- Sabés distinguir `Verified`, `Unverified` y un commit sin firma.
- Configuraste Git para firmar commits con SSH.
- Configuraste `allowed_signers` para verificar localmente.
- Creaste y comparaste un commit firmado y uno no firmado.

---

## 🧠 Para pensar

- **Verified** no significa que el código sea bueno o seguro.
- Significa que la firma corresponde a una clave registrada y que el commit no
  cambió después de ser firmado.
- En ramas importantes se puede exigir firma con reglas de protección.

➡️ **Siguiente:** `git switch main` y seguí con `lesson/06-lineal-vs-merge`.
