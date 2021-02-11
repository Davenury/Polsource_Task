# Polsource_Task
![Python](https://img.shields.io/badge/Language-Python-9cf) ![Framework](https://img.shields.io/badge/Framework-Flask-gray)

NoteAPI that enable users to create, read, update and delete notes.

## Table of Contents
* [Requirements](#requirements)
* [Database Setup](#database-setup)
* [Run Project](#run-project)
* [Run Project Demo](#run-project-demo)
* [Example Usages](#example-usages)
* [Project Structure](#project-structure)

---

### Requirements
Note, that if you don't want to install this project on your device, go directly into Run Project Demo section of this repository.

To run this project, you'll need Python 3 and flask module. When you download (or clone) this repository, go into command line, go to project directory and:

a) create env (optional but recommended)

b) type `pip install -r requirements.txt` (make sure that you're in directory with this file)

After some time (pip needs to install all requirements), the project is ready to go.

---

### Database Setup
You don't need to do anything more than run project. If you want to see SQL commands that create database, go to database directory and open sql_scripts.py file in any IDE
of your choice.
Why is that so, that you don't need to do anything special? If you look into main.py file, in line 97 we're creating new instance of Database class. And when you look at code
of this class, you'll see that we're creating "new" database. The thing is that it won't be created unless there's nothing in database file (SQL is "CREATE IF NOT EXISTS").

---

### Run Project
To run project, simply type `python main.py` in your command line. This will make a flask server, most probably on your localhost. To test it, please go to 
[this repository](https://github.com/Davenury/NoteIT), where you'll find detailed instruction of how to set up frontend part. Please note, that you'll need to change one thing
in there, because frontend was created with another URL (more about it in Run Project Demo section).

You can also run tests if you want so.

---

### Run Project Demo
If  you don't want to install anything on your device, you can check this server in another way. Go to [this site](https://repl.it/@Davenury/PolsourceTask), where you'll
see something like this:
![Repl](https://imgur.com/Xx3cO7j.png)
Click on green button with arrow to run the server!

Then click on the link under Live Demo section to go to NoteIT web application for looking how it works in real life.

![Repl2](https://imgur.com/m4PRDxp.png)

For more details on UI, go to [this repository](https://github.com/Davenury/NoteIT).

---

### Example usages

You can use this project as I've shown in Run Project Demo section (for fun) or in previous sections (for making your own version of this API and NoteIT app).

---

### Project Sturcture
Project consists few important files, mostly in database directory:
* database - directory with all files that are used in notes persistance
  * Database.py - file with Database class, wrapper for QueryExecutor class. Prepares notes, creates connection to database.
  * Note.py - file that consists Note class
  * QueryExecutor.py - file with QueryExecutor class that operates on database.
  * sql_scripts.py - file with SQL Scripts to create database.
* src/exceptions/Exceptions.py - file that contains several custom exceptions.
* templates/index.html - file with HTML code for start page of API.
* tests - directory with tests for CRUD operations.
* definitions.py - file with some constants.
* main.py - main flask file with all endpoints.
