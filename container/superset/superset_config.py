# Configuration file for Apache Superset

import os

# Secure SECRET_KEY
SECRET_KEY = os.environ.get('SUPERSET_SECRET_KEY', 'goTwArAC0buI5DLNQOcWHqL0J+Fw9om9Z0RU7hYByZ06keVrQkp7Ew6L')
