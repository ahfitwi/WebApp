### 2.1 Introduction
- **What is Django?**
  - Django is a Python framework that makes it easier to create web sites using Python.
  - Django takes care of the difficult stuff so that you can concentrate on building your web applications.
  - Django emphasizes reusability of components, also referred to as DRY (Don't Repeat Yourself), and comes with ready-to-use features like login system, database connection and CRUD operations (Create Read Update Delete).
- ***Django is especially helpful for database driven websites***.
- ***How does Django Work?***:
  - Django follows the MVT design pattern (Model View Template).
      - **Model** - The data you want to present, usually data from a database.
      - **View** - A request handler that returns the relevant template and content - based on the request from the user.
      - **Template** - A text file (like an HTML file) containing the layout of the web page, with logic on how to display the data.
  - **Model: models.py**
    - The model provides data from the database.
      - In Django, the data is delivered as an Object Relational Mapping (ORM), which is a technique designed to make it easier to work with databases.
      - The most common way to extract data from a database is SQL. One problem with SQL is that you have to have a pretty good understanding of the database structure to be able to work with it.
      - Django, with ORM, makes it easier to communicate with the database, without having to write complex SQL statements.
      - The models are usually located in a file called models.py
  - **View: views.py**: 
    - A view is a function or method that takes http requests as arguments, imports the relevant model(s), and finds out what data to send to the template, and returns the final result.
    - The views are usually located in a file called views.py.
  - **Template: templates.py**
    - A template is a file where you describe how the result should be represented.
    - Templates are often .html files, with HTML code describing the layout of a web page, but it can also be in other file formats to present other results, but we will concentrate on .html files.
    - Django uses standard HTML to describe the layout, but uses Django tags to add logic:

            <h1>My Homepage</h1>
            <p>My name is {{ firstname }}.</p>
    - The templates of an application is located in a folder named templates.
  - **URLs: urls.py**:
    - Django also provides a way to navigate around the different pages in a website.
    - When a user requests a URL, Django decides which view it will send it to.
    - This is done in a file called urls.py.
- **So, What is Going On?**
  - When you have installed Django and created your first Django web application, and the browser requests the URL, this is basically what happens:
  - Django receives the URL, checks the urls.py file, and calls the view that matches the URL.
  - The view, located in views.py, checks for relevant models.
  - The models are imported from the models.py file.
  - The view then sends the data to a specified template in the template folder.
  The template contains HTML and Django tags, and with the data it returns finished HTML content back to the browser.
  - Django can do a lot more than this, but this is basically what you will learn in this tutorial, and are the basic steps in a simple web application made with Django.
- **Django History**:
  - Django was invented by Lawrence Journal-World in 2003, to meet the short deadlines in the newspaper and at the same time meeting the demands of experienced web developers.
  - Initial release to the public was in July 2005.
  - Latest version of Django is 4.0.3 (March 2022).

### 2.2 Getting Started
- To install Django, you must have Python installed, and a package manager like **PIP**.
  - pip Install Packages
- PIP is included in Python from version 3.4.
- To check if your system has Python installed, run this command in the command prompt:
  - python --version
    - python 3.10.6
- To install Django, you must use a package manager like PIP, which is included in Python from version 3.4. To check if your system has PIP installed, run this command in the command prompt:
- sudo apt install python3-pip
  - pip --version
    - pip 22.0.2 from /usr/lib/python3/dist-packages/pip (python 3.10)

### 2.3 Virtual Environment (venv)
- It is suggested to have a dedicated virtual environment for each Django project, and in the next chapter you will learn how to create a virtual environment, and then install Django in it.
- Windows:
  - y -m venv myworld
  - myworld\Scripts\activate.bat
- Unix/MacOS:
  - python -m venv myworld
  - source myworld/bin/activate
  
### 2.4 Installing Django
- Now, that we have created a virtual environment, we are ready to install Django.
- Note: Remember to install Django while you are in the virtual environment!
- Django is installed using pip, with this command:
  - (venv) C:\Users\Your Name>py -m pip install Django
  - (venv) C:\Users\Your Name>python3 -m pip install Django
  - django-admin --version : --> 4.1.7
  
### 2.5 Create Project
- Once you have come up with a suitable name for your Django project, myDjango, navigate to where in the file system you want to store the code (in the virtual environment), and run this command in the command prompt:
  - django-admin startproject myDjango
  - Django creates a my_tennis_club folder on my computer, with this content:

          myDjango
              manage.py
              myDjango/
                  __init__.py
                  asgi.py
                  settings.py
                  urls.py
                  wsgi.py
- Run the Django Project
  - Now that you have a Django project, you can run it, and see what it looks like in a browser.
  - Navigate to the /myDjango folder and execute this command in the command prompt:
    - py manage.py runserver
      - Open a new browser window and type 127.0.0.1:8000 in the address bar.
  
### 2.6 Create App
- An app is a web application that has a specific meaning in your project, like a home page, a contact form, or a members database.
- In this tutorial we will create an app that allows us to list and register members in a database.
- But first, let's just create a simple Django app that displays "Hello World!".
- I will name my app members.
- Start by navigating to the selected location where you want to store the app, in my case the myDjango folder, and run the command below.
  - python manage.py startapp members
- If the server is still running, and you are not able to write commands, press [CTRL] [BREAK], or [CTRL] [C] to stop the server and you should be back in the virtual environment.
- (webapp) alem@alem-Legion-S7-15ACH6:/media/alem/a325a2da-4efe-42fb-acad-1f982e1f6eb7/SE/myDjango/members$ ls
- 
                        admin.py  
                        apps.py  
                        __init__.py  
                        migrations  
                        models.py  
                        tests.py  
                        views.py
- These are all files and folders with a specific meaning. You will learn about most of them later in this tutorial.
- 
### 2.7 Views
- Django views are Python functions that takes http requests and returns http response, like HTML documents.
- A web page that uses Django is full of views with different tasks and missions.
- Views are usually put in a file called views.py located on your app's folder.
- There is a views.py in your members folder that looks like this:
  - myDjango/members/views.py:

        from django.shortcuts import render
        #Create your views here.
        
        Find it and open it, and replace the content with this:
          from django.shortcuts import render
          from django.http import HttpResponse

          def members(request):
              return HttpResponse("Hello world!")
  - Note: The name of the view does not have to be the same as the application.
  - I call it members because I think it fits well in this context.
  - This is a simple example on how to send a response back to the browser.
  - But how can we execute the view? Well, we must call the view via a URL.
  - 
### 2.8 Urls
- Create a file named urls.py in the same folder as the views.py file, and type this code in it:

            my_tennis_club/members/urls.py:

            from django.urls import path
            from . import views

            urlpatterns = [
                path('members/', views.members, name='members'),
            ]
- 
### 2.9 Templates
### 2.10 Models
- Insert Data
- Delete Data
- Delete Data
- Update Model

https://www.w3schools.com/django/django_urls.php
