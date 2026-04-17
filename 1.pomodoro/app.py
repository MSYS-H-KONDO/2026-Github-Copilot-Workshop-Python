from flask import Flask, render_template


def create_app() -> Flask:
	app = Flask(__name__, template_folder="templates", static_folder="static")

	@app.get("/")
	def index() -> str:
		return render_template("index.html")

	return app


app = create_app()


if __name__ == "__main__":
	app.run(debug=True)
