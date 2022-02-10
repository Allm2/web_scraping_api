_version_ = '1.0.0'

from flask import Flask

application = Flask(__name__)

from web_scraping.controller.scraping_crontroller import web_scraping
application.register_blueprint(web_scraping)