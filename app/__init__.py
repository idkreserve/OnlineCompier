from flask import Flask
from datetime import timedelta

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(days=10)
