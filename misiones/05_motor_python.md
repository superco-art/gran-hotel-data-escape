### `misiones/05_motor_python.md`

```markdown
# ⚙️ Puerta 5: El Motor (Python CLI - Procesamiento Scripting)
**Sprint 5: Conciliación Financiera Inicial**

## 🕵️‍♀️ Contexto de la Misión
¡Llegamos al núcleo del problema! El ataque al Gran Hotel Olimpo mezcló en una misma tabla las reservas **Completadas**, las **Canceladas** y las **Devueltas**. La recepción afirma que ingresaron miles de euros, pero la caja real está vacía.

Activaremos **El Motor (Python desde Consola CLI)** para ejecutar un script de procesamiento de datos que lea el archivo CSV, realice la conciliación inicial y genere un informe preliminar de auditoría.

---

## 👥 Dinámica AGILE & Trabajo en Parejas
* 🔄 **CAMBIO DE ROLES:** Rotad los roles de Piloto y Copiloto al tomar el teclado.

---

## 🎯 Objetivos Técnicos y Pedagógicos
1. Ejecutar scripts de Python (`.py`) directamente desde la consola de comandos.
2. Aplicar lógica de filtrado de datos: diferenciar volumen total bruto de facturación neta efectiva.
3. Inspeccionar archivos de salida generados automáticamente por un programa en Python.

---

## 📜 Paso a Paso del Sprint

1. **Verificar el Dataset Bruto:** Confirma que el archivo `data/reservas_raw.csv` existe en tu proyecto. Si no existiera o estuviera corrupto, ejecútalo para generarlo:
   ```bash
   python scripts/make_dataset.py
