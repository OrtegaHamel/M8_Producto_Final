# Cartelera Música en Vivo
Por Álvaro Ortega Hamel

### Proyecto final del Bootcamp FullStack Python.

------------------------------------------------------------------------

## 🎯 Identificación de la problemática

En muchos locales nocturnos que ofrecen música en vivo, la gestión de
eventos suele realizarse de manera manual o desorganizada, dificultando
la comunicación, la actualización de información y la coordinación con
bandas y productores. Para resolver esta necesidad, se desarrolló una
aplicación web que permite administrar música en vivo de forma eficiente
mediante la creación, visualización, actualización y eliminación de
eventos según los permisos del usuario.

Además, se ofrece un **home público** diseñado para mostrar la cartelera
de manera atractiva. Este home puede integrarse fácilmente a la página
web del local si ya existe, o servir como página principal en caso de
que no cuenten con una, realizando los ajustes de diseño y hosting
necesarios.

## 🛠️ Proceso de desarrollo

El desarrollo comenzó con una fase de planificación, donde se definieron
el alcance del proyecto, los tipos de usuarios y los permisos necesarios
para cada uno. Se buscó construir una herramienta clara, eficiente y
adaptable a distintos locales o centros culturales.

Para mantener el código ordenado y escalable, el sistema se estructuró
de manera **modular**, dividido en tres aplicaciones independientes:\
- **usuarios**\
- **bandas**\
- **eventos**

A partir de esta planificación, se diseñó la arquitectura del sistema
siguiendo buenas prácticas de desarrollo, incluyendo: - Controladores
separados por funcionalidad\
- Reutilización de componentes\
- Estructura clara de rutas\
- Vistas organizadas y coherentes

El despliegue se realizó en Render, utilizando una base de datos PostgreSQL externa (Neon) para garantizar persistencia. Se configuró el manejo de archivos estáticos, las variables de entorno y el servidor Gunicorn. También se automatizaron las migraciones y la creación del superusuario inicial para facilitar la puesta en marcha del sistema.

Probé todas las rutas de usuario, el inicio de sesión, los permisos y la edición de eventos para asegurar que el flujo fuera consistente y sin errores. Ajusté detalles de validación, mensajes de error y visualización de datos.

El proceso contempló las etapas del ciclo de vida del software:
planificación, diseño, implementación, pruebas y despliegue.

------------------------------------------------------------------------

## 💻 Tecnologías utilizadas

-   **Backend:** Python, Django\
-   **Frontend:** HTML, CSS, JavaScript\
-   **Base de datos:** PostgreSQL con Neon como servicio externo\
-   **Entorno y despliegue:** ender, utilizando Gunicorn como servidor WSGI y Whitenoise para servir archivos estáticos\
-   **Control de versiones:** GitHub para manejo estructurado del proyecto y despliegue continuo.

Estas tecnologías fueron seleccionadas por su solidez, compatibilidad y
presencia en la industria del desarrollo web.

------------------------------------------------------------------------

## 📦 Estructura del proyecto

M8_Producto_Final/
├── gestion_musica/        # Proyecto principal (settings, urls, wsgi)
├── usuarios/              # App para registro, login y permisos
├── bandas/                # App para gestionar bandas
├── eventos/               # App para gestionar eventos y cartelera
├── static/                # Archivos estáticos (CSS, JS, imágenes)
├── templates/             # Plantillas HTML compartidas
├── createsu.py (eliminado luego del deploy)
├── manage.py
├── Procfile
├── requirements.txt
└── README.md

------------------------------------------------------------------------

## 🚀 Despliegue

## 🖥️ Ejecutar el proyecto en local

### 1. Clonar el repositorio

``` bash
git clone https://github.com/OrtegaHamel/M8_Producto_Final.git
cd M8_Producto_Final
```

### 2. Crear entorno virtual

``` bash
python -m venv venv
source venv/Scripts/activate   # Windows
source venv/bin/activate       # Mac/Linux
```

### 3. Instalar dependencias

``` bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

-   Crear archivo `.env` (si fuera necesario).
-   Configurar base de datos local (SQLite o PostgreSQL según
    prefieras).

### 5. Aplicar migraciones

``` bash
python manage.py migrate
```

### 6. Crear superusuario

``` bash
python manage.py createsuperuser
```

### 7. Levantar servidor

``` bash
python manage.py runserver
```

Ahora puedes entrar en:

👉 http://127.0.0.1:8000\
👉 http://127.0.0.1:8000/admin (para administración)

------------------------------------------------------------------------

## 🌐 Ver el proyecto en Render

El proyecto está desplegado en Render con:

-   PostgreSQL administrado por Render\
-   Gunicorn como servidor de producción\
-   Procfile para levantar la aplicación

### 🔧 Configuración usada en Render

**Start Command (en Render Dashboard):**

``` bash
python manage.py migrate && gunicorn gestion_musica.wsgi --bind 0.0.0.0:$PORT
```

Puedes acceder al sitio desplegado en:

👉 https://cartelera-musica.onrender.com


## 🔑 Usuarios Creados

Ya existen dos usuarios de prueba, organizados en grupos con permisos distintos:

| Usuario | Contraseña | Grupo | Permisos |
| :--- | :--- | :--- | :--- |
| **administrador1** | `contrasena123` | Administradores | Acceso total a todo el sistema |
| **basico1** | `contrasena123` | Básico | Puede ver, pero no modificar información |

---

**Recordatorio:** Además de estos, creaste el **superusuario** con credenciales **`root` / `root`** para la administración de Django.


------------------------------------------------------------------------

## 📌 Estado del proyecto

Versión estable inicial, con CRUD completo para eventos, permisos por
usuario y visualización pública de la cartelera.

------------------------------------------------------------------------

## MIT License

Copyright (c) 2025 Álvaro Ortega Hamel

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
IN THE SOFTWARE.
