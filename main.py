from flask import Flask, request
from flask_cors import CORS

from database.Database import Database
from src.exceptions.Exceptions import WebException, NoteNotFound, NoteDeleted

database = None


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "hello world"


def get_and_check_note_params(request):
    title = request.form.get("title")
    content = request.form.get("content")
    if title is None or title == "":
        raise WebException("Title of note cannot be empty!", 406)
    if content is None or content == "":
        raise WebException("Content of note cannot be empty!", 406)
    return title, content


@app.route("/create_note", methods=["POST", "GET"])
def create_note():
    if request.method == "POST":
        try:
            title, content = get_and_check_note_params(request)
        except WebException as e:
            return e.message, e.code
        database.create_note(title, content)
        return "created", 201
    return "Hellow get"


@app.route("/update_note/<note_id>", methods=["GET", "POST"])
def update_note(note_id):
    if request.method == "POST":
        try:
            title, content = get_and_check_note_params(request)
        except WebException as e:
            return e.message, e.code
        try:
            database.update_note_by_id(note_id, title, content)
        except NoteNotFound:
            return "There's no such note", 404
        except NoteDeleted:
            return "This note was already deleted, you can't update it", 410
        return "Note was updated", 200
    return "Hellow update"


@app.route("/delete_note/<note_id>", methods=["GET", "POST"])
def delete_note(note_id):
    if request.method == "POST":
        try:
            database.delete_note_by_id(note_id)
        except NoteNotFound:
            return "There's no such note", 404
        return "Note deleted", 200
    return "Hello delete"


@app.route("/get_note/<note_id>", methods=["GET"])
def get_note_by_id(note_id):
    try:
        note = database.get_note_by_id(note_id)
        return note.get_json()
    except NoteNotFound:
        return "There's no such note", 404


@app.route("/get_all_notes", methods=["GET"])
def get_all_notes():
    try:
        notes = database.get_all_notes()
        notes_jsonified = [note.get_json() for note in notes]
        return {
            "notes": notes_jsonified
        }
    except NoteNotFound:
        return "There are no notes", 404


if __name__ == "__main__":
    database = Database()
    app.run()
