# CPOP Backend

CPOP Backend is the backend part of the CPOP project.

<!--[Documentation](docs/)-->

## How to Compile

### Hot Reloading

To install the required packages, follow the steps below:

````bash
# Create a virtual environment
python3 -m venv .venv
# Activate the virtual environment (Windows)
.venv\Scripts\activate
# Activate the virtual environment (macOS)
source .venv/bin/activate
# Change directory to the project root
cd Backend
# Install Python dependencies
pip install -r requirements.txt

# q
python manage.py qcluster

# Run the development server
python manage.py runserver 0.0.0.0:8000


# Build the Docker image
docker build -t cpop-server-image .

# Run the Docker container
docker run -p 8000:8000 cpop-server-image

### Contributor

- Project Manager: [LAIHUNGWEI](https://github.com/s990093)```
````
