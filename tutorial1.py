from flask import Flask, redirect, url_for

app = Flask(__name__)

a = False

@app.route("/")
def home():
  return "Hello, this is the main page<h1> Hello world!!</h1>"

@app.route("/<name>")
def user(name):
  return f"Hello {name}!"

@app.route("/admin")
def admin():
  if not a:
    return redirect(url_for("home"))
  return "Hello <h1>ADMIN!!</h1>"

if __name__ == "__main__":
  app.run(debug=True)
