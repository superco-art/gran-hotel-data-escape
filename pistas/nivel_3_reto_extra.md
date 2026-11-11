# 🚀 Nivel 3: Retos Extra y Profundización (Nivel Avanzado)

Si vuestro equipo ha completado las 6 Puertas antes de tiempo o quiere explorar conceptos avanzados de **Ingeniería de Datos, Scripting Bash, MLOps "lite" e IA Generativa**, resolved los siguientes desafíos técnicos.

---

## 🚪 Reto Extra 1: Terminal & Scripting Bash (Puerta 1)
* **Desafío:** Sin utilizar Python ni editores gráficos, usa comandos puros de la terminal Bash para contar cuántas filas totales tiene el dataset `data/reservas_raw.csv` y mostrar únicamente las primeras 5 reservas.
* **Pregunta:** ¿Qué combinación de comandos (`wc -l`, `head`, `grep` y tuberías `|`) te permite saber cuántas reservas en el CSV tienen el estado `Completada` directamente desde la consola?

---

## 🛡️ Reto Extra 2: Git Avanzado & Estrategia de Ramas (Puerta 2)
* **Desafío:** Crea una rama secundaria llamada `feature/limpieza-datos` con `git checkout -b feature/limpieza-datos`. Realiza un cambio en la bitácora, registra un commit en esa rama y luego fusiona (`git merge`) los cambios de vuelta a la rama `main`.
* **Pregunta:** ¿Por qué en metodologías AGILE y entornos profesionales de desarrollo nunca se debe subir código directamente a la rama `main` sin pasar por una revisión de código (*Pull Request*)?

---

## 👁️ Reto Extra 3: Control de Entorno & Ocultación en IDE (Puerta 4)
* **Desafío:** Inspecciona la carpeta `.vscode/settings.json`. Configura la regla `"files.exclude"` para que los archivos temporales de Python (`__pycache__`) o notebooks (`.ipynb_checkpoints`) tampoco aparezcan en la barra lateral de VS Code.
* **Pregunta:** ¿Qué diferencia existe entre ignorar un archivo para el control de versiones (`.gitignore`) y ocultar un archivo en la interfaz visual de un IDE (`settings.json`)?

---

## ⚙️ Reto Extra 4: Python & MLOps "Lite" (Puerta 5)
* **Desafío:** Modifica el script `scripts/conciliacion_hotel.py` para que calcule automáticamente el **ticket medio por noche** de las reservas completadas (`ingresos_totales / noches_totales`).
* **Pregunta:** Si quisieras garantizar la reproducibilidad completa de este experimento en un pipeline de datos, ¿qué información deberías registrar en un archivo `model_card.md` o en un registro de trazabilidad (*logging*)?

---

## 🔮 Reto Extra 5: IA Generativa Responsable & Evaluación de Salidas (Puerta 6)
* **Desafío:** Utiliza el prompt estructurado generado en tu notebook y pásalo por dos modelos de IA diferentes (ej. ChatGPT y Claude). 
* **Evaluación de Guardrails y Sesgos:**
  - ¿Alguna de las IAs ha incluido supuestos o métricas financieras que no estaban en vuestro contexto?
  - ¿El lenguaje utilizado presenta algún sesgo de culpabilidad hacia la recepción del hotel o se mantiene en un tono profesional neutro?
  - Documenta esta evaluación de salidas en la bitácora (`evidencias/bitacora_investigador.md`).