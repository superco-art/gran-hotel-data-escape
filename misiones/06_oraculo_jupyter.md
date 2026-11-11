### `misiones/06_oraculo_jupyter.md`

```markdown
# 🔮 Puerta 6: El Oráculo (Jupyter Notebooks, DataViz & IA Generativa)
**Sprint 6: Auditoría Interactiva, Data Viz y Reporte Ejecutivo con IA**

## 🕵️‍♀️ Contexto de la Misión
Estamos en la etapa final de la investigación. Para presentar nuestras conclusiones a la Dirección General del Gran Hotel Olimpo, debemos utilizar **El Oráculo (Jupyter Notebooks en VS Code)**. 

En este sprint realizaremos una limpieza profunda con **Pandas** (eliminación de duplicados exactos y tratamiento de nulos), crearemos un gráfico ejecutivo de facturación con **Matplotlib**, aplicaremos **IA Generativa Responsable (Prompting Estructurado con Guardrails)** para redactar el comunicado y dejaremos constancia de las conclusiones.

---

## 👥 Dinámica AGILE & Trabajo en Parejas
* 🔄 **CAMBIO DE ROLES:** Último cambio de roles. Ambas personas deben participar activamente en la ejecución de celdas y en la redacción final.

---

## 🎯 Objetivos Técnicos y Pedagógicos
1. Manejar Jupyter Notebooks dentro de VS Code: selección de Kernel, ejecución secuencial de celdas y estado de memoria.
2. Aplicar operaciones de limpieza de datos en Pandas (`drop_duplicates()`, `isnull()`, filtrado por condiciones).
3. Construir gráficos explicativos con Matplotlib adaptados a audiencias no técnicas.
4. Diseñar prompts estructurados (Rol + Contexto factual + Tarea + Restricciones) para LLMs evitando alucinaciones y evaluando sesgos.

---

## 📜 Paso a Paso del Sprint

1. **Abrir el Notebook:** En VS Code, navega a `notebooks/analisis_gran_hotel.ipynb`.
2. **Seleccionar el Kernel de Python:** En la esquina superior derecha del editor del notebook, haz clic en **Select Kernel** y selecciona tu intérprete activo de Python 3.x.
3. **Ejecutar Celdas de Carga y Limpieza (Paso 1 y 2):**
   * Ejecuta la celda de importación de librerías y carga mediante `pathlib` dinámico.
   * Revisa cuántos duplicados exactos detecta Pandas (`df.duplicated().sum()`).
   * Aplica la deduplicación y comprueba cuántas filas reales quedan en el dataset.
4. **Calcular la Facturación Real (Paso 3):**
   * Filtra las reservas con estado `Completada`.
   * Compara la facturación bruta inicial frente a los ingresos netos reales.
5. **Generar la Visualización Ejecutiva (Paso 4):**
   * Ejecuta la celda del gráfico de barras en Matplotlib.
   * Revisa que las etiquetas de los ejes y los colores distingan claramente los ingresos reales de la fuga financiera.
6. **IA Generativa Aplicada & Prompting Responsable (Paso 5):**
   * Inspecciona el bloque del **Prompt Estructurado**.
   * Identifica cómo el prompt delimita las **restricciones de factualidad** para que la LLM no invente datos (*guardrails contra alucinaciones*).
   * Copia el prompt generado y pruébalo en una LLM (ChatGPT/Claude). Revisa si la respuesta devuelta contiene sesgos o datos no presentes en el contexto.
7. **Redactar la Conclusión del Equipo (Paso 6):**
   * En la última celda de Markdown del notebook, redactad en 2 o 3 frases la conclusión analítica respondiendo: *¿A cuánto asciende la cifra real de ingresos del hotel y qué acciones de calidad de datos se aplicaron?*
8. **Commit y Push Final:** Guarda el notebook ejecutado y sube la versión definitiva a tu repositorio público de GitHub:
   ```bash
   git add notebooks/ evidencias/
   git commit -m "feat: auditoria final completada con notebook, viz e informe IA"
   git push origin main