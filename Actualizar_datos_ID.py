# Importar la biblioteca pandas y asignarle el alias pd
import pandas as pd

# Leer el archivo Excel de entrada
input_file = 'CON_DATOS_REPETIDOS.xlsx'
df = pd.read_excel(input_file)

# Se requiere crear una columna BANDERA, la cual permitira elimminar todos los coincidentes salvo el de la BANDERA mas alta
# Eliminar duplicados en la columna 'ID' manteniendo la fila con el mayor valor en la columna 'BANDERA'
df = df.sort_values(by='BANDERA', ascending=False).drop_duplicates(subset='ID', keep='first')

# Guardar el DataFrame resultante en un nuevo archivo Excel
output_file = 'CON_SOLO_DATOS_ACTUALES.xlsx'
df.to_excel(output_file, index=False)

# Imprimir un mensaje de confirmación
print("Se ha creado el archivo de salida:", output_file)
