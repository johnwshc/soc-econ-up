from flask import Flask
from config import Config
from app.sumlog import SLogger
from analz.soc_econ.labor_div.jobs import CFED1
from analz.dashapps.dataUtils import US_Gov_Employment as USGE


server = Flask(__name__)
server.config.from_object(Config)
server.config['WTF_CSRF_ENABLED'] = False
slog = SLogger()
cfed = CFED1.fromCFED()
usge = USGE()
SECRET_KEY = server.config['SECRET_KEY']



from app import routes