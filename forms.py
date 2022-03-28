from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FloatField
from wtforms.validators import InputRequired

###############################
###   App Calculator form   ###
###############################
class AddRecordForm(FlaskForm):
    bus_kms = FloatField("Bus (Kilometers)", [InputRequired()])
    bus_co2 = FloatField("Bus (CO2)")
    bus_type = SelectField("Bus (Type of Fuel)",
                           [InputRequired()],
                           choices=[
                               ('Bus Diesel', 'Bus Diesel'),
                               ('Bus CNG', 'Bus CNG'),
                               ('Bus Petrol', 'Bus Petrol'),
                               ('Bus No Fossil Fuel', 'Bus No Fossil Fuel')
                           ])
    submit = SubmitField("Submit")
