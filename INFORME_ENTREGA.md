# EXAMEN PRACTICO
## Desarrollo de Aplicaciones Web con Flask

### Sistema: Portal de Biblioteca

**Estudiante:** [ESCRIBE AQUI TU NOMBRE COMPLETO]

**Materia:** Tecnologias Emergentes II

**Docente:** M. Sc. Mario Torrez C.

**Fecha:** 22 de septiembre de 2026

---

## 1. URL del repositorio en GitHub

El codigo fuente completo se encuentra disponible en el siguiente repositorio:

**https://github.com/brayanzuniga044/portal-biblioteca**

El repositorio contiene la aplicacion Flask, las plantillas HTML, los estilos CSS, el archivo README.md y el archivo .gitignore.

---

## 2. Descripcion general de la aplicacion

El Portal de Biblioteca es una aplicacion web desarrollada con Python y Flask. Permite iniciar sesion con usuarios registrados, consultar un catalogo de libros, visualizar el perfil del usuario autenticado y cerrar la sesion.

La aplicacion utiliza rutas Flask, plantillas Jinja2, sesiones, cookies y control de versiones con Git.

---

## 3. Estructura del proyecto

```text
portal_biblioteca/
|-- app.py
|-- README.md
|-- .gitignore
|-- venv/                  (no se sube a GitHub)
|-- templates/
|   |-- base.html
|   |-- index.html
|   |-- login.html
|   |-- libros.html
|   `-- perfil.html
`-- static/
    `-- style.css
```

---

## 4. Entorno virtual

Se creo un entorno virtual para aislar las dependencias del proyecto.

Comandos utilizados en Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install Flask
python app.py
```

La aplicacion se ejecuto utilizando el interprete ubicado en:

```text
D:\carrito_plus\venv\Scripts\python.exe
```

**Evidencia del entorno virtual:**

[INSERTAR AQUI CAPTURA DE POWERShell mostrando el entorno activado y Flask instalado]

---

## 5. Rutas implementadas

| Ruta | Funcion |
|---|---|
| `/` | Muestra la pagina principal. |
| `/login` | Muestra y procesa el formulario de inicio de sesion. |
| `/libros` | Muestra el catalogo de libros. |
| `/perfil` | Muestra el usuario autenticado. |
| `/logout` | Cierra la sesion y vuelve al inicio. |
| `/eliminar-cookie` | Elimina la cookie del ultimo usuario. |

**Evidencia de la pagina principal:**

[INSERTAR AQUI CAPTURA DE LA pagina principal]

---

## 6. Inicio de sesion y sesiones

Se definieron los siguientes usuarios de prueba:

```python
usuarios = {
    "carlos": "1111",
    "laura": "2222",
    "diego": "3333"
}
```

Cuando las credenciales son correctas:

1. El nombre del usuario se guarda en la sesion.
2. El usuario es redirigido a `/libros`.
3. Se muestra un mensaje de bienvenida.
4. Se guarda la cookie `ultimo_usuario`.

Cuando las credenciales son incorrectas se muestra el mensaje:

> Usuario o contraseña incorrectos.

La ruta `/perfil` esta protegida. Si una persona no ha iniciado sesion, es redirigida a `/login`.

**Evidencias de inicio de sesion:**

- [INSERTAR CAPTURA DEL formulario de login]
- [INSERTAR CAPTURA DEL login correcto y mensaje de bienvenida]
- [INSERTAR CAPTURA DEL perfil de usuario]
- [INSERTAR CAPTURA DEL acceso rechazado al perfil sin iniciar sesion]

---

## 7. Uso de Jinja2

La lista de libros se definio en `app.py`:

```python
libros = [
    {"titulo": "Python desde cero", "autor": "Juan Pérez", "disponibles": 4},
    {"titulo": "Desarrollo Web", "autor": "María López", "disponibles": 2},
    {"titulo": "Inteligencia Artificial", "autor": "Pedro García", "disponibles": 0}
]
```

La plantilla `libros.html` utiliza:

- `{% extends "base.html" %}` para heredar la plantilla base.
- `{% for libro in libros %}` para recorrer los libros.
- `{% if libro.disponibles > 0 %}` para mostrar la disponibilidad.

Los libros disponibles muestran la cantidad de ejemplares. El libro sin ejemplares muestra el mensaje `No disponible`.

**Evidencia del catalogo:**

[INSERTAR AQUI CAPTURA DE LA pagina de libros mostrando los tres libros]

---

## 8. Uso de cookies

Al iniciar sesion correctamente se crea una cookie llamada `ultimo_usuario`, cuyo valor corresponde al nombre del usuario.

En la pagina principal se muestra:

- `Último usuario registrado: [usuario].` cuando existe la cookie.
- `Bienvenido al Portal de Biblioteca.` cuando no existe la cookie.

Tambien se implemento una opcion para eliminar la cookie.

**Evidencia de la cookie:**

[INSERTAR AQUI CAPTURA DE LA pagina principal mostrando el ultimo usuario registrado]

---

## 9. Cierre de sesion

La ruta `/logout` elimina los datos guardados en la sesion, redirige a la pagina principal y muestra el mensaje:

> La sesión fue cerrada correctamente.

**Evidencia del cierre de sesion:**

[INSERTAR AQUI CAPTURA DEL mensaje de sesion cerrada]

---

## 10. Evidencia de Git

El proyecto fue controlado mediante Git y contiene los siguientes commits significativos:

```text
c55dc72 Implementa rutas del portal
8a85446 Implementa navegacion y pagina principal
89968c0 Implementa sesiones y catalogo Jinja
e1faa22 Agrega estilos del portal
de2aba1 Simplifica estilos del portal
ed26ef3 Actualiza titulo de la biblioteca
```

Comandos utilizados para revisar el historial:

```powershell
git log --oneline
git status
git remote -v
git push -u origin main
```

El repositorio remoto utilizado es:

```text
https://github.com/brayanzuniga044/portal-biblioteca.git
```

**Evidencia de Git:**

[INSERTAR AQUI CAPTURA DE PowerShell mostrando git log --oneline]

[INSERTAR AQUI CAPTURA DEL repositorio en GitHub]

El archivo `.gitignore` evita subir el entorno virtual mediante la siguiente linea:

```text
venv/
```

---

## 11. Conclusion

Se desarrollo un Portal de Biblioteca funcional con Flask. La aplicacion cumple con el uso de entorno virtual, ruteo, plantillas Jinja2, sesiones, cookies, proteccion de rutas, cierre de sesion y control de versiones con Git y GitHub.
