# ✏️ Lección 08 — Crear ramas y moverse entre ellas

**Nivel:** 🟡 Intermedio · **Tipo:** Ejercicio · **Tiempo:** ~8 min

---

## 🎯 Qué vas a aprender
Una **rama** es solo un puntero móvil a un commit. Crear una rama no copia
archivos ni ocupa espacio: es una etiqueta que se mueve sola cuando commiteás.

```
          ┌─ feature (vos acá, avanza al commitear)
A ── B ── C
          └─ main (se queda en C hasta que la muevas)
```

`HEAD` es "dónde estás parado". Cuando hacés `switch`, movés `HEAD` a otra rama y
Git actualiza tus archivos para reflejar ese commit.

### Comandos clave
| Comando | Qué hace |
|---------|----------|
| `git branch` | Lista las ramas (la actual con `*`) |
| `git switch -c nombre` | Crea una rama y salta a ella |
| `git switch nombre` | Salta a una rama existente |
| `git switch -` | Vuelve a la rama anterior |
| `git branch -d nombre` | Borra una rama (ya mergeada) |

> `git checkout -b nombre` hace lo mismo que `switch -c`. `switch` es más nuevo y
> menos ambiguo — usalo.

---

## 📋 La tarea

### Paso 1 — Mirá dónde estás
```bash
git branch          # deberías ver un * en lesson/08-crear-ramas
git status
```

### Paso 2 — Creá una rama nueva y saltá a ella
```bash
git switch -c mi-experimento
git branch          # ahora el * está en mi-experimento
```

### Paso 3 — Hacé un commit en la rama nueva
```bash
echo "experimento" > experimento.txt
git add experimento.txt
git commit -m "chore: prueba en rama experimento"
```

### Paso 4 — Volvé y comprobá que el archivo desaparece
```bash
git switch lesson/08-crear-ramas
ls                  # experimento.txt NO está: vive solo en la otra rama
git switch -        # volvé a mi-experimento con el guion
ls                  # ahí sí está
```

### Paso 5 — Volvé y borrá la rama
```bash
git switch lesson/08-crear-ramas
git branch -D mi-experimento   # -D fuerza el borrado aunque no esté mergeada
```

---

## ✅ ¿Lo lograste?
- Creaste `mi-experimento`, commiteaste ahí, y viste que `experimento.txt` solo
  existe en esa rama.
- Usaste `git switch -` para saltar entre las dos.
- Borraste la rama.

---

## 🧠 Para pensar
- Cambiar de rama **cambia tus archivos**. Si tenés cambios sin commitear que
  chocan, Git te frena. Ahí entran `git stash` o commitear antes.
- Una rama borrada no destruye sus commits al instante: `git reflog` los recuerda
  un tiempo. Igual, no borres ramas con trabajo no mergeado a la ligera.

---

## 💡 Solución
```bash
git switch -c mi-experimento
echo "experimento" > experimento.txt
git add experimento.txt && git commit -m "chore: prueba en rama experimento"
git switch lesson/08-crear-ramas
git branch -D mi-experimento
```

➡️ **Siguiente:** `git switch main` y seguí con `lesson/09-mergear-ramas`.
