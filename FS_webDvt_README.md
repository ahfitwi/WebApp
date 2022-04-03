
# Fullstack Web-APP (FSWA) Dvt --> Skillsets Required

#            -------------------- FSWA = |FE | BE | DB|---------------------------
#### Compiled by Alem Fitwi, Created on Wed Jun 24 18:37:49 2020
##### A FSWDeveloper is one who is often responsible for the E2E development of a fullblown product or a web-app. He is supposed to have the following skillsets, listed 1 through 7.
## 1. Front End (FE) Technologies
   ###### FE is a website where customers directly interact with. It displays data/response in a nice or user-friendly manner.
   ###### FE Stores no data/response; it only displays the data fetched from DB by means of BE in a nice way.
   ###### FE source codes can be accessed and downloaded by anyone who can access the page/FE/website on a any browser.
   ###### FE Skills Required:
   ###### 1.1 **FE/Website Developemnt Technolgies**: HTML, CSS, & JS. A website is developed using these technologies.
   ###### 1.2 **FE Dev't Frameworks**: Angular, React, View, etc: Be well familiar at least with one of them.
   ###### 1.3 **Bootstrape**:makes front-end web development faster and easier. It is the world's most popular front-end open source toolkit made for folks of all skill levels, devices of all shapes, and projects of all sizes. 
   ###### 1.4 **Jquery**: Bootstrap provides components of JavaScript in the form JQuery plugins. JQuery UI contains a library of several pre-written functions. Bootstrap is mainly used to develop responsive web-pages.
   ###### 1.5 **Visualization JS Libraries**: chart.js, DB.js, etc
       
## 2. Back End (BE) Technologies
###### Source Codes are securely stored and can be accessed only by authorized users, not by ordinary customers/users.
###### It serves as a secure communication interface/means between the FE and DB 
###### Majorly exists for security reasons; it has other vital purposes, though.
###### Popular BE Technolgies include:
###### 2.1 Python Stack (Django, Flask, Cherry py, & Pyramid) with python
###### 2.2 Microsoft.NET Stack(asp.net MVC, asp.net WEB API, .net core Web API, & WCF) with C#/VB/F#
###### 2.3 .NET Java Stack (Spring Boot, Spring MVC, and Spring REST) with Java
###### 2.4 PHP, still widely used for website development. It accounts more 35% of current web-devts
###### 2.5 Ruby on Rails
###### 2.6 Javascript backend frameworks: express.js, backbone.js


## 3. Database (DB) Technologies
###### The place where data/actual details about sth are stored systematically and securely.
###### All user data are stored here securely, where the public features/data are accessed by customers by means of the BE.
###### One should be good at:
###### 3.1 SQL Databases (SQLite, MySQL, Maria DB, MS SQL Server, Oracle SQL, ...)
###### Used to organize and store structured data; data organized in the form of Records and Fields.
###### 3.2 NoSQL Databases (mongoDB, neo4j, cassandra, HBASE, ...)
###### NoSQL stores unstructured data; data not organized in the form of rows-columns, obeservations-variables, or records-fields. Image, social-meida data, text data, etc, are typical examples
###### 3.3 Debugging and writting SQL Queries and subqueries, stored procedures, and SQL Functions.

## 4. Object Relational Mapping (ORM) Tools: 
###### JungleORM/SQLAlchemy (Python), Entity Framework (C# & .NET), and Hibernate (Java) 
###### Enables you to interact with the DB Technology in use using a BE programming lamguage of your choice.

## 5. Source/Version Control Software: 
###### It helps keep track of all the changes made to the app under devt by different authorized developers. Besides, it helps create auspicious environment for collaboration with different developers from different organizations or places. Good for collaborative devt of apps. 
###### 5.1 Git along with Github (Github, Enterprise Github, ...)
###### 5.2 CVS: CVS is (old) centralized version control system, while Git is distributed.
###### 5.3 TFS: Team Foundation version Control System (Git and TFS) is a version control tool 

## 6. Mobile App Devt Frameworks: 
###### Swiftic, Native Scripts, AndroidStudio, React Native, Xamarin, Ionic, Sencha Ext JS, OpenSI, Flutter, Corona, and JQuery Mobile 

## 7. DevOps and Agile Methodology.
###### 7.1 DevOps: Devt and operation skills are vital. Dev > Ops > Dev > Ops ...; 
###### Dev = Plan > Code > Build > Test and 
###### Ops = Release > Deploy > Operate > Monitor > Dev ...
###### 7.2 Agile Methodology: Break an app into several deliverable pieces, and maintain communication between the devt team and customer throughout. 
###### Agile:=> Define > Build > Release > Repeat ...

## 8. Development Server vs Production Server
###### 8.1 Development Server: A development server is a type of server that is designed to facilitate the development and testing of programs, websites, software, or applications for software programmers. It provides a run-time environment, as well as all hardware/software utilities that are essential to program debugging and development.

###### 8.2 Production Server: A production server is a type of server that is used to deploy and host live websites or Web applications. It hosts websites and Web applications that have undergone extensive development and testing before they are validated as production ready.A production server is the core server on which any website or Web application is being hosted and accessed by users. It is part of the entire software and application development environment. Typically, the production server environment, hardware and software components are exactly similar to a staging server. Though, rather being confined to in-house usage as in a staging server, the production server is open for end-user access. The software or application must be tested and debugged on a staging server before being deployed on the production server. A production server is a type of server that is used to deploy and host live websites or Web applications. It hosts websites and Web applications that have undergone extensive development and testing before they are validated as production-ready. A production server may also be referred to as a live server.

###### 8.3 WSGI: The Web Server Gateway Interface (WSGI, pronounced whiskey or WIZ-ghee) is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language. It is an interface between web servers and web apps for python. mod_wsgi is an Apache HTTP server module that enables Apache to serve Flask applications.


# ------------------------------------------------------
# Typical Components of a WebApp (FS Python Flask)
# ------------------------------------------------------
FE/Client --> BE/Server --> DB

### 1. schema.sql
$ nano schema.sql

drop table if exists alemtbl;
         create table alemtbl(
                id integer primary key autoincrement,
                name text not null,
                address text not null,
);

### 2. datbase.db
$ sqlite3 database.db < schema.sql

### 3. app.py: a BE/Server App
#### Router/route or an intermediary program
#### It is a good practice to name it as app.py
##### $  pip install flask
##### $  pip install flask_cors
      
      import os
      import sys
      import random
      from flask import Flask
      from flask import render_template, request, jsonify, redirect, url_for, send_file, Response, make_response
      from werkzeug import secure_filename
      from flask_cors import CORS
      
      from models import create_post, get_posts
      
      app = Flask(__name__) # actual server
      
      CORS(app) #security precautions, prevents crosssite scripting, injection, ...
      
      #'/' homepage
      @app.route('/', methods =['GET', 'POST', 'DELETE', ...) # a kind of callback
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
         add.run(debug=True
      
### 4. models.py: 
###### A thin layer or middleware that interfaces the FE with the database through ORM tools
###### It allows us to access the db.

      import sqlite3 as sql
      from os import path
   
      root = path.dirname(path.relpath((__file__))
   
      def create_post(name, address):
         con = sql.connect(path.join(root, 'database.db')
         cur = con.cursor()
         cur.execute('insert into alemtbl (name, address) values(?,?)', (name, address))
         con.commit()
         con.close()
   
      def get_posts():
         con = sql.connect(path.join(root, 'database.db'))
         cur = con.cursor()
         cur.execute("select * from alemtbl")
         posts = cur.fetchall()
         return posts 
   
### 5. template/index.html: 
##### Flask always look for a template folder for html rendering file named index.html

      <!DOCTYPE html>
      <html>
         <!---******************************************************************-->
         <!--- Template/index.html-->
         <!---******************************************************************-->
         <!---Created on Fri Wed Jun 24 17:45:14 2020 @author: alem fitwi --->
         <!---******************************************************************-->

         <body>
               <form action = '/' method = 'post'>
                     <input placeholder = 'Name' name = 'name'>
                     <input placeholder = 'Address' name = 'address'>
                     <input type = 'submit', value = 'Submit'>
               </form>
               
               <!--- Below: Rendering Template, {{python}} --->
               {% for attrib in posts%}
               <div> {{attrib[1] + ': ' + attrib[2] }}</div>
               {%endfor%}
       

         </body>

      </html>
      
### 6. requirements.txt (Added on Apr 02, 2022)
(sn) (base) alem@alem-Legion-S7-15ACH6:~/Documents/projects/sn$ pip freeze

      certifi==2021.10.8
      charset-normalizer==2.0.12
      click==8.0.4
      Flask==2.0.3
      Flask-Cors==3.0.10
      idna==3.3
      importlib-metadata==4.11.3
      itsdangerous==2.1.2
      Jinja2==3.1.1
      MarkupSafe==2.1.1
      numpy==1.21.5
      requests==2.27.1
      six==1.16.0
      typing_extensions==4.1.1
      urllib3==1.26.9
      Werkzeug==2.0.3
      zipp==3.7.0
      
$ pip install -r requirements.txt

# ------------------------------------------------------
# Sample Project: React-FE-UI + Flask-BE + DB
# ------------------------------------------------------
### Project Structure

      projReactFlask/
      |-- api
          |-- config.py
          |-- __init__.py
          |-- models.py
          |-- routes.py
      |-- |-- app.py
      |-- |-- Dockerfile
      |-- |-- README.md
      |-- |-- requirements.txt
      |-- |-- sampleTest.py

### On Linux OS

      mkdir [folder_name] 
      touch [filename, .py, .md, .txt]
      ----------------~END~---------------------
