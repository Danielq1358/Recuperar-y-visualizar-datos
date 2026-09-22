from flask import Flask, redirect, render_template, request, url_for

from mascota import Mascota

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    mascotas = Mascota.get_all()
    return render_template(
        "index.html",
        mascotas=mascotas,
        mascota_editar=None,
    )


@app.route("/crear", methods=["POST"])
def crear_mascota():
    data = {
        "nombre": request.form["nombre"],
        "tipo": request.form["tipo"],
        "color": request.form["color"],
    }
    Mascota.save(data)
    return redirect(url_for("index"))


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar_mascota(id):
    mascota = Mascota.get_by_id(id)
    if request.method == "POST":
        mascota.nombre = request.form["nombre"]
        mascota.tipo = request.form["tipo"]
        mascota.color = request.form["color"]
        mascota.update()
        return redirect(url_for("index"))

    mascotas = Mascota.get_all()
    return render_template("index.html", mascotas=mascotas, mascota_editar=mascota)


@app.route("/eliminar/<int:id>")
def eliminar_mascota(id):
    Mascota.delete(id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
