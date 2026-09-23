from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "clave-secreta-portal-academico"

usuarios = {
    "juan": "1234",
    "maria": "abcd",
    "pedro": "2026"
}

cursos = [
    {"nombre": "Programación Web", "docente": "Luis Pérez", "cupos": 15},
    {"nombre": "Bases de Datos", "docente": "Ana López", "cupos": 8},
    {"nombre": "Inteligencia Artificial", "docente": "Carlos Rojas", "cupos": 0}
]


@app.route("/")
def index():
    usuario_preferido = request.cookies.get("usuario_preferido")
    if usuario_preferido:
        mensaje = f"Bienvenido nuevamente, {usuario_preferido}."
    else:
        mensaje = "Bienvenido al Portal Académico."
    return render_template("index.html", mensaje=mensaje, usuario_preferido=usuario_preferido)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        contrasena = request.form.get("contrasena", "")

        if usuarios.get(usuario) == contrasena:
            session["usuario"] = usuario
            respuesta = redirect(url_for("cursos_disponibles"))
            respuesta.set_cookie("usuario_preferido", usuario)
            flash(f"Bienvenido, {usuario}.", "success")
            return respuesta

        flash("Usuario o contraseña incorrectos.", "error")

    return render_template("login.html")


@app.route("/cursos")
def cursos_disponibles():
    return render_template("cursos.html", cursos=cursos)


@app.route("/libros")
def libros_disponibles():
    return redirect(url_for("cursos_disponibles"))


@app.route("/perfil")
def perfil():
    if "usuario" not in session:
        flash("Debes iniciar sesión para ver tu perfil.", "error")
        return redirect(url_for("login"))

    return render_template("perfil.html", usuario=session["usuario"])


@app.route("/logout")
def logout():
    session.clear()
    flash("La sesión fue cerrada correctamente.", "success")
    return redirect(url_for("index"))


@app.route("/eliminar-cookie")
def eliminar_cookie():
    respuesta = redirect(url_for("index"))
    respuesta.delete_cookie("usuario_preferido")
    return respuesta


if __name__ == "__main__":
    app.run(debug=True)