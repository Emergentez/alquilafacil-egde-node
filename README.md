# AlquilaFacil Edge Node

## Descripción

AlquilaFacil Edge Node es un servicio backend desarrollado en Python utilizando FastAPI, diseñado para recopilar y gestionar datos de sensores en locales alquilables. Este sistema actúa como un nodo de borde (edge node) en un entorno IoT, permitiendo el monitoreo en tiempo real de condiciones como humo, ruido y capacidad de ocupación en espacios rentables.

El proyecto sigue los principios de Clean Architecture, separando las capas de dominio, aplicación, infraestructura e interfaces para una mejor mantenibilidad y escalabilidad.

## Funcionalidades Principales

- **Gestión de Locales**: Creación y administración de locales con información de capacidad.
- **Recopilación de Lecturas de Sensores**: Soporte para sensores de humo, ruido y capacidad.
- **API REST**: Endpoints para acceder a las lecturas de sensores.
- **WebSockets**: Notificaciones en tiempo real a través de conexiones WebSocket.
- **Base de Datos**: Almacenamiento local utilizando SQLite.
- **Geolocalización**: Integración con geopy para funcionalidades relacionadas con ubicación.

## Arquitectura

El proyecto está estructurado siguiendo Clean Architecture:

- **Domain**: Contiene las entidades y lógica de negocio (e.g., `Local`, `Reading`).
- **Application**: Servicios de aplicación que orquestan la lógica.
- **Infrastructure**: Implementaciones concretas como modelos de base de datos y repositorios.
- **Interfaces**: Recursos REST y manejadores de WebSocket.

## Requisitos

- Docker y Docker Compose (recomendado)
- Python 3.9+ (si se ejecuta sin Docker)
- Archivo `.env` con las variables de configuración necesarias

## Instalación y Ejecución

### Opción 1: Usando Docker (Recomendado)

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/Emergentez/alquilafacil-egde-node.git
   cd alquilafacil-egde-node
   ```

2. **Crea el archivo `.env`**:
   Crea un archivo llamado `.env` en la raíz del proyecto con las siguientes variables (ajusta los valores según tu configuración):
   ```
   BACKEND_API_BASE_URL=http://localhost:3000
   TOKEN_EXPIRATION_SECONDS=3600
   AUTHENTICATION_EMAIL=admin@example.com
   AUTHENTICATION_PASSWORD=securepassword
   LOCAL_ID=1
   ```

3. **Ejecuta con Docker Compose**:
   ```bash
   docker-compose up --build
   ```

   Esto construirá la imagen Docker, instalará las dependencias y ejecutará la aplicación en el puerto 3000.

4. **Accede a la aplicación**:
   - API: http://localhost:3000
   - Documentación Swagger: http://localhost:3000/docs

### Opción 2: Ejecución Local sin Docker

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/Emergentez/alquilafacil-egde-node.git
   cd alquilafacil-egde-node
   ```

2. **Instala Python y dependencias**:
   Asegúrate de tener Python 3.9+ instalado. Luego:
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Crea el archivo `.env`**:
   Como en el paso 2 de la opción Docker.

4. **Ejecuta la aplicación**:
   ```bash
   uvicorn main:app --reload
   ```

   La aplicación estará disponible en http://localhost:8000 (puerto por defecto de Uvicorn).

## Uso

- **API Endpoints**:
  - `GET /api/v1/edge-node/readings`: Obtener lecturas de sensores.
  - Otros endpoints disponibles en la documentación Swagger.

- **WebSocket**:
  - Conéctate a `/api/v1/web-socket` para recibir notificaciones en tiempo real.

## Contribución

1. Fork el proyecto.
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`).
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`).
4. Push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.