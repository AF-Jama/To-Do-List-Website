from flask import Flask, flash, redirect, render_template, request,g,session
from flask_restful import Resource, Api,reqparse,abort
from matplotlib.style import context



app = Flask(__name__,template_folder='templates',static_folder='static')
app.secret_key = "sfibrtuoytvRNtHV_ber6HAVDVTEVR?JNRioedmkr"

@app.route('/',methods = ["POST","GET"]) # route takes in a GET and POST
def add():
    if request.method == "POST":
        note = request.form["note-text"]
        note_list = session['notes']
        note_list.append(note) # appends note list with new note
        session['note'] = note_list
        print("============================")
        for note in session['notes']:
            print(note)
        return redirect('/')



    elif request.method == "GET":
        if 'notes' not in session:
                print("SESSION CREATED")
                session['notes'] =[] # sets to an empty list
                return render_template('add.html', message = "No notes added yet/empty") # renders out page and context that notifies that there are no notes

        else:
            '''triggered if "notes" key already exists'''
            print("SESSION ALREADY EXISTS") 
            return render_template('add.html',notess = session['notes'])
# @app.route('/')
# def index():
#     return "GELLO"

@app.route('/delete<note_number>',methods = ["POST"])
def delete(note_number):
    note_number = int(note_number) # converts string index into int
    '''triggered when delete button is clicked'''
    notes_list = session['notes']
    notes_list.pop(note_number)
    session['notes'] = notes_list
    print("HIT")
    return redirect('/')


@app.route('/delete_all',methods = ["POST"])
def delete_all():
    '''method triggered'''
    notes_list = session['notes']
    notes_list = [] # clear lists using clear() method
    session['notes'] = notes_list
    return redirect('/')






if __name__ == "__main__":
    app.run(debug=True)

