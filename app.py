# TODO Redirect page requests to serve the actual pages.
# TODO Create API endpoints for facebook and google classroom announcements.

from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder="./frontend/src/templates",
    static_folder="frontend/build"
)

@app.route("/")
def index():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)