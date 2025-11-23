from flask import Flask, render_template, request, redirect, url_for
import joblib

# Load the trained model and scaler
model = joblib.load('hypertension_model.pkl')

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get form values
        Age = float(request.form['age'])
        Salt_Intake = float(request.form['Salt_Intake'])
        Stress_Score = float(request.form['Stress_Score'])
        BP_History = float(request.form['BP_History'])
        Sleep_Duration = float(request.form['Sleep_Duration'])
        BMI = float(request.form['BMI'])
        Medication = float(request.form['Medication'])
        Family_History = float(request.form['Family_History'])
        Exercise_Level = float(request.form['Exercise_Level'])
        Smoking_Status = float(request.form['Smoking_Status'])

        # Prepare and scale data
        data = [[Age, Salt_Intake, Stress_Score, BP_History, Sleep_Duration,
                 BMI, Medication, Family_History, Exercise_Level, Smoking_Status]]
                 
        # Predict
        result = model.predict(data)[0]

        # Redirect with output in query string
        return redirect(url_for('result', output=result))

    return render_template("index.html")

@app.route("/result")
def result():
    # Get prediction from query parameter
    output = int(request.args.get('output'))
    return render_template("result.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
