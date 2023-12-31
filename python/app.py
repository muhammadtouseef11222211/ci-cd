from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route and a function to handle the route
@app.route('/')
def hello_world():
    return 'This will automatically trigger the pipeline'

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

