# 📘 Teacher & Facilitator Guide: Gran Hotel Olimpo Escape Room
**Modulo 0: Welcome & Technical Stack Onboarding**

---

## 🎯 1. Marco Pedagógico y Metodológico

Esta actividad utiliza una **Pedagogía Activa basada en Retos (Challenge-Based Learning)** y gamificación mediante un Escape Room. Está diseñada para mitigar la fricción cognitiva inicial frente a la consola (CLI), Git, VS Code y Python en perfiles principiantes.

* **Metodología AGILE / Scrum:**
  - Estructuración del trabajo en 6 Sprints (correspondientes a las 6 Puertas).
  - Trabajo colaborativo obligatorio en parejas bajo la dinámica **Piloto (Teclado) / Copiloto (Navegante)**.
  - Rotación obligatoria de roles en cada Sprint para asegurar el desarrollo de competencias en ambos integrantes.
* **Seguridad Psicológica & Cultura del Error:**
  - Los errores en consola o Git se abordan como fuentes de aprendizaje y diagnóstico técnico, evaluando la capacidad de lectura de documentación y trazabilidad de fallos.

---

## 📊 2. Matriz de Competencias Evaluadas

| Dimensión | Competencia Técnica / Transversal | Evidencia de Aprendizaje |
| :--- | :--- | :--- |
| **CLI & Entorno** | Navegación por terminal, gestión de archivos y variables de entorno. | Resolución de rutas en Git Bash e instalación de `requirements.txt`. |
| **Control de Versiones** | Flujo Git (Init, Add, Commit, Push) y GitHub. | Repositorio remoto actualizado y mensajes de commit bajo convenciones. |
| **Editor e IDE** | Documentación estructurada en Markdown y workspace en VS Code. | Edición de `bitacora_investigador.md` y cartografía en `mapa_hotel.md`. |
| **Scripting Python** | Ejecución de scripts CLI, librerías estándar y tratamiento ETL. | Procesamiento de `reservas_raw.csv` mediante `conciliacion_hotel.py`. |
| **Analytics & DataViz** | Limpieza en Pandas (nulos/duplicados), facturación neta vs bruta y Matplotlib. | Cuaderno `analisis_gran_hotel.ipynb` ejecutado con gráficos explicativos. |
| **IA Generativa** | Prompting estructurado (Rol, Contexto, Restricciones) e inspección de sesgos/alucinaciones. | Definición de guardrails en la celda de síntesis ejecutiva. |
| **Transversales** | Comunicación técnica, gestión de la frustración y trabajo AGILE en equipo. | Calidad de la bitácora y participación en la rotación Piloto/Copiloto. |

---

## ⏱️ 3. Distribución Temporal del Timeboxing (340 min)

* **Bloque 1 (60 min):** Lore, constitución de parejas AGILE, Sprint 1 (Git Bash) y Sprint 2 (Git/GitHub).
* **Bloque 2 (90 min):** Sprint 3 (VS Code & Markdown) y Sprint 4 (IDE Workspace & `requirements.txt`).
* **Bloque 3 (120 min):** Sprint 5 (Python CLI & ETL inicial) y Sprint 6 (Jupyter, DataViz & Prompting con IA).
* **Bloque 4 (70 min):** Retro AGILE, presentación de conclusiones por pareja, Ticket de Salida y Semáforo de Aprendizaje.

---

## 🚦 4. Sistema de Acompañamiento y Andamiaje (Scaffolding)

El progreso del alumnado está asistido por un sistema de apoyo en 3 niveles disponibles en la carpeta `pistas/`:
* **Nivel 1 (Guía):** Asistencia directa con sintaxis explícita.
* **Nivel 2 (Autónomo):** Pistas conceptuales y preguntas orientadoras de razonamiento.
* **Nivel 3 (Reto Extra):** Desafíos de profundización (MLOps lite, Bash scripting, evaluación de alucinaciones en IA) para equipos con ritmo avanzado.

---

## 📝 5. Evaluación Formativa y Ticket de Salida

Al finalizar la sesión, cada estudiante completa de forma individual su **Semáforo de Aprendizaje**:
* 🟢 **Verde (Nivel A):** Capaz de realizar el flujo de forma autónoma y explicarlo a una compañera.
* 🟡 **Amarillo (Nivel B):** Comprende el concepto pero requiere consultar la sintaxis en la guía.
* 🔴 **Rojo (Nivel C):** Requiere refuerzo práctico en los próximos bloques del bootcamp.