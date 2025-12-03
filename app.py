from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Dossier où les fichiers seront stockés
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return "Aucun fichier reçu."

        fichier = request.files["file"]

        if fichier.filename == "":
            return "Aucun fichier sélectionné."

        # Sauvegarde du fichier
        chemin = os.path.join(app.config["UPLOAD_FOLDER"], fichier.filename)
        fichier.save(chemin)

        return f"Fichier '{fichier.filename}' bien installé !"

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)
