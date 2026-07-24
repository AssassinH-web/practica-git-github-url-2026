# ✏️ Lección 10 — Resolver conflictos de merge

**Nivel:** 🟡 Intermedio · **Tipo:** Ejercicio · **Tiempo:** ~12 min

---

## 🎯 Qué vas a aprender
Un **conflicto** aparece cuando dos ramas cambiaron **la misma línea** del mismo
archivo de formas distintas. Git no adivina cuál gana: **te lo pasa a vos**.

No es un error ni algo que hiciste mal: es Git pidiéndote una decisión.

### Cómo se ve un conflicto
Git mete **marcadores** en el archivo:
```
<<<<<<< HEAD
la versión de TU rama (donde estás parado)
=======
la versión de la rama que estás trayendo
>>>>>>> lesson/10-feature
```
- Arriba (`HEAD`) → lo que ya tenías.
- Abajo → lo que trae la otra rama.
- Resolver = **borrar los marcadores** y dejar el contenido final que quieras
  (una, la otra, o una mezcla).

---

## 🔍 El escenario
Esta rama y `lesson/10-feature` cambiaron **la misma línea** de `config.txt`:
- Esta rama la puso en `puerto=8080`.
- La feature la puso en `puerto=3000`.

Al mergear, va a chocar. Miralo:
```bash
git switch lesson/10-feature -- 2>/dev/null; git switch lesson/10-conflictos 2>/dev/null
cat config.txt
```

---

## 📋 La tarea

### Paso 1 — Provocá el conflicto (a propósito)
Parado en `lesson/10-conflictos`:
```bash
git merge lesson/10-feature
```
Git te va a decir:
```
CONFLICT (content): Merge conflict in config.txt
Automatic merge failed; fix conflicts and then commit the result.
```

### Paso 2 — Mirá el estado y el archivo
```bash
git status              # config.txt aparece como "both modified"
cat config.txt          # vas a ver los <<<<<<< ======= >>>>>>>
```

### Paso 3 — Resolvé
Editá `config.txt` a mano. Borrá los marcadores y dejá **la línea final que
quieras**. Por ejemplo, quedate con el puerto 3000:
```
puerto=3000
```
(No debe quedar ningún `<<<<`, `====` ni `>>>>` en el archivo.)

### Paso 4 — Marcá como resuelto y cerrá el merge
```bash
git add config.txt
git commit --no-edit        # usa el mensaje de merge que Git preparó
```

### Paso 5 — Verificá
```bash
git log --oneline --graph -3
cat config.txt              # solo tu línea final, sin marcadores
```

---

## ✅ ¿Lo lograste?
- Provocaste el conflicto y lo viste con `git status` (`both modified`).
- Editaste `config.txt` dejando una sola versión, sin marcadores.
- `git add` + `git commit` cerraron el merge.

---

## 🧠 Para pensar
- Si te asustás en medio de un conflicto: `git merge --abort` te devuelve todo
  como estaba antes de empezar. Nada se rompe.
- `git checkout --ours config.txt` / `--theirs config.txt` resuelven tomando
  **toda** una versión sin editar a mano. Útil cuando una gana entera.
- Herramientas visuales: `git mergetool`, o el panel de conflictos de VS Code.

---

## 💡 Solución
```bash
git merge lesson/10-feature
# editá config.txt: borrá marcadores, dejá "puerto=3000"
git add config.txt
git commit --no-edit
```

➡️ **Siguiente:** `git switch main` y seguí con `lesson/11-squash-vs-merge`.
