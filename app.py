import logging
from flask import Flask
from datetime import datetime
import os

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/')
def hello():
    logging.info("Hello route accessed")
    return "Hello World!"

if __name__ == '__main__':
    today_date = datetime.today()
    logging.info("Today's date is: %s", today_date.strftime('%Y-%m-%d'))  # Logs today's date
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port, host='0.0.0.0')
