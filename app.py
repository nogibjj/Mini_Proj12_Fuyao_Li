from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Available car options
car_brands = ['Toyota', 'Kia', 'Benz', 'BMW']
car_years = ['2025', '2024', '2023', '2022', '2021']
car_mileages = ['6000 mi', '20000 mi', '30000 mi', '55000 mi']

# Storage for selected cars
selected_cars = []

# HTML template for the car purchasing interface
CAR_PURCHASE_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Car Purchasing Interface</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f0f0f0;
        }
        .container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
            gap: 10px;
            margin-bottom: 20px;
        }
        select, button {
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            padding: 8px;
            border-bottom: 1px solid #ddd;
            display: flex;
            justify-content: space-between;
        }
        .delete-btn {
            background-color: #f44336;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .delete-btn:hover {
            background-color: #da190b;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Car Purchasing Interface</h1>
        <form action="/add" method="post">
            <label for="brand">Car Brand:</label>
            <select id="brand" name="brand" required>
                {% for brand in brands %}
                <option value="{{ brand }}">{{ brand }}</option>
                {% endfor %}
            </select>

            <label for="year">Car Year:</label>
            <select id="year" name="year" required>
                {% for year in years %}
                <option value="{{ year }}">{{ year }}</option>
                {% endfor %}
            </select>

            <label for="mileage">Mileage:</label>
            <select id="mileage" name="mileage" required>
                {% for mileage in mileages %}
                <option value="{{ mileage }}">{{ mileage }}</option>
                {% endfor %}
            </select>

            <button type="submit">Add Car</button>
        </form>

        <ul>
            {% for car in cars %}
            <li>
                {{ car }}
                <form action="/delete" method="post" style="display: inline;">
                    <input type="hidden" name="car" value="{{ car }}">
                    <button type="submit" class="delete-btn">Remove</button>
                </form>
            </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(
        CAR_PURCHASE_TEMPLATE, 
        brands=car_brands, 
        years=car_years, 
        mileages=car_mileages, 
        cars=selected_cars
    )

@app.route('/add', methods=['POST'])
def add_car():
    brand = request.form.get('brand')
    year = request.form.get('year')
    mileage = request.form.get('mileage')
    car = f"{brand}, {year}, {mileage}"

    if car not in selected_cars:
        selected_cars.append(car)

    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete_car():
    car = request.form.get('car')
    if car in selected_cars:
        selected_cars.remove(car)

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run("0.0.0.0", port=80, debug=True)
