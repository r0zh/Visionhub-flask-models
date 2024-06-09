# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install git and curl
RUN apt-get update && apt-get install -y git curl

# Install ngrok
RUN curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc | tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null && echo "deb https://ngrok-agent.s3.amazonaws.com buster main" | tee /etc/apt/sources.list.d/ngrok.list && apt update && apt install ngrok

# Make port 80 available to the world outside this container
EXPOSE 5000

# Clone the shape-e repository
RUN git clone https://github.com/openai/shap-e

# Install shape-e requirements
RUN pip install -e ./shap-e

# Run app.py when the container launches
CMD ["python", "app.py"]
