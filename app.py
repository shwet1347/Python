from flask import Flask
from datetime import datetime
import os
import logging

# Set up basic logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    # Log today's date using Flask's logger
    today_date = datetime.today()
    app.logger.info("Today's date is: %s", today_date.strftime('%Y-%m-%d'))

    # Get the port from the environment or default to 8080
    port = os.environ.get('FLASK_PORT', 8080)
    port = int(port)

    # Start the Flask app
    app.run(port=port, host='0.0.0.0')
