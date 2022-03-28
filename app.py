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
    if form.validate_on_submit():
        bus_kms = form.bus_kms.data

        bus_type = form.bus_type.data

        if bus_type == 'Bus Diesel':
            co2_bus = float(bus_kms) * 0.10231
        elif bus_type == 'Bus CNG':
            co2_bus = float(bus_kms) * 0.08
        elif bus_type == 'Bus Petrol':
            co2_bus = float(bus_kms) * 0.10231
        else:
            co2_bus = float(bus_kms) * 0

        co2_bus = float("{:.2f}".format(co2_bus))

        form.bus_co2.data = co2_bus

        return render_template('app_calculator2.html', title='App Calculator', legend='App Calculator',
                               paragraph='(Based on the code developed by Gabriel Fuentes for the course ENE425)',
                               co2_bus=co2_bus, bus_kms=bus_kms, bus_type=bus_type, form=form)
    return render_template('app_calculator.html', title='App Calculator', legend='App Calculator',
                           paragraph='(Based on the code developed by Gabriel Fuentes for the course ENE425)',
                           form=form)

if __name__ == '__main__':
    app.run(debug=True)
