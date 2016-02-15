from flask import Flask, jsonify,render_template,flash,url_for,session,request,redirect
app = Flask(__name__)
app.debug = True
app.secret_key = 'secret'

@app.route("/")
def hello():
    return "Hello World!"

    
@app.route("/json/<name>")
def name(name):
    return jsonify(name=name,age=2)
    
    
@app.route("/html/<int:age>")
def age(age):
    if request.method == 'GET':
        print url_for('age',age=age)
    return render_template('age.html',age=age)
      
@app.route("/fla")
def flashme():
    flash('Youve been flashed "%d"' % 999)
    return redirect(url_for('age', age=100))

print app.url_map

if __name__ == "__main__":
    app.run('0.0.0.0',3000)