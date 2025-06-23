from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask import send_from_directory
import pandas as pd

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# --- Make 'now()' available in all templates ---
from datetime import datetime

@app.context_processor
def inject_now():
    """Expose a callable 'now' inside templates: {{ now().year }}"""
    return {'now': datetime.utcnow}
cars = pd.read_csv('used_cars.csv')

# Clean image column: remove blanks and turn nan/None into empty strings
cars['image'] = (
    cars['image']
        .astype(str)
        .str.strip()
        .replace({'nan': '', 'None': ''})
)

# Build a reusable, sorted brand list for dropdowns / filters
brands = sorted(cars['brand'].unique())

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
        flash("Car added to favorites!", "success")
    else:
        flash("Car already in favorites.", "info")
    return redirect(request.referrer or url_for('listings'))

@app.route('/favorites')
def favorites():
    fav_ids = session.get('favorites', [])
    favorite_cars = []
    for i in fav_ids:
        if 0 <= i < len(cars):
            car_dict = cars.iloc[i].to_dict()
            car_dict['car_id'] = i      # keep original index for detail link
            favorite_cars.append(car_dict)
    return render_template('favorites.html', favorite_cars=favorite_cars)

@app.route('/unfavorite/<int:car_id>')
def unfavorite_car(car_id):
    favorites = session.get('favorites', [])
    if car_id in favorites:
        favorites.remove(car_id)
        session['favorites'] = favorites
        flash("Car removed from favorites!", "warning")
    else:
        flash("Car not in your favorites.", "info")
    return redirect(url_for('favorites'))


@app.route('/listings')
def listings():
    return render_template('listings.html',
                           cars=cars.to_dict(orient="records"),
                           brands=brands)

# --- Donation & About routes ---------------------------------------------

@app.route('/donate_car')
def donate_car():
    """Landing page for car donation (placeholder)."""
    # When a dedicated template is ready, swap the return line for:
    # return render_template('donate_car.html')
    return "<h1>Donate a Car – Coming Soon</h1><p>Thank you for your generosity! " \
           "A full donation form will appear here shortly.</p>"

@app.route('/donate_cash')
def donate_cash():
    """Landing page for cash donation (placeholder)."""
    return "<h1>Donate Cash – Coming Soon</h1><p>Secure cash donations will be enabled soon.</p>"


@app.route('/about')
def about():
    """About Us detailed page (placeholder)."""
    return render_template('about.html')

# --- Contact placeholder route ---
@app.route('/contact')
def contact():
    """Contact page (placeholder)."""
    return "<h1>Contact Us</h1><p>A full contact form will appear here soon.</p>"

# --- Careers placeholder route ---
@app.route('/careers')
def careers():
    """Careers page (placeholder)."""
    return "<h1>Careers – Join Our Team</h1><p>We’ll list open positions here soon.</p>"

if __name__ == '__main__':
    app.run(debug=True)