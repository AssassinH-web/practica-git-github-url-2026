# 📖 Lección 16 — `git blame`: quién cambió cada línea

**Nivel:** 🔴 Avanzado · **Tipo:** Estudio · **Tiempo:** ~10 min

---

## 🎯 Qué vas a aprender
`git blame <archivo>` te dice, **para cada línea**, cuál fue el último commit que
la tocó, quién y cuándo. No es para "echar culpas": es para **entender el porqué**
de una línea rara antes de tocarla.

```
a1b2c3d (Ana   2024-01-10) def procesar(datos):
e4f5g6h (Beto  2024-03-22)     # validación agregada tras el bug #42
a1b2c3d (Ana   2024-01-10)     return limpiar(datos)
```
Cada línea trae: **hash · autor · fecha · contenido**. Con el hash saltás al
commit completo y leés *por qué* se hizo ese cambio.

---

## 🔍 El escenario
El archivo `procesar.py` de esta rama fue construido en **varios commits**
distintos, a propósito. Cada línea tiene su propia historia.

---

## 📋 La tarea (inspección)

### Paso 1 — Blame básico
```bash
git blame procesar.py
```
Fijate que **líneas distintas tienen commits (hashes) distintos**: no se
escribió todo de una.

### Paso 2 — De la línea al porqué
Elegí el hash de una línea que te llame la atención y miralo entero:
```bash
git show <HASH>
```
Ahí ves el commit completo: mensaje, qué otras líneas cambió, cuándo.

### Paso 3 — Blame enfocado a un rango de líneas
```bash
git blame -L 2,4 procesar.py
```
`-L 2,4` limita el blame a las líneas 2 a 4. Útil en archivos grandes.

### Paso 4 — Ignorar cambios de formato
A veces una línea "la tocó por última vez" un commit que solo la re-indentó.
Para saltar esos cambios cosméticos y ver el cambio *real*:
```bash
git blame -w procesar.py     # -w ignora cambios de espacios en blanco
```

---

## ✅ ¿Entendiste?
- `git blame procesar.py` muestra hash/autor/fecha por línea.
- Saltaste de una línea a su commit con `git show <hash>`.
- Sabés acotar con `-L` e ignorar formato con `-w`.

---

## 🧠 Para pensar
- **En GitHub** es aún más cómodo: abrí el archivo → botón **"Blame"**. Cada
  bloque enlaza a su commit y su PR. Además hay un botón **"View blame prior to
  this change"** para seguir la historia hacia atrás línea por línea.
- Comando primo: `git log -L '/def procesar/',+5:procesar.py` te muestra la
  **evolución** de ese rango de líneas a lo largo del tiempo (no solo el último
  que las tocó).
- `git blame` responde *quién y cuándo*; el **mensaje del commit** responde
  *por qué*. Por eso las lecciones 03 y 04 (buenos mensajes) importan tanto:
  un blame es tan útil como buenos sean los commits que encuentra.

➡️ **¡Terminaste las 16 lecciones!** 🎉 Volvé a `main` (`git switch main`) para
ver el índice completo. Ahora sabés Git de punta a punta.
