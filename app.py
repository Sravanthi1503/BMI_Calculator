from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    advice = ""
    if request.method == "POST":
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        bmi = round(weight / (height ** 2), 2)
        if bmi < 18.5:
            advice = "Underweight – Focus on a calorie-rich, nutritious diet."
        elif 18.5 <= bmi < 24.9:
            advice = "Normal weight – Maintain with balanced diet and regular exercise."
        elif 25 <= bmi < 29.9:
            advice = "Overweight – Add more activity and watch portion sizes."
        else:
            advice = "Obese – Seek guidance from a health professional."
    return render_template("index.html", bmi=bmi, advice=advice)

if __name__ == "__main__":
    app.run(debug=True)