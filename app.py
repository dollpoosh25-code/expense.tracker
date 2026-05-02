from flask import Flask, render_template, request, redirect

app = Flask(__name__)

expenses = []

# Load data
try:
    file = open("expenses.txt", "r")
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 3:
            amount, category, date = parts
            expenses.append((float(amount), category, date))
    file.close()
except:
    pass


@app.route("/")
def home():
    total = sum(exp[0] for exp in expenses)
    return render_template("index.html", expenses=expenses, total=total)


@app.route("/add", methods=["POST"])
def add():
    amount = float(request.form["amount"])
    category = request.form["category"]
    date = request.form["date"]

    expenses.append((amount, category, date))

    file = open("expenses.txt", "a")
    file.write(str(amount) + "," + category + "," + date + "\n")
    file.close()

    return redirect("/")


@app.route("/delete/<int:index>")
def delete(index):
    if index < len(expenses):
        expenses.pop(index)

    file = open("expenses.txt", "w")
    for exp in expenses:
        file.write(str(exp[0]) + "," + exp[1] + "," + exp[2] + "\n")
    file.close()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=5001) 