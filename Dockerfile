# Use an official Python runtime as the base image
FROM python:trixie

#create a working directory 
RUN mkdir -p /usr/src

ADD ./ /usr/src/

WORKDIR /usr/src

# Copy the requirements file into the container
COPY requirements.txt /usr/src

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python", "main.py"]