
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Read in the coffee trucks data
coffee_trucks = pd.read_csv('coffee_trucks.csv')

@app.route('/')
def home():
    """Render the home page with the map and search bar."""
    return render_template('home.html', coffee_trucks=coffee_trucks)

@app.route('/coffee_trucks')
def coffee_trucks_list():
    """Render the page listing all coffee trucks."""
    return render_template('coffee_trucks.html', coffee_trucks=coffee_trucks)

@app.route('/search')
def search():
    """Handle search requests and return filtered coffee truck data."""

    # Get the search term from the request
    search_term = request.args.get('search_term')

    # Filter the coffee trucks based on the search term
    filtered_coffee_trucks = coffee_trucks[coffee_trucks['name'].str.contains(search_term) |
                                            coffee_trucks['location'].str.contains(search_term)]

    # Return the filtered coffee trucks as JSON
    return filtered_coffee_trucks.to_json(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
