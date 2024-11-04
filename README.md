PORYECTO BASE DE DATOS EN PYTHON/DJANGO
SISTEMA DE COMPRA Y FACTURACION

├───api/                  # API REST para el sistema
├───app/                  # Configuración principal de la aplicación
├───bases/               # Módulo base con funcionalidades comunes
├───cmp/                 # Módulo de compras
├───fac/                 # Módulo de facturación
├───inv/                 # Módulo de inventario
├───static/              # Archivos estáticos
│   └───base/
│       ├───css/         # Hojas de estilo personalizadas
│       ├───img/         # Imágenes
│       ├───js/          # JavaScript personalizado
│       └───vendor/      # Bibliotecas de terceros
└───templates/           # Plantillas HTML

Tecnologías Utilizadas 🛠️

Django (Framework principal)
Bootstrap (Frontend)
jQuery
Chart.js (Para gráficos)
DataTables
FontAwesome (Iconos)

Características Principales ✨

Sistema de autenticación y autorización
Gestión de inventario
Sistema de facturación
Gestión de compras
API REST para integración con otros sistemas
Interfaz responsive y moderna

Requisitos Previos 📋

Python 3.x
Django (última versión estable)
Base de datos PostgreSQL
Pip (Gestor de paquetes de Python)

Instalación 🔧

Clonar el repositorio:

git clone https://github.com/SeCo72/ProyectoSistemaCompraFacturacion.git

Crear y activar entorno virtual:

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

Instalar dependencias:

pip install -r requirements.txt

Realizar migraciones:

python manage.py makemigrations
python manage.py migrate

Crear superusuario:

python manage.py createsuperuser

Ejecutar el servidor:

python manage.py runserver
