from flask import Flask, render_template, request, g
import time


app = Flask(__name__)


@app.route("/")
def home():
    g.error_fields = []
    return render_template("base.html", fields={})


@app.route("/sleep")
def nap():
    time.sleep(1)
    return """
    <script type="module">
        let info = await browser.runtime.getBrowserInfo()
        console.log("I'm in yoir console scripting yur java", info)
    </script>"""


@app.template_global()
def error_class(field_name):
    return "text-red-500" if field_name in g.get("error_fields") else ""


@app.route("/", methods=["POST"])
def process():
    error_messages = []
    error_fields = []
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")
    password = request.form.get("password")
    password_confirmation = request.form.get("password_confirmation")
    marketing_accept = request.form.get("marketing_accept")
    print(marketing_accept)

    if not marketing_accept:
        error_messages.append("fuck u, read our shit")
        error_fields.append("marketing")

    if not first_name:
        error_messages.append("you need a first name bruv")
        error_fields.append("first_name")

    # Process the form data here
    error_message = "\n".join(f"<div>{message}</div>" for message in error_messages)
    g.error_fields = error_fields
    return render_template(
        "base.html",
        error_message=error_message,
        error_fields=error_fields,
        fields={"first_name": first_name, "marketing_accept": marketing_accept},
    )


if __name__ == "__main__":
    app.run(debug=True)
