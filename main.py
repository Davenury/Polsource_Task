from flask import Flask, request, render_template
from flask_cors import CORS

from database.Database import Database
from src.exceptions.Exceptions import WebException, NoteNotFound, NoteDeleted

database = None


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return render_template("index.html")


def get_and_check_note_params(request):
    title = request.form.get("title")
    content = request.form.get("content")
    if title is None or title == "":
        raise WebException("Title of note cannot be empty!", 406)
    if content is None or content == "":
        raise WebException("Content of note cannot be empty!", 406)
    return title, content


@app.route("/create_note", methods=["POST"])
def create_note():
    try:
        title, content = get_and_check_note_params(request)
    except WebException as e:
        return e.message, e.code
    database.create_note(title, content)
    return "created", 201


@app.route("/update_note/<note_id>", methods=["POST"])
def update_note(note_id):
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


@app.route("/delete_note/<note_id>", methods=["POST"])
def delete_note(note_id):
    try:
        database.delete_note_by_id(note_id)
    except NoteNotFound:
        return "There's no such note", 404
    return "Note deleted", 200


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


@app.route('/get_versions_by_id/<note_id>', methods=["GET"])
def get_versions_by_id(note_id):
    try:
        notes = database.get_versioned_note_by_id(note_id)
        notes_jsonified = [note.get_json() for note in notes]
        return {
            "notes": notes_jsonified
        }
    except NoteNotFound:
        return "There are no versions of this note", 404


if __name__ == "__main__":
    database = Database()
    app.run()
