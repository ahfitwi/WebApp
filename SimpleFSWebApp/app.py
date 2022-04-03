import os
import sys
import random
from flask import Flask
from flask import render_template, request, jsonify, redirect, url_for, send_file, Response, make_response
#from werkzeug import secure_filename
from flask_cors import CORS

#Program defined modules/methods
from models import create_post, get_posts



#sys.path.append("apis")
	#import settings



# Create the app   
app = Flask(__name__) # actual server
CORS(app) #security precautions, prevents crosssite scripting, injection, ...
    
#'/' homepage
@app.route('/', methods =['GET', 'POST']) # a kind of callback
 #router, @app.route('/home'), @app.route('/login') ...
      
def index():

    if request.method == 'GET':
        pass
    
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        create_post(name, address)

    posts = get_posts()

    return render_template("index.html", posts = posts)
         
      
if __name__ == '__main__':
 	app.run(debug=True)
 	#whip pip
