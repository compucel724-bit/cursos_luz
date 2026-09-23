# Portal Académico

Aplicación web desarrollada con Python y Flask para simular el acceso de estudiantes a un portal académico.

## Requisitos

- Python 3.10 o superior
- Flask

## Instalación y ejecución en Windows

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install Flask
python app.py
```

Luego abrir http://127.0.0.1:5000 en el navegador.

## Usuarios de prueba

| Usuario | Contraseña |
| --- | --- |
| juan | 1234 |
| maria | abcd |
| pedro | 2026 |

## Funcionalidades

- Inicio de sesión con sesiones de Flask.
- Protección de la ruta `/perfil`.
- Listado dinámico de cursos con Jinja2.
- Cookie `usuario_preferido` y opción para eliminarla.
- Cierre de sesión.

El entorno virtual está excluido del repositorio mediante `.gitignore`.
