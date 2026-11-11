import pandas as pd
import numpy as np

# Semilla para reproducibilidad técnica
np.random.seed(42)

n_rows = 90
ids = [f"RES-{1000 + i}" for i in range(1, n_rows + 1)]
clientes = [
    "Ana García", "Carlos López", "María Rodríguez", "Juan Martínez", "Elena Gómez",
    "David Fernández", "Lucia Pérez", "Javier Sánchez", "Sofia Romero", "Diego Navarro",
    "Laura Torres", "Pablo Ruiz", "Carmen Díaz", "Álvaro Morales", "Marta Castro"
]
fechas = pd.date_range(start="2026-02-01", end="2026-03-15", freq="D").strftime("%Y-%m-%d").tolist()
estados = ["Completada", "Completada", "Completada", "Cancelada", "Devuelta"]
precios = [85.0, 120.0, 150.0, 200.0, 250.0, 310.0]
noches_list = [1, 2, 3, 4, 5, 7]

data = []
for i in range(n_rows):
    data.append({
        "id_reserva": ids[i],
        "cliente": np.random.choice(clientes),
        "fecha": np.random.choice(fechas),
        "estado": np.random.choice(estados),
        "precio_noche": np.random.choice(precios),
        "noches": np.random.choice(noches_list)
    })

df = pd.DataFrame(data)

# Introducción intencionada de valores nulos (NaN / Vacíos)
df.loc[5, "cliente"] = ""
df.loc[12, "precio_noche"] = ""
df.loc[25, "noches"] = ""
df.loc[40, "estado"] = ""
df.loc[58, "cliente"] = ""
df.loc[72, "precio_noche"] = ""

# Introducción intencionada de filas duplicadas (10 filas exactamente iguales)
duplicates = df.iloc[[3, 10, 15, 22, 30, 45, 50, 63, 77, 85]].copy()
df_final = pd.concat([df, duplicates], ignore_index=True)

# Mezcla aleatoria respetando la reproducibilidad
df_final = df_final.sample(frac=1, random_state=42).reset_index(drop=True)

# Guardar en la carpeta data/
df_final.to_csv("data/reservas_raw.csv", index=False)
print("✅ Dataset data/reservas_raw.csv creado con éxito (100 filas).")