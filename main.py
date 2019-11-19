from flask import Flask
from routes.init import initRoute
import datetime

app = Flask(__name__)
app = initRoute(app)
    
app.run()
