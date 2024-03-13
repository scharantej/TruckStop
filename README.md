## Flask Application Design

### HTML Files

**home.html**

* Display the map with coffee truck data.
* Provide a search bar for filtering trucks.

**coffee_trucks.html**

* List all coffee trucks, including name, location, and hours of operation.
* Allow users to filter trucks by name, location, or hours of operation.

### Routes

**@app.route('/')**

* Render the home page with the map and search bar.

**@app.route('/coffee_trucks')**

* Render the page listing all coffee trucks.

**@app.route('/search')**

* Handle search requests and return filtered coffee truck data.