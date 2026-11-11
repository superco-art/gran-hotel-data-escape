# 🧭 Nivel 1: Guía Paso a Paso (Pistas Directas)

Esta guía proporciona la **sintaxis exacta y los comandos explícitos** para superar cada una de las 6 Puertas del Escape Room *"Fuga de Datos en el Gran Hotel Olimpo"*. Úsala si tu equipo se atasca en la sintaxis o necesita verificar un comando.

---

## 🚪 Puerta 1: La Brújula (Git Bash / Terminal)
**Objetivo:** Explorar el servidor y localizar la contraseña oculta `.llave_maestra.txt`.

 **Verificar directorio actual:**
   ```bash
   pwd
  1. Listar todos los archivos (incluyendo ocultos): ls -la
  2. Navegar a la carpeta del proyecto (si no estás en ella):cd gran-hotel-data-escape
  3. Leer el archivo de bienvenida:cat COMIENZA_AQUI.txt
  4. Leer el archivo oculto encontrado: cat .llave_maestra.txt

  🛡️ Puerta 2: El Escudo (Git + GitHub)
Objetivo: Crear un respaldo seguro del estado de la recepción en GitHub.
    1. Inicializar Git (si no está inicializado):

Bash
git init
    2. Añadir el archivo README al área de preparación (Staging Area):

Bash
git add README.md
    3. Registrar el primer commit local con convención AGILE:

Bash
git commit -m "feat: inicio de investigacion tras ataque al Gran Hotel Olimpo"
    4. Revisar el historial de commits:

Bash
git log --oneline

    5. Vincular y publicar en tu perfil personal de GitHub:

Bash
git branch -M main
git remote add origin [https://github.com/TU_USUARIO/gran-hotel-data-escape.git](https://github.com/TU_USUARIO/gran-hotel-data-escape.git)
git push -u origin main
(Si falla la autenticación remota en el aula, anota en tu bitácora "Commit local registrado; push pendiente" y avanza a la Puerta 3).
-------------------------------------------------------------------------------------------------
✒️ Puerta 3: La Pluma Digital (VS Code - Documentación Markdown)
Objetivo: Redactar la bitácora de investigación en formato Markdown usando VS Code.
1. Abrir la carpeta del proyecto en VS Code desde Git Bash:

Bash
code .
2. Abrir el archivo de evidencias: En el panel explorador de VS Code, abre evidencias/bitacora_investigador.md.

3. Activar la vista previa: Pulsa Ctrl + K y luego V (o haz clic en el icono de vista previa dividida).

4. Completar las secciones requeridas:

Markdown
# 📝 Bitácora de Investigación - Gran Hotel Olimpo

## 1. Hallazgo Inicial
Se ha localizado la llave maestra en `.llave_maestra.txt` usando Git Bash (`ls -la`).

## 2. Comando Útil de Git
`git commit -m "..."` permite congelar el estado de la investigación antes de aplicar cambios en el código.

## 3. Hipótesis Financiera
Las reservas canceladas y devueltas están inflando la cifra bruta de ingresos, distorsionando la caja real.
Guardar los cambios: Pulsa Ctrl + S y verifica el archivo desde la terminal integrada (Ctrl + Ñ).
--------------------------------------------------------------------------------------------
👁️ Puerta 4: El Visor (VS Code - IDE & Entorno)
Objetivo: Cartografiar la arquitectura del proyecto e instalar las dependencias de datos.

1. Abrir la terminal integrada en VS Code: Pulsa Ctrl + Ñ y asegúrate de seleccionar Git Bash.

2. Comprobar el intérprete de Python:

Bash
python --version

3. Instalar dependencias necesarias (Pandas, Matplotlib, Jupyter):

Bash
pip install -r requirements.txt

4. Cartografiar el proyecto: Abre evidencias/mapa_hotel.md y documenta las 3 rutas clave:

Markdown
# 🗺️ Mapa de Estructura del Proyecto

1. `data/reservas_raw.csv` -> Dataset bruto con reservas, valores nulos y duplicados.
2. `scripts/conciliacion_hotel.py` -> Script de consola Python para filtrado inicial.
3. `notebooks/analisis_gran_hotel.ipynb` -> Cuaderno interactivo de análisis final y DataViz.

5. Registrar en Git:

Bash
git add evidencias/
git commit -m "docs: mapa de proyecto y dependencias instaladas"
----------------------------------------------------------------------------------------------------

⚙️ Puerta 5: El Motor (Python CLI)
Objetivo: Ejecutar el script de conciliación financiera desde la terminal.

1. Verificar o regenerar el dataset bruto:

Bash
python scripts/make_dataset.py

2. Ejecutar el script de conciliación financiera:

Bash
python scripts/conciliacion_hotel.py

3. Visualizar el informe generado en evidencias:

Bash
cat evidencias/informe_preliminar.txt

4. Debate con tu pareja (Piloto/Copiloto): Observa los subtotales de Completada, Cancelada y Devuelta. ¿Cuáles representan ingresos reales en caja?
----------------------------------------------------------------------------------------------------

🔮 Puerta 6: El Oráculo (Jupyter Notebook, DataViz e IA)
Objetivo: Limpiar datos con Pandas, generar visualizaciones con Matplotlib y construir un prompt estructurado con restricciones factuales.

1. Abrir el cuaderno: Navega a notebooks/analisis_gran_hotel.ipynb.

2. Vincular el Kernel: En la esquina superior derecha, haz clic en Select Kernel y elige tu entorno de Python 3.x.

3. Ejecutar celdas en orden: Pulsa ▶ en cada celda secuencialmente:

Limpieza de duplicados: df_cleaned = df_raw.drop_duplicates()

Filtrado de facturación efectiva: df_ventas = df_cleaned[df_cleaned['estado'] == 'Completada']

4. Visualización en Matplotlib: Revisa que el gráfico de barras diferencie correctamente los ingresos reales de la fuga financiera.

5. Prompting Estructurado e IA: Examina el prompt con formato [ROLE], [CONTEXT], [TASK] y [CONSTRAINTS]. Copia el resultado en tu IA de referencia y verifica que no contenga alucinaciones ni sesgos.

6. Redactar conclusión: Escribe 2 frases ejecutivas en la última celda de Markdown del notebook.