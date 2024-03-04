# PY-ActualizarDatosConBandera

Este programa sirve para actualizar datos "duplicados" mediante una bandera indicadora de fecha reciente. Por ejemplo:

Si para pedir un producto este pasa por 3 fases (registro, vista, entrega), necesitamos saber en qué fase se encuentra actualmente.

En enero este producto tenía solo Fase 1, con fecha 18/01/24. En su base de datos se vería así:

| ID | Producto | Fase 1   | Fase 2   | Fase 3   |
|----|----------|----------|----------|----------|
| 01 | Lentes   | 18/01/24 |          |          |

Pero tras febrero esto se debería actualizar y me pasan una nueva fila, en la cual agregan el progreso actual:

| ID | Producto | Fase 1   | Fase 2   | Fase 3   |
|----|----------|----------|----------|----------|
| 01 | Lentes   | 18/01/24 |          |          |
| 01 | Lentes   | 18/01/24 | 18/02/24 |          |

Lo que ocurre es que esto se toma como dato duplicado y con un "Eliminar duplicados" de Excel por ID, puede eliminarse el más actual (el segundo) lo cual no se quiere hacer. 

La solución es agregar una BANDERA: 

| ID | Producto | Fase 1   | Fase 2   | Fase 3   | BANDERA |
|----|----------|----------|----------|----------|---------|
| 01 | Lentes   | 18/01/24 |          |          | 1       |
| 01 | Lentes   | 18/01/24 | 18/02/24 |          | 2       |

Con esto al ejecutar nuestro código, solo quedaría el de la bandera mayor (que se entiende que es el más actual) dejando la siguiente fila:

| ID | Producto | Fase 1   | Fase 2   | Fase 3   | BANDERA |
|----|----------|----------|----------|----------|---------|
| 01 | Lentes   | 18/01/24 | 18/02/24 |          | 2       |

## Descripción

La herramienta utiliza las siguientes bibliotecas de Python:

- **pandas**: Para el manejo eficiente de datos en forma de DataFrame.

## Requisitos

Para utilizar esta herramienta, asegúrate de tener instaladas las siguientes bibliotecas de Python:

```bash
pip install pandas

```

Uso
1- Clona este repositorio en tu máquina local.
2- Instala las dependencias utilizando el comando mencionado anteriormente.
3- Ejecuta el script principal para comenzar a procesar tus datos de texto.

Contribuciones
¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, no dudes en enviar una solicitud de extracción.