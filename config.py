import os
from pathlib import Path
import zipfile
import datetime
from dotenv import load_dotenv

# import json
# import requests
# import logging.handlers


class Config:
    load_dotenv()

    basedir = os.path.abspath(os.path.dirname(__file__))
    static_dir = Path(basedir,'app/static').as_posix()
    templates_dir = Path(basedir, 'app/templates').as_posix()
    SITE_HOST = '127.0.0.1'
    SITE_PORT = 6001
    SITE_URL = f"http://{SITE_HOST}:{SITE_PORT}"
    GIT_REPO = "https://github.com/johnwshc/soc-econ-up.git"
    GIT_account = 'jcase4218@gmail.com'
    GIT_USER = 'johnwshc'
    GIT_PW = 'C0mradeL3nin'

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-gue55'
    azure_url = 'https://flaskfolium.azurewebsites.net'

    DEVGMAIL = 'devcase181@gmail.com'
    DEVGMAIL_PW = 'VIl3nin!!'

    #     config utils

    @staticmethod
    def unzip(zipf: str, dir: str):
        with zipfile.ZipFile(zipf, 'r') as zip_ref:
            zip_ref.extractall(dir)

    #  datetime.dateime to and from strings utilities
    @staticmethod
    def date2str(d: datetime.datetime):
        return d.strftime('%m/%d/%Y')

    @staticmethod
    def str2date(s: str):
        return datetime.datetime.strptime(s, '%m/%d/%Y')

    @staticmethod
    def capitalizeEachWord(s: str):
        words = s.split(' ')
        cwords = list(map(str.capitalize, words))
        return ' '.join(cwords)

    @staticmethod
    def e_slugify(s: str):
        import re
        s = re.sub('[^0-9a-zA-Z]+', '-', s)
        return s


