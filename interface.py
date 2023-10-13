from flask import Flask, render_template, jsonify, request, url_for, redirect

import config

from project_data.utils import MedicalInsurance

app = Flask(__name__)

##########################################################################################
##################################    HOME API     #######################################
##########################################################################################

@app.route('/')
def main_home():
    print('Medical Indsurance project')
    return render_template ('login.html')

@app.route('/result/int : <name>')
def result(name):
    return f'Hello {name} you are in result API'

# @app.route('/login', methods = ['POST','GET'])
# def login():
#     if request.method == "POST":
#         data = request.form
#         name = data["name"]
#         print("In Login API")
#         print("NAme:",name)
#         return redirect(url_for('result',name = name))
    
#     if request.method == 'GET':
#         name = request.args.get("name")
#         print("Name:",name)
#         return redirect(url_for('result',name = name))


@app.route('/charges')
def insurance_charges():

    user_data = request.form
    
    # age = 25  
    # sex = 'male'
    # bmi = 28.3
    # children = 1
    # smoker = 'yes'
    # region = 'southeast'

    print("age,sex,bmi,children,smoker,region >>",age,sex,bmi,children,smoker,region)
    
    med_ins = MedicalInsurance(age, sex, bmi, children, smoker, region)
    charges = med_ins.get_predict_charges()
    
    return jsonify({'Result' : f'The predicted insurance charges is {charges}'})


app.run(port = config.PORT_NUMBER, debug = True)