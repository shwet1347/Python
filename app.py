from flask import Flask
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def hello():
    # Get today's date
    today_date = datetime.today().strftime('%Y-%m-%d')
    # Log the date (for internal debugging)
    app.logger.info(f"Today's date is: {today_date}")
    # Return the "Hello World" message with today's date
    return f"Hello World! Today's date is: {today_date}"

if __name__ == '__main__':
    # Set the port from the environment or default to 8080
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)
    
    # Log the start of the application
    app.logger.info(f"Starting the Flask app on port {port}")
    
    # Run the app on all addresses (0.0.0.0) so it's accessible externally
    app.run(port=port, host='0.0.0.0')
