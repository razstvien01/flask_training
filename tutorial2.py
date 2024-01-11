from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

a = False

@app.route("/<name>")
def home(name):
  # return render_template("index.html", content=name, r=2)
  return render_template("index.html", content=["nico", "evanz", "nics"])

# @app.route("/<name>")
# def user(name):
#   return f"Hello {name}!"

# @app.route("/admin")
# def admin():
#   if not a:
#     return redirect(url_for("user", name="Nicolen"))
#   return "Hello <h1>ADMIN!!</h1>"

if __name__ == "__main__":
  app.run(debug=True)
