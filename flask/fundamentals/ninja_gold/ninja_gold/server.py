import random
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "f892f4210b534fe545d76d872d3b7c6dd504b041bbf8d982d336dfdbf752be13"


@app.route("/")
def index():
    """
    Set session keys for 'gold', 'activity', and 'disabled' for buttons
    """
    if "gold" not in session:
        session["gold"] = 0
        session["activity"] = []
        session["disabled"] = None
    return render_template("index.html")


@app.route("/process_money", methods=["POST"])
def process_money():
    building = request.form["building"]
    if building == "farm":
        add_gold = random.randint(10, 20)
        session["activity"].append(f"Earned {add_gold} gold from the farm!")
    elif building == "cave":
        add_gold = random.randint(5, 10)
        session["activity"].append(f"Earned {add_gold} gold from the cave!")
    elif building == "house":
        add_gold = random.randint(2, 5)
        session["activity"].append(f"Earned {add_gold} gold from the house!")
    elif building == "casino":
        add_gold = random.randint(-50, 50)
        if add_gold < 0:
            session["activity"].append(
                f"Entered a casino and lost {abs(add_gold)} gold...Ouch!"
            )
        elif add_gold == 0:
            session["activity"].append(f"Entered a casino and neither won or lost gold")
        else:
            session["activity"].append(f"Entered a casino and won {add_gold} gold!")

    session["gold"] += add_gold

    if len(session["activity"]) == 15:
        session["disabled"] = "disabled"

    return redirect("/")


@app.route("/reset")
def reset():
    session.clear()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
