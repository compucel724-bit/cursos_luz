from flask import Flask, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = "clave-secreta-biblioteca"

usuarios = {
    "carlos": "1111",
    "laura": "2222",
    "diego": "3333"
}

libros = [
    {"titulo": "Python desde cero", "autor": "Juan Pérez", "disponibles": 4},
    {"titulo": "Desarrollo Web", "autor": "María López", "disponibles": 2},
    {"titulo": "Inteligencia Artificial", "autor": "Pedro García", "disponibles": 0}
]

@app.route("/")
def index():
    return render_template("index.html", ultimo_usuario=request.cookies.get("ultimo_usuario"))

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        contrasena = request.form.get("contrasena", "")

        if usuarios.get(usuario) == contrasena:
            session["usuario"] = usuario
            respuesta = redirect(url_for("libros_disponibles"))
            respuesta.set_cookie("ultimo_usuario", usuario)
            flash(f"Bienvenido, {usuario}.", "success")
            return respuesta

        flash("Usuario o contraseña incorrectos.", "error")

    return render_template("login.html")

@app.route("/libros")
def libros_disponibles():
    return render_template("libros.html", libros=libros)

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
    respuesta.delete_cookie("ultimo_usuario")
    return respuesta

if __name__ == "__main__":
    app.run(debug=True)