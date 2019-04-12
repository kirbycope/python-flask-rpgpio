#!/usr/bin/python
from flask import Flask
from Routes import routes

# Create a 'flask' instance using this ('name') module
app = Flask(__name__)

# Register the blueprint
app.register_blueprint(routes)

# Start the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337, debug=True)
