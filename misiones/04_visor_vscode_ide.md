### `misiones/04_visor_vscode_ide.md`

```markdown
# 👁️ Puerta 4: El Visor (VS Code - IDE & Gestión del Proyecto)
**Sprint 4: Cartografía de la Arquitectura y Entorno**

## 🕵️‍♀️ Contexto de la Misión
Estamos a punto de acceder al motor de datos del hotel. Antes de ejecutar código de análisis, debemos activar **El Visor (VS Code como IDE integral)** para entender la arquitectura del proyecto, verificar el intérprete de Python e instalar las dependencias técnicas necesarias para procesar grandes volúmenes de información.

---

## 👥 Dinámica AGILE & Trabajo en Parejas
* 🔄 **CAMBIO DE ROLES:** Rotad los roles de Piloto y Copiloto.

---

## 🎯 Objetivos Técnicos y Pedagógicos
1. Entender la estructura estándar de carpetas de un proyecto de datos (`data/`, `scripts/`, `notebooks/`, `evidencias/`).
2. Configurar el entorno virtual y el intérprete de Python 3.x dentro de VS Code.
3. Instalar librerías externas de datos mediante `pip` y el archivo de requerimientos `requirements.txt`.

---

## 📜 Paso a Paso del Sprint

1. **Inspeccionar la Terminal Integrada:** En VS Code, abre la terminal integrada con `Ctrl + Ñ` (o `Ctrl + ~`). Asegúrate de que la terminal sea **Git Bash**.
2. **Verificar el Entorno de Python:** Comprueba qué versión de Python tiene configurada tu sistema:
   ```bash
   python --version
   # O en Windows: py --version