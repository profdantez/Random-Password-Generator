from flask import Flask, render_template, request, url_for, redirect
from algorithm import generate_password

app = Flask(__name__)
 

@app.route('/', methods=['GET', 'POST'])
def home():
    global password
    if request.method == 'POST':
        nr_letters = request.form.get("nr_letters")
        nr_numerals = request.form.get('nr_numerals')
        nr_symbols = request.form.get('nr_symbols')
        password = generate_password(int(nr_letters), int(nr_numerals), int(nr_symbols))
        return redirect(url_for('show_password'))
    return render_template('home.html') 

@app.route('/show_password')
def show_password():
    return render_template("show_password.html", password=password)

if __name__ == '__main__':
    app.run(debug=True)