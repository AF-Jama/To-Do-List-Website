from flask import Flask, redirect,render_template,request,abort,after_this_request,session,flash,url_for
from pandas import read_parquet



app = Flask(__name__,template_folder='../templates',static_folder='../static')
app.secret_key = "hdffbHh-34t64GD%hebkgTDYRCrcgv_+3Nhgbhgc34tfcr"


@app.route('/',methods = ["POST","GET"]) # route takes in a GET and POST
def add():
    if request.method == "POST":
        note_text = request.form["note-text"] # gets text submitted
        note_list = session['notes'] # assigns list of notes to variable
        note_list.append(note_text) # appends to note list
        session['notes'] = note_list # assigns updated note list to session
        return render_template('add.html') # redirects using GET request which renders notes

    elif request.method == "GET":
        if 'notes' not in session:
                print("SESSION CREATED")
                session['notes'] =[] # sets
                return render_template('add.html',context={"message":"No notes for you here yet"})

        else:
            print("RENDERED")
            return render_template('add.html',context={"notes":session['notes']})












if __name__ == "__main__":
    app.run(debug=True)