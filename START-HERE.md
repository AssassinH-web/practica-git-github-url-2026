# ✏️ Lección 09 — Mergear ramas (fast-forward vs merge commit)

**Nivel:** 🟡 Intermedio · **Tipo:** Ejercicio · **Tiempo:** ~10–15 min

---

## 🎯 Qué vas a aprender

El comando:

```bash
git merge otra-rama
```

trae los cambios de `otra-rama` hacia la rama donde estás parado.

> La rama actual recibe los cambios.

Ejemplo:

```bash
git switch main
git merge feature
```

Aquí `main` recibe los cambios de `feature`.

Un merge puede terminar principalmente de dos formas:

### Fast-forward (FF)

Ocurre cuando la rama actual no avanzó desde que se creó la otra rama.

Antes:

```text
A ── B          lesson/09-mergear-ramas
     \
      C ── D    lesson/09-feature
```

Después:

```text
A ── B ── C ── D
               ↑
     ambas ramas apuntan aquí
```

Git no crea un commit nuevo. Solamente mueve el puntero de la rama hacia
adelante.

### Merge commit (`--no-ff`)

Se crea un commit especial que registra explícitamente la integración de las dos
ramas.

```text
A ── B ───────── M
     \          /
      C ── D ──
```

`M` tiene dos padres porque une dos líneas de trabajo.

---

## 🔍 El escenario

La rama:

```text
lesson/09-mergear-ramas
```

tiene una rama compañera:

```text
lesson/09-feature
```

La rama `lesson/09-feature` agregó nuevos commits, mientras que
`lesson/09-mergear-ramas` no avanzó.

Por eso, un merge normal debería terminar en **fast-forward**.

---

## 🔄 Preparar la rama compañera

Antes de hacer el merge, actualizá las referencias remotas:

```bash
git fetch origin
```

Revisá las ramas locales:

```bash
git branch
```

Si `lesson/09-feature` no aparece, revisá las ramas remotas:

```bash
git branch -r
```

Debería aparecer una referencia similar a:

```text
origin/lesson/09-feature
```

En ese caso, creá una rama local conectada con la remota:

```bash
git switch -c lesson/09-feature --track origin/lesson/09-feature
```

Después regresá a la rama que recibirá los cambios:

```bash
git switch lesson/09-mergear-ramas
```

Comprobá la rama actual:

```bash
git branch --show-current
```

El resultado debe ser:

```text
lesson/09-mergear-ramas
```

> Si aparece `merge: lesson/09-feature - not something we can merge`, normalmente
> significa que `lesson/09-feature` todavía no existe como rama local.

> Si Git indica que la rama `lesson/09-feature` ya existe, no volvas a crearla.
> Solo ejecutá:
>
> ```bash
> git switch lesson/09-mergear-ramas
> ```

---

## 👀 Revisar el historial antes del merge

Ejecutá:

```bash
git log --oneline --graph --all --decorate
```

- `--oneline`: muestra cada commit en una sola línea.
- `--graph`: dibuja las ramas.
- `--all`: incluye todas las ramas.
- `--decorate`: muestra los nombres de las ramas.

---

## 📋 Parte A — Merge fast-forward

Asegurate de estar en:

```text
lesson/09-mergear-ramas
```

Luego ejecutá:

```bash
git merge lesson/09-feature
```

Git debería mostrar un mensaje parecido a:

```text
Fast-forward
```

Revisá el historial:

```bash
git log --oneline --graph --all --decorate
```

No debería existir un commit nuevo de merge. La rama
`lesson/09-mergear-ramas` simplemente avanzó hasta el último commit de
`lesson/09-feature`.

### Idea clave

> Fast-forward integra los cambios moviendo el puntero de la rama. No crea un
> commit adicional.

---

## ↩️ Deshacer el fast-forward

Para repetir el ejercicio de otra forma:

```bash
git reset --hard ORIG_HEAD
```

`ORIG_HEAD` guarda la posición donde estaba la rama antes del merge.

Comprobá el historial:

```bash
git log --oneline --graph --all --decorate
```

> ⚠️ `git reset --hard` puede eliminar cambios locales sin guardar. En esta
> práctica debe usarse únicamente cuando `git status` indique que no hay cambios
> pendientes.

Podés comprobarlo antes con:

```bash
git status
```

---

## 📋 Parte B — Forzar un merge commit

Ejecutá:

```bash
git merge --no-ff lesson/09-feature -m "merge: integra feature (no-ff)"
```

- `--no-ff`: impide el fast-forward y obliga a crear un merge commit.
- `-m`: establece el mensaje del nuevo commit.

Revisá el historial:

```bash
git log --oneline --graph --all --decorate
```

Ahora debería aparecer una unión parecida a:

```text
*   merge: integra feature (no-ff)
|\
| * commit de la feature
| * commit de la feature
|/
* commit anterior
```

### Idea clave

> `--no-ff` deja visible en el historial el punto exacto donde se integró la
> rama.

---

## 👨‍👩‍👦 Confirmar los dos padres

Ejecutá:

```bash
git log --merges -1 --pretty="%h padres:%p"
```

El resultado será similar a:

```text
a1b2c3 padres:d4e5f6 g7h8i9
```

Un commit normal tiene un padre. Un merge commit tiene dos porque une dos líneas
de desarrollo.

---

## 🖥️ ¿Se puede hacer con GitHub Desktop?

Sí. Primero seleccioná como rama actual:

```text
lesson/09-mergear-ramas
```

Después entrá a:

```text
Branch → Merge into current branch
```

Elegí:

```text
lesson/09-feature
```

GitHub Desktop puede realizar el merge normal. Si la historia permite un
fast-forward, Git lo hará automáticamente.

Para forzar específicamente `--no-ff`, utilizá la terminal:

```bash
git merge --no-ff lesson/09-feature -m "merge: integra feature (no-ff)"
```

---

## ⚠️ Si los commits están configurados para firmarse

Si anteriormente activaste:

```bash
git config --global commit.gpgsign true
```

Git intentará firmar también el nuevo merge commit.

Si aparece un error como:

```text
incorrect passphrase supplied to decrypt private key
fatal: failed to write commit object
```

significa que Git no pudo desbloquear la clave privada. No es un problema del
merge.

Para continuar sin firmar automáticamente:

```bash
git config --global commit.gpgsign false
```

Para crear intencionalmente un merge commit firmado:

```bash
git merge --no-ff -S lesson/09-feature -m "merge: integra feature firmado"
```

Los commits firmados y no firmados pueden convivir dentro del mismo historial.

---

## ✅ ¿Lo lograste?

- Preparaste localmente la rama `lesson/09-feature`.
- Hiciste un merge fast-forward.
- Confirmaste que no se creó un merge commit.
- Deshiciste el merge con `git reset --hard ORIG_HEAD`.
- Forzaste un merge commit con `--no-ff`.
- Confirmaste que el merge commit tiene dos padres.

---

## 🧠 Para pensar

¿Por qué algunos equipos utilizan siempre `--no-ff`?

Porque el merge commit agrupa visualmente todo el trabajo de una feature y deja
registrado el punto donde fue integrada.

Fast-forward deja un historial más lineal. `--no-ff` conserva más información
visual sobre las ramas.

---

## 💡 Solución completa

```bash
git fetch origin

git branch
git branch -r

# Ejecutar solamente si lesson/09-feature no existe localmente:
git switch -c lesson/09-feature --track origin/lesson/09-feature

git switch lesson/09-mergear-ramas
git branch --show-current

git log --oneline --graph --all --decorate

git merge lesson/09-feature
git log --oneline --graph --all --decorate

git status
git reset --hard ORIG_HEAD

git merge --no-ff lesson/09-feature -m "merge: integra feature (no-ff)"
git log --oneline --graph --all --decorate

git log --merges -1 --pretty="%h padres:%p"
```

➡️ **Siguiente:** `git switch main` y continuá con
`lesson/10-conflictos`.
