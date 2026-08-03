# ✏️ Lección 10 — Resolver conflictos de merge

**Nivel:** 🟡 Intermedio · **Tipo:** Ejercicio · **Tiempo:** ~12–15 min

---

## 🎯 Qué vas a aprender

Un **conflicto de merge** aparece cuando dos ramas cambiaron la misma parte de un
archivo de formas diferentes.

Git no puede decidir automáticamente cuál versión debe quedarse, así que detiene
el merge y te pide que elijas.

> Un conflicto no significa que Git se dañó. Significa que necesita una decisión
> humana.

---

## 👀 Cómo se ve un conflicto

Git coloca marcadores temporales dentro del archivo:

```text
<<<<<<< HEAD
la versión de la rama donde estás parado
=======
la versión de la rama que estás trayendo
>>>>>>> lesson/10-feature
```

- `HEAD` representa tu rama actual.
- La parte de abajo representa la rama que estás integrando.
- Resolver significa borrar los marcadores y dejar solamente el contenido final.

---

## 🔍 El escenario

Estas dos ramas modificaron la misma línea de `config.txt`:

```text
lesson/10-conflictos → puerto=8080
lesson/10-feature    → puerto=3000
```

Al intentar unirlas, Git no sabe cuál valor debe conservar.

---

## 🔄 Preparar las ramas

Primero actualizá las referencias remotas:

```bash
git fetch origin
```

Revisá las ramas locales:

```bash
git branch
```

Si `lesson/10-feature` no aparece, revisá las ramas remotas:

```bash
git branch -r
```

Debería aparecer:

```text
origin/lesson/10-feature
```

Creá la rama local conectada con la remota:

```bash
git switch -c lesson/10-feature --track origin/lesson/10-feature
```

Después regresá a la rama que recibirá los cambios:

```bash
git switch lesson/10-conflictos
```

Comprobá la rama actual:

```bash
git branch --show-current
```

Debe mostrar:

```text
lesson/10-conflictos
```

> Si Git indica que `lesson/10-feature` ya existe, no la creés otra vez. Solo
> regresá con:
>
> ```bash
> git switch lesson/10-conflictos
> ```

---

## 🪟 Comandos según la terminal

Algunos comandos cambian según el sistema.

### Git Bash, Linux o macOS

```bash
cat config.txt
```

### Windows CMD

```bat
type config.txt
```

> En Windows CMD, `cat` no funciona. Usá `type`.

Tampoco usés comandos como:

```bash
git switch lesson/10-feature -- 2>/dev/null; git switch lesson/10-conflictos 2>/dev/null
```

Ese formato está pensado para una terminal tipo Bash y puede fallar en CMD.

Usá comandos separados:

```bash
git switch lesson/10-feature
git switch lesson/10-conflictos
```

---

## 📋 Paso 1 — Provocá el conflicto

Asegurate de estar en:

```text
lesson/10-conflictos
```

Luego ejecutá:

```bash
git merge lesson/10-feature
```

Git debería mostrar algo parecido a:

```text
Auto-merging config.txt
CONFLICT (content): Merge conflict in config.txt
Automatic merge failed; fix conflicts and then commit the result.
```

---

## ⚠️ Si aparece `Already up to date`

Si Git responde:

```text
Already up to date.
```

significa que, en el estado actual de tu repositorio, la rama ya contiene los
cambios de `lesson/10-feature` o el ejercicio ya fue realizado antes.

Primero revisá:

```bash
git status
git log --oneline --graph --all --decorate
```

Si querés repetir la práctica desde el estado original de la rama remota:

```bash
git merge --abort
```

El comando anterior solo funciona si hay un merge en progreso.

Después restaurá la rama de la lección:

```bash
git switch lesson/10-conflictos
git reset --hard origin/lesson/10-conflictos
```

Actualizá también la rama feature local:

```bash
git branch -f lesson/10-feature origin/lesson/10-feature
```

Y volvé a intentar:

```bash
git merge lesson/10-feature
```

> ⚠️ `git reset --hard` elimina cambios locales sin guardar. Usalo únicamente
> para reiniciar esta práctica.

---

## 📋 Paso 2 — Revisá el estado

Ejecutá:

```bash
git status
```

Debería aparecer:

```text
both modified: config.txt
```

Ahora mirá el archivo.

### Git Bash, Linux o macOS

```bash
cat config.txt
```

### Windows CMD

```bat
type config.txt
```

Verás algo parecido a:

```text
<<<<<<< HEAD
puerto=8080
=======
puerto=3000
>>>>>>> lesson/10-feature
```

---

## 📋 Paso 3 — Resolvé el conflicto

Abrí `config.txt` en VS Code, Antigravity o cualquier editor de texto.

Podés elegir:

- conservar `puerto=8080`;
- conservar `puerto=3000`;
- escribir otro valor;
- combinar ambas versiones si tuviera sentido.

Para esta práctica, dejá:

```text
puerto=3000
```

El archivo final no debe contener:

```text
<<<<<<<
=======
>>>>>>>
```

Guardá el archivo.

---

## 📋 Paso 4 — Marcá el conflicto como resuelto

Ejecutá:

```bash
git add config.txt
```

Esto le indica a Git que ya decidiste qué contenido debe quedarse.

Comprobá:

```bash
git status
```

Ahora Git debería indicar que todos los conflictos fueron resueltos, pero que el
merge todavía debe confirmarse.

---

## 📋 Paso 5 — Cerrá el merge

Ejecutá:

```bash
git commit --no-edit
```

`--no-edit` usa el mensaje de merge que Git preparó automáticamente.

Si tenés activada la firma automática y aparece un error de contraseña de la
clave privada, podés desactivarla temporalmente:

```bash
git config --global commit.gpgsign false
```

Luego repetí:

```bash
git commit --no-edit
```

---

## 📋 Paso 6 — Verificá el resultado

Revisá el historial:

```bash
git log --oneline --graph --all --decorate -6
```

Revisá el archivo final.

### Git Bash, Linux o macOS

```bash
cat config.txt
```

### Windows CMD

```bat
type config.txt
```

Debe aparecer solamente:

```text
puerto=3000
```

---

## 🧯 Cancelar un conflicto

Si querés abandonar el merge y regresar al estado anterior:

```bash
git merge --abort
```

Esto funciona mientras el merge todavía está en progreso.

Después podés volver a intentarlo:

```bash
git merge lesson/10-feature
```

---

## ⚡ Resolver tomando una versión completa

Si querés quedarte con toda la versión de tu rama actual:

```bash
git checkout --ours config.txt
git add config.txt
git commit --no-edit
```

Si querés quedarte con toda la versión de la rama que estás trayendo:

```bash
git checkout --theirs config.txt
git add config.txt
git commit --no-edit
```

- `--ours`: conserva la versión de `lesson/10-conflictos`.
- `--theirs`: conserva la versión de `lesson/10-feature`.

---

## 🖥️ Resolver con GitHub Desktop o VS Code

También podés iniciar el merge desde GitHub Desktop:

```text
Branch → Merge into current branch
```

Seleccioná:

```text
lesson/10-feature
```

Cuando aparezca el conflicto, abrí `config.txt` en VS Code o Antigravity.

En VS Code pueden aparecer opciones como:

```text
Accept Current Change
Accept Incoming Change
Accept Both Changes
```

Para esta práctica:

```text
Accept Incoming Change
```

dejará:

```text
puerto=3000
```

Después guardá, regresá a GitHub Desktop y completá el commit de merge.

---

## ✅ ¿Lo lograste?

- Preparaste localmente la rama `lesson/10-feature`.
- Provocaste el conflicto.
- Confirmaste `both modified` con `git status`.
- Revisaste el archivo con `cat` o `type`, según tu terminal.
- Eliminaste los marcadores.
- Marcaste el archivo como resuelto con `git add`.
- Cerraste el merge con `git commit --no-edit`.
- Verificaste el contenido final.

---

## 🧠 Para pensar

- Git puede detectar el conflicto, pero no puede decidir cuál versión es la
  correcta.
- Resolver un conflicto significa tomar una decisión sobre el contenido final.
- Los conflictos son normales cuando varias personas trabajan sobre las mismas
  líneas.
- `git merge --abort` permite cancelar el proceso sin romper el repositorio.

---

## 💡 Solución completa

```bash
git fetch origin

git branch
git branch -r

# Ejecutar solo si lesson/10-feature no existe localmente:
git switch -c lesson/10-feature --track origin/lesson/10-feature

git switch lesson/10-conflictos
git branch --show-current

git merge lesson/10-feature
git status
```

Abrí `config.txt`, eliminá los marcadores y dejá:

```text
puerto=3000
```

Después:

```bash
git add config.txt
git commit --no-edit
git log --oneline --graph --all --decorate -6
```

Para ver el archivo:

### Git Bash, Linux o macOS

```bash
cat config.txt
```

### Windows CMD

```bat
type config.txt
```

➡️ **Siguiente:** `git switch main` y continuá con
`lesson/11-squash-vs-merge`.
