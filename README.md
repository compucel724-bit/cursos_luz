# Portal de Biblioteca

Aplicación web desarrollada con Python y Flask para simular el acceso de usuarios a un portal de biblioteca.

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

Luego abrir `http://127.0.0.1:5000` en el navegador.

## Usuarios de prueba

| Usuario | Contraseña |
| --- | --- |
| carlos | 1111 |
| laura | 2222 |
| diego | 3333 |

## Funcionalidades

- Inicio de sesión con sesiones de Flask.
- Protección de la ruta `/perfil`.
- Catálogo dinámico de libros con Jinja2.
- Cookie `ultimo_usuario` y opción para eliminarla.
- Cierre de sesión.

El entorno virtual está excluido del repositorio mediante `.gitignore`.
