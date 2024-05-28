# FastAPI Inventory Management System

Este proyecto es una API backend desarrollada con FastAPI para la gestión de productos, categorías, proveedores, facturas, remitos, órdenes de pedido y control de stock. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre cada entidad.

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)
- [Modelos](#modelos)
  - [Product](#product)
  - [Category](#category)
  - [Provider](#provider)
  - [Invoice](#invoice)
  - [Remittance](#remittance)
  - [Order](#order)
  - [Stock](#stock)
- [Esquemas](#esquemas)
- [Operaciones CRUD](#operaciones-crud)
- [Base de Datos](#base-de-datos)
- [Dependencias](#dependencias)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Instalación

1. Clona el repositorio:

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd project
    ```

2. Crea y activa un entorno virtual:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\\Scripts\\activate`
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Configura la base de datos en el archivo `.env`.

5. Inicia el servidor:

    ```bash
    uvicorn app.main:app --reload
    ```

## Uso

Una vez iniciado el servidor, puedes acceder a la documentación interactiva de la API en `http://127.0.0.1:8000/docs`.

## Modelos

### Product

- **Campos**:
  - `id`: Identificador único del producto.
  - `name`: Nombre del producto.
  - `description`: Descripción del producto.
  - `price`: Precio del producto.
  - `category_id`: Identificador de la categoría a la que pertenece el producto.

### Category

- **Campos**:
  - `id`: Identificador único de la categoría.
  - `name`: Nombre de la categoría.

### Provider

- **Campos**:
  - `id`: Identificador único del proveedor.
  - `name`: Nombre del proveedor.
  - `contact_info`: Información de contacto del proveedor.

### Invoice

- **Campos**:
  - `id`: Identificador único de la factura.
  - `provider_id`: Identificador del proveedor.
  - `date`: Fecha de la factura.
  - `total`: Total de la factura.

### Remittance

- **Campos**:
  - `id`: Identificador único del remito.
  - `order_id`: Identificador de la orden de pedido.
  - `date`: Fecha del remito.

### Order

- **Campos**:
  - `id`: Identificador único de la orden.
  - `provider_id`: Identificador del proveedor.
  - `date`: Fecha de la orden.
  - `status`: Estado de la orden.

### Stock

- **Campos**:
  - `id`: Identificador único del stock.
  - `product_id`: Identificador del producto.
  - `quantity`: Cantidad en stock del producto.

## Esquemas

Los esquemas se utilizan para validar y serializar los datos. Cada entidad tiene su propio esquema de entrada (para creación y actualización) y esquema de salida.

## Operaciones CRUD

Cada entidad soporta las siguientes operaciones CRUD:

- **Crear**: Permite agregar una nueva entidad.
- **Leer**: Permite obtener una entidad por su identificador y listar todas las entidades.
- **Actualizar**: Permite modificar una entidad existente.
- **Eliminar**: Permite eliminar una entidad existente.

## Base de Datos

### Configuración

La base de datos se configura en el archivo `database.py` utilizando SQLAlchemy. El archivo `.env` se utiliza para almacenar las configuraciones de la base de datos.

### Migraciones

Para aplicar migraciones a la base de datos, utiliza la herramienta `alembic`.

## Dependencias

El archivo `requirements.txt` incluye todas las dependencias necesarias para el proyecto. Estas incluyen:

- `fastapi`: Framework web para construir la API.
- `uvicorn`: Servidor ASGI para ejecutar la aplicación FastAPI.
- `sqlalchemy`: ORM para interactuar con la base de datos.
- `pydantic`: Para la validación de datos.
- `alembic`: Herramienta para migraciones de la base de datos.

## Contribución

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza los cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Empuja los cambios a tu rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
