from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
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

    return render_template('car_detail.html', car=car)

@app.route('/recommend/<int:car_id>')
def recommend(car_id):
    selected = cars.iloc[car_id]
    recommended = cars[(cars['price'] - selected['price']).abs() <= 2000]
    return render_template('recommend.html', selected=selected, recs=recommended.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)