from flask import Flask, render_template, request, redirect, url_for, session
from flask import send_from_directory
import pandas as pd

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
cars = pd.read_csv('used_cars.csv')

# Clean image column: remove blanks and turn nan/None into empty strings
cars['image'] = (
    cars['image']
        .astype(str)
        .str.strip()
        .replace({'nan': '', 'None': ''})
)

@app.route('/')
def index():
    brands = sorted(cars['brand'].unique())
    return render_template('index.html', cars=cars.to_dict(orient='records'), brands=brands)

@app.route('/filter', methods=['POST'])
def filter_by_brand():
    selected_brand = request.form.get('brand')
    filtered = cars[cars['brand'] == selected_brand]
    brands = sorted(cars['brand'].unique())
    return render_template('index.html', cars=filtered.to_dict(orient='records'), brands=brands, selected=selected_brand)

@app.route('/car/<int:car_id>')
def car_detail(car_id):
    try:
        car = cars.iloc[car_id].to_dict()
    except IndexError:
        return "Car not found", 404

    return render_template('car_detail.html', car=car, car_id=car_id)

@app.route('/recommend/<int:car_id>')
def recommend(car_id):
    selected = cars.iloc[car_id]
    recommended = cars[(cars['price'] - selected['price']).abs() <= 2000]
    return render_template('recommend.html', selected=selected, recs=recommended.to_dict(orient='records'))

@app.route('/favorite/<int:car_id>')
def favorite_car(car_id):
    favorites = session.get('favorites', [])
    if car_id not in favorites:
        favorites.append(car_id)
        session['favorites'] = favorites
    return redirect(url_for('index'))

@app.route('/favorites')
def favorites():
    favorites = session.get('favorites', [])
    cars_list = cars.to_dict(orient='records')
    favorite_cars = [car for car in cars_list if car['id'] in favorites]
    return render_template('favorites.html', cars=favorite_cars)

if __name__ == '__main__':
    app.run(debug=True)