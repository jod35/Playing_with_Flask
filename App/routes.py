from App import app,db
from flask import render_template,url_for,redirect,request
from App.models import Text

@app.route('/', methods=['POST','GET'])
def index():
    texts=Text.query.all()
    return render_template('index.html',texts=texts)

@app.route('/addtext', methods=['POST'])
def add_text():
    if request.method=='POST':
        text=request.form.get('text')
        comment=request.form.get('comment')
        new_text=Text(text=text,comment=comment)
        db.session.add(new_text)
        db.session.commit()
        return redirect('/')