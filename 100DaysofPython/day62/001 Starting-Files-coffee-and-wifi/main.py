from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe location (URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time (8:00AM)', validators=[DataRequired()])
    close_time = StringField('Closing Time (8:00PM)', validators=[DataRequired()])

    coffee_rating = SelectField('Coffee Rating ☕️', choices=["0", "1", "2", "3", "4", "5"], validators=[DataRequired()])
    wifi_rating = SelectField('WiFi Rating 💪', choices=["0", "1", "2", "3", "4", "5"], validators=[DataRequired()])
    power_rating = SelectField('Power Outlet Rating 🔌', choices=["0", "1", "2", "3", "4", "5"],
                               validators=[DataRequired()])

    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = [
            form.cafe.data,
            form.location.data,
            form.open_time.data,
            form.close_time.data,
            form.coffee_rating.data,
            form.wifi_rating.data,
            form.power_rating.data
        ]

        with open("cafe-data.csv", mode="a", newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(new_cafe)

        return render_template("add.html", form=form, msg="Cafe added successfully! ✅")  # ✅ Stay on the same page
    return render_template("add.html", form=form)  # ✅ Always render `add.html`


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = [row for row in csv_data]
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
