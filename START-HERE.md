# 📖 Lección 13 — Solicitar cambios (code review en una PR)

**Nivel:** 🟡 Intermedio · **Tipo:** Estudio · **Tiempo:** ~12 min

---

## 🎯 Qué vas a aprender
Una PR no se mergea "porque sí": pasa por **review**. Revisar código es leer los
cambios de otra persona y responder con uno de **tres estados**:

| Estado | Qué significa | Efecto |
|--------|---------------|--------|
| 💬 **Comment** | Comentarios sueltos, sin veredicto | No aprueba ni bloquea |
| ✅ **Approve** | "Por mí, se mergea" | Habilita el merge |
| 🛑 **Request changes** | "Hay que arreglar esto antes" | **Bloquea** el merge hasta resolver |

El de esta lección es **Request changes**: cómo pedir cambios bien y cómo
responderlos del otro lado.

---

## 🔍 Estudio: anatomía de un review en GitHub

### Del lado del que revisa
1. En la PR → pestaña **"Files changed"**.
2. Pasá el mouse por una línea → aparece un **`+` azul** → clic para comentar
   **esa línea puntual**.
3. Podés proponer el cambio exacto con un bloque **"Suggestion"**:
   ````
   ```suggestion
   const puerto = 3000;
   ```
   ````
   El autor puede aplicarlo con un botón, sin copiar y pegar.
4. Cuando terminás, **"Review changes"** (arriba a la derecha) → elegís
   Comment / Approve / **Request changes** → **Submit review**.

### Del lado del autor (respondiendo el review)
1. Hacés los cambios pedidos **en la misma rama**, localmente.
2. `git add` + `git commit` + `git push` → la PR se **actualiza sola** (misma rama).
3. Respondés cada comentario y marcás **"Resolve conversation"**.
4. Pedís re-review (🔁 al lado del reviewer).

---

## 📋 La tarea (guiada — necesitás tu fork y una PR abierta)
> Si venís de la lección 12, ya tenés una PR abierta. Si no, abrí una primero.

1. **Simulá ser el reviewer**: en tu PR → *Files changed* → comentá una línea y
   dejá una **Suggestion**. Submit como **Request changes**.
2. **Simulá ser el autor**: aplicá la suggestion (o hacé el cambio a mano),
   commiteá y pusheá:
   ```bash
   git add .
   git commit -m "fix: aplica cambios pedidos en el review"
   git push
   ```
3. Mirá cómo la PR se actualizó con tu nuevo commit y el review quedó pendiente
   de re-aprobación. Marcá las conversaciones como **Resolved**.

---

## ✅ ¿Entendiste?
- Distinguís **Comment / Approve / Request changes** y cuál bloquea el merge.
- Sabés dejar una **Suggestion** y aplicarla.
- Sabés que pushear a la rama de la PR **la actualiza** — no hace falta PR nueva.

---

## 🧠 Para pensar
- **Request changes bloquea**; un comentario suelto no. Usá "Request changes"
  cuando de verdad no debe mergearse así, no para dudas menores.
- Buen review = específico y amable: señalá la línea, proponé la alternativa,
  explicá el porqué. "Esto está mal" no ayuda; "acá conviene X porque Y" sí.
- **Branch protection** puede exigir *N approvals* y *CI en verde* antes de
  habilitar el botón de merge.

➡️ **Siguiente:** `git switch main`. ¡Terminaste el intermedio! Sigue lo avanzado
con `lesson/14-cherry-pick`.
