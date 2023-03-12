# BFF - Monolito Solutions

Este es el repositorio del microservicio BFF del proyecto "Entregas de los Alpes", el cual se encarga de recibir los pedidos del cliente. Este microservicio fue construido utilizando el framework FastAPI.

## Requerimientos

Para poder correr el microservicio Inbound, es necesario tener instalado lo siguiente:

- Python 3.10 o superior
- pip

Además, se necesitará instalar las dependencias del proyecto utilizando el siguiente comando:

```
pip install -r requirements.txt
```

## Configuración

Antes de correr el microservicio Inbound, es necesario configurar las direcciones del host de Apache Pulsar.
- La configuración de Apache Pulsar se encuentra en ```./utils.py```

## Correr el microservicio

Para correr el microservicio Inbound, use el siguiente comando:

```
python main.py
```

Una vez que el microservicio esté corriendo, se podrá hacer una petición HTTP POST al endpoint `/orders` para enviar un pedido al microservicio. El pedido debe incluir un formato similar a los encontrados en la carpeta de ```./json_examples```.
Adicionalmente, puede encontrar en la misma carpeta una colección de postman para pruebas, es necesario cambiar la IP del host en donde se esté sirviendo el bff.
