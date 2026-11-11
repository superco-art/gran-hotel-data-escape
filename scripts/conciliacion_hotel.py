import csv
import os
import sys

# 1. Definición de rutas relativas dentro de la estructura del proyecto
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, ".."))

DATA_PATH = os.path.join(PROJECT_ROOT, "data", "reservas_raw.csv")
EVIDENCIAS_DIR = os.path.join(PROJECT_ROOT, "evidencias")
OUTPUT_PATH = os.path.join(EVIDENCIAS_DIR, "informe_preliminar.txt")

def ejecutar_conciliacion():
    # Verificar la existencia del dataset de entrada
    if not os.path.exists(DATA_PATH):
        print(f"❌ Error: No se encontró el archivo de datos en '{DATA_PATH}'.")
        print("💡 Pista: Ejecuta primero 'python scripts/make_dataset.py' para generar los datos.")
        sys.exit(1)

    total_transacciones = 0
    totales_por_estado = {
        "Completada": {"count": 0, "ingresos": 0.0},
        "Cancelada": {"count": 0, "ingresos": 0.0},
        "Devuelta": {"count": 0, "ingresos": 0.0},
        "Sin Estado / Error": {"count": 0, "ingresos": 0.0}
    }

    # 2. Lectura y procesamiento del archivo CSV
    with open(DATA_PATH, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            total_transacciones += 1
            estado = row["estado"].strip() if row["estado"] else "Sin Estado / Error"
            
            # Cálculo del subtotal por reserva (precio_noche * noches)
            try:
                precio = float(row["precio_noche"]) if row["precio_noche"] else 0.0
                noches = int(float(row["noches"])) if row["noches"] else 0
                subtotal = precio * noches
            except ValueError:
                subtotal = 0.0

            # Acumular según el estado registrado
            if estado in totales_por_estado:
                totales_por_estado[estado]["count"] += 1
                totales_por_estado[estado]["ingresos"] += subtotal
            else:
                totales_por_estado["Sin Estado / Error"]["count"] += 1
                totales_por_estado["Sin Estado / Error"]["ingresos"] += subtotal

    # 3. Salida por Consola (Feedback pedagógico inmediato)
    print("\n==================================================")
    print("🏨 GRAN HOTEL OLIMPO - INFORME DE CONCILIACIÓN")
    print("==================================================")
    print(f"📊 Número total de transacciones procesadas: {total_transacciones}")
    print("--------------------------------------------------")
    print(f"✅ Completadas : {totales_por_estado['Completada']['count']:2d} reservas | Subtotal bruto: {totales_por_estado['Completada']['ingresos']:>10.2f} €")
    print(f"❌ Canceladas  : {totales_por_estado['Cancelada']['count']:2d} reservas | Importe perdido: {totales_por_estado['Cancelada']['ingresos']:>10.2f} €")
    print(f"⚠️  Devueltas   : {totales_por_estado['Devuelta']['count']:2d} reservas | Importe devuelto: {totales_por_estado['Devuelta']['ingresos']:>9.2f} €")
    print("--------------------------------------------------")

    # 4. Generación del reporte escrito en evidencias/informe_preliminar.txt
    os.makedirs(EVIDENCIAS_DIR, exist_ok=True)
    
    with open(OUTPUT_PATH, mode="w", encoding="utf-8") as out_file:
        out_file.write("==================================================\n")
        out_file.write("   INFORME PRELIMINAR DE CONCILIACIÓN FINANCIERA  \n")
        out_file.write("==================================================\n\n")
        out_file.write(f"Total de transacciones registradas: {total_transacciones}\n\n")
        out_file.write("RESUMEN DE INGRESOS POR ESTADO:\n")
        out_file.write(f"- COMPLETADAS : {totales_por_estado['Completada']['ingresos']:.2f} € ({totales_por_estado['Completada']['count']} reservas)\n")
        out_file.write(f"- CANCELADAS  : {totales_por_estado['Cancelada']['ingresos']:.2f} € ({totales_por_estado['Cancelada']['count']} reservas)\n")
        out_file.write(f"- DEVUELTAS   : {totales_por_estado['Devuelta']['ingresos']:.2f} € ({totales_por_estado['Devuelta']['count']} reservas)\n")
        out_file.write(f"- S/ESTADO    : {totales_por_estado['Sin Estado / Error']['ingresos']:.2f} € ({totales_por_estado['Sin Estado / Error']['count']} reservas)\n\n")
        out_file.write("--------------------------------------------------\n")
        out_file.write("PREGUNTA DE INVESTIGACIÓN PARA EL EQUIPO DE DATOS:\n")
        out_file.write("¿El total de ingresos del hotel debe incluir las reservas canceladas y devueltas?\n")
        out_file.write("Documenta tu conclusión analítica en tu Notebook (Puerta 6).\n")

    print(f"💾 Informe guardado correctamente en: evidencias/informe_preliminar.txt\n")

if __name__ == "__main__":
    ejecutar_conciliacion()