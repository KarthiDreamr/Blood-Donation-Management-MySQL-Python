# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
source myenv/bin/activate

# Install packages from requirements.txt
pip install -r requirements.txt

# Run
python index.py

# Configure localhost name and password
db_creation.py file