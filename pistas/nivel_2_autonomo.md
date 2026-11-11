# 💡 Nivel 2: Guía Autónoma (Pistas Conceptuales)

Este nivel está diseñado para desafiar la lógica de vuestro equipo. **No os daremos el código exacto**, sino pistas conceptuales y preguntas de razonamiento para que encontréis la solución por vosotros mismos.

---

## 🚪 Puerta 1: La Brújula (Git Bash / Terminal)
* **Pista 1 (Ubicación):** ¿Sabéis exactamente en qué directorio os encontráis? Recordad la orden que significa *"Print Working Directory"*.
* **Pista 2 (Visibilidad):** Los archivos que comienzan por punto (`.`) no se muestran con un listado básico. Buscad las opciones compuestas del comando de listado (`ls`) que revelan elementos ocultos (`-a`).
* **Pista 3 (Lectura rápida):** Para inspeccionar el texto de un archivo plano desde la terminal sin abrir editores gráficos, recordad el comando que proviene de la palabra *"catenar"*.

---

## 🛡️ Puerta 2: El Escudo (Git + GitHub)
* **Pista 1 (Flujo Local):** Guardar un archivo en el editor no hace que Git lo registre automáticamente. Necesitáis dos pasos: preparar el escenario (*Staging Area*) y congelar la versión (*Commit*).
* **Pista 2 (Local vs Remoto):** Un `git commit` vive **únicamente en tu disco duro**. Para que aparezca en GitHub, debes *"empujar"* los cambios hacia el servidor remoto (`origin`).
* **Pista 3 (Ramas):** Aseguraos de que vuestra rama local coincida con la rama por defecto de GitHub (habitualmente `main`).

---

## ✒️ Puerta 3: La Pluma Digital (VS Code - Documentación Markdown)
* **Pista 1 (Sintaxis):** Los archivos `.md` usan sintaxis ligera. Recordad que `#` se usa para el título principal, `##` para subtítulos y `-` o `1.` para listas estructuradas.
* **Pista 2 (Vista Previa):** En VS Code podéis ver el documento renderizado en tiempo real abriendo la vista previa dividida (`Ctrl + K` `V`).
* **Pista 3 (Entregables):** Aseguraos de guardar la bitácora dentro de la carpeta destinada a auditoría (`evidencias/`).

---

## 👁️ Puerta 4: El Visor (VS Code - IDE & Entorno)
* **Pista 1 (Perspectiva de Proyecto):** En lugar de abrir los archivos por separado, abrid la carpeta completa desde la consola (`code .`). Esto os permitirá ver el árbol de trabajo completo en el panel izquierdo.
* **Pista 2 (Gestión de Dependencias):** Para instalar todas las librerías necesarias de golpe, usad el gestor de paquetes de Python (`pip`) junto con el flag `-r` apuntando al archivo de requerimientos.
* **Pista 3 (Portabilidad):** Al indicar rutas en vuestra documentación, usad rutas relativas respecto a la raíz (`data/reservas_raw.csv`) y no rutas absolutas de vuestro disco local.

---

## ⚙️ Puerta 5: El Motor (Python CLI)
* **Pista 1 (Rutas de Ejecución):** Para ejecutar un script guardado en una subcarpeta desde la raíz, pasadle a Python la ruta relativa del archivo (`python scripts/conciliacion_hotel.py`).
* **Pista 2 (Diagnóstico de Errores):** Si la consola devuelve un error `FileNotFoundError`, leed detenidamente la ruta en la que Python busca el archivo. ¿Estáis ejecutando el comando desde la carpeta raíz correcta?
* **Pista 3 (Lógica Financiera):** Si una reserva figura como `Cancelada`, ¿el hotel llegó a percibir ese ingreso? Si fue `Devuelta`, ¿permanece el dinero en la caja?

---

## 🔮 Puerta 6: El Oráculo (Jupyter Notebook, DataViz e IA)
* **Pista 1 (Vinculación de Kernel):** Si al intentar ejecutar una celda no ocurre nada o aparece `Kernel Not Selected`, elegid vuestro intérprete de Python en la esquina superior derecha.
* **Pista 2 (Calidad de Datos ETL):** Limpiar datos implica dos etapas: la calidad técnica (eliminar duplicados exactos y gestionar valores nulos) y el filtro de negocio (filtrar estados que no representan ventas efectivas).
* **Pista 3 (Prompting con Restricciones):** Para evitar que un modelo de IA invente datos (*alucinaciones*), proporcionad únicamente datos factuales en la sección `[CONTEXT]` y prohibid expresamente la generación de métricas no incluidas mediante el bloque `[CONSTRAINTS]`.