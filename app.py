from flask import Flask, render_template, request

app = Flask(__name__)

OPERATORS = {"+", "-", "*", "/"}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/math", methods=["POST"])
def math():
    # test user input
    try:
        left_num = float(request.form.get("left-num"))
        right_num = float(request.form.get("right-num"))
    except ValueError:
        return render_template("fail.html", reason="Please enter two valid numbers.")

    # ensure user uses valid operator
    operator = request.form.get("operator")
    if operator not in OPERATORS:
        return render_template("fail.html", reason="Please use a valid operator.")

    # math cases
    result = None
    match operator:
        case "+":
            result = left_num + right_num
        case "-":
            result = left_num - right_num
        case "*":
            result = left_num * right_num
        case "/":
            try:
                result = left_num / right_num
            except ZeroDivisionError:
                return render_template("fail.html", reason="Cannot divide by 0.")

    # if no exceptions met, return success html with result
    return render_template("success.html", result=result)