to run this web app locally

after clone git

1. python3 -m venv venv
2. source venv/bin/activate
3. pip install Flask gunicorn
4. gunicorn webapp:app -> 127.0.0.1:8000

to exit venv, type deactivate

