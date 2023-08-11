from flask_app import app
from flask_app.models.email import Email
from flask import flash, render_template, redirect, request, session


@app.route("/")
def index():
    return render_template("index.html")


@app.post("/validate")
def validate():
    if not Email.validate_email(request.form):
        return redirect("/")

    flash(
        f"The email address you entered ({request.form['email']}) is a VALID email address! Thank you!"
    )

    email_id = Email.create(request.form)
    session["email_id"] = email_id
    return redirect("/success")


@app.route("/success")
def success():
    email = Email.get_one(session["email_id"])
    emails = Email.get_all()
    return render_template("success.html", email=email, emails=emails)


@app.route("/delete/<int:email_id>")
def delete(email_id):
    Email.delete(email_id)
    return redirect("/success")
