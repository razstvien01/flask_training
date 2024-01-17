"""
* Blueprints
* Allows us to divide our application into separate Python files where we can actually pass specific views and render templates from different areas of our kind of project and application
"""
from flask import Flask, render_template
from admin.second import second

app = Flask(__name__)

# * Url prefix is what needs to come first to send something to that blueprint
app.register_blueprint(second, url_prefix="/admin")

@app.route("/")
def test():
  return "<h1>Test</h1>"

if __name__ == "__main__":
  app.run(debug=True)