

# Make migration 
python -m pip install --upgrade pip


pip install -r requirements.txt
cd "./conceptile"
python manage.py makemigrations
python manage.py migrate