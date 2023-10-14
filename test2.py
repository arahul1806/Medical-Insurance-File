from flask import Flask, jsonify, request

app = Flask(__name__)

####################################################################################
########################             Home API              #########################
####################################################################################

@app.route('/home')
def my_fun():
    print('Hello Flask')
    return 'Welcome to Flask'

####################################################################################
####################             Testing API                   #####################
####################################################################################


@app.route('/test')
def test():
    print('Testing TEST API')
    return 'Testing API'

####################################################################################
####################            Testing Variable API           #####################
####################################################################################

@app.route('/name/<name>')
def user_name(name):
    print('User name is :',name)
    return jsonify({'Name of User is ' : name})

####################################################################################
####################      Testing input Variable integer API   #####################
####################################################################################

@app.route('/marks/<int:marks>')
def user_marks(marks):
    print('Marks is :',marks)
    return jsonify({'Message' : f'Marks of User is {marks}'})

####################################################################################
####################            Addition API                   #####################
####################################################################################

@app.route("/addition")
def addition():
    data = request.form
    print("Data >>>>",data)   #ImmutableMultiDict([('a', '222'), ('b', '333')])
    x = int(data["p"])
    y = int(data['q'])
    add = x+y
    return jsonify({"Message": f"Addition is {add}"})

##########################################################################################
#########################    Multiplication API  #########################################
##########################################################################################

@app.route("/multiplication")
def multiplication():
    data = request.get_json()
    print("Data >>>>",data)   
    a = int(data["a"])
    b = int(data['b'])
    multi = a*b
    return jsonify({"Message": f"Multiplication is {multi}"})

app.run()