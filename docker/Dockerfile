# Use the official Red Hat UBI 9 Python image
FROM registry.access.redhat.com/ubi9/python-39:1-117.1684741281

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_PORT=8081

# By default, listen on port 8081
EXPOSE 8081

# Set the working directory in the container
WORKDIR /projects

# Copy the content of the local src directory to the working directory
COPY . .

# Install any dependencies
RUN \
  if [ -f requirements.txt ]; \
    then pip install -r requirements.txt; \
  elif [ `ls -1q *.txt | wc -l` == 1 ]; \
    then pip install -r *.txt; \
  fi

# Install gunicorn for production deployment
RUN pip install gunicorn

# Specify the command to run on container start
CMD ["gunicorn", "-b", "0.0.0.0:8081", "app:app"]
