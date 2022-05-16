
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

#Load the model
model = joblib.load('model/diabetic80.pkl')
@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/data',methods=['post'])
def Data():
    Preg = request.form.get("preg")
    Plas = request.form.get("plas")
    Pres = request.form.get("pres")
    Skin = request.form.get("skin")
    Test = request.form.get("test")
    Mass = request.form.get("mass")
    Pedi = request.form.get("pedi")
    Age = request.form.get("age")

    result = model.predict([[Preg,Plas,Pres,Skin,Test,Mass,Pedi,Age]])

    if result[0] == 0:
        data = "The person is diabetic"
    
    else:
        data = "The person is not diabetic"
    
    print(data)


    return data


app.run(debug = True)
