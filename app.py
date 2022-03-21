from flask import Flask, render_template
from forms import AddRecordForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '3434345791628bb0b13ce0c676dfde280ba245'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/app_calculator', methods=['GET', 'POST'])
def app_calculator():
    form = AddRecordForm()
    return render_template('app_calculator.html', title='App Calculator', legend='App Calculator',
                           paragraph='(Based on the code developed by Gabriel Fuentes for the course ENE425)',
                           form=form)

if __name__ == '__main__':
    app.run(debug=True)
