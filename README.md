# 🏪 Sistema de Compra y Facturación

Sistema integral para la gestión de inventario, compras y facturación desarrollado con Python/Django.

## 📋 Contenido
- [Características](#-características)
- [Tecnologías](#-tecnologías)
- [Estructura](#-estructura)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Uso](#-uso)

## ✨ Características

<table>
  <tr>
    <td>
      <h3 align="center">📊 Gestión de Inventario</h3>
      <ul>
        <li>✓ Control de stock en tiempo real</li>
        <li>✓ Categorización inteligente de productos</li>
        <li>✓ Sistema de alertas de inventario bajo</li>
        <li>✓ Gestión de ubicaciones y almacenes</li>
      </ul>
    </td>
    <td>
      <h3 align="center">💰 Facturación</h3>
      <ul>
        <li>✓ Generación automática de facturas</li>
        <li>✓ Control avanzado de pagos</li>
        <li>✓ Reportes detallados de ventas</li>
        <li>✓ Integración con sistemas fiscales</li>
      </ul>
    </td>
  </tr>
  <tr>
    <td>
      <h3 align="center">🛍️ Compras</h3>
      <ul>
        <li>✓ Gestión integral de proveedores</li>
        <li>✓ Sistema de órdenes de compra</li>
        <li>✓ Seguimiento en tiempo real de pedidos</li>
        <li>✓ Historial de transacciones</li>
      </ul>
    </td>
    <td>
      <h3 align="center">🔑 Seguridad</h3>
      <ul>
        <li>✓ Control de acceso granular</li>
        <li>✓ Sistema de roles y permisos</li>
        <li>✓ Auditoría completa de cambios</li>
        <li>✓ Autenticación de doble factor</li>
      </ul>
    </td>
  </tr>
</table>

## 🛠️ Tecnologías

<div align="center">

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![jQuery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

</div>

### Componentes Adicionales
- 📊 Chart.js - Visualización de datos
- 📑 DataTables - Gestión de tablas
- 🎨 FontAwesome - Iconografía
- 🔄 REST Framework - API RESTful

## 📁 Estructura

```
📦 proyecto
├── 🔌 api/                # Endpoints REST y servicios
│   ├── views/
│   └── serializers/
├── ⚙️ app/                # Configuración principal
│   ├── settings/
│   └── urls/
├── 🏗️ bases/              # Módulos base del sistema
├── 🛍️ cmp/                # Gestión de compras
├── 💰 fac/                # Sistema de facturación
├── 📦 inv/                # Control de inventario
├── 🎨 static/             # Recursos estáticos
└── 📑 templates/          # Plantillas HTML
```

## 📋 Requisitos

- Python 3.8+
- PostgreSQL 12+
- Pip (Gestor de paquetes)
- Entorno virtual (recomendado)

## 🚀 Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/SeCo72/ProyectoSistemaCompraFacturacion.git
cd ProyectoSistemaCompraFacturacion
```

2. **Crear y activar entorno virtual**
```bash
python -m venv venv
venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar la base de datos**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Crear superusuario**
```bash
python manage.py createsuperuser
```

6. **Iniciar el servidor**
```bash
python manage.py runserver
```

## 💻 Uso

1. Accede a `http://localhost:8000/admin` para la interfaz de administración
2. Inicia sesión con las credenciales del superusuario
3. Comienza a gestionar tu inventario, compras y facturación
