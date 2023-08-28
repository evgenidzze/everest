import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_uploads import UploadSet, IMAGES, configure_uploads

from market.celery_utils import make_celery

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'marker.db')  # for localhost
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/market'  # for docker

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '06a09495199cd7ea9ff14c79'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/images')

app.config.from_mapping(CELERY=dict(
    broker_url="redis://redis:6379/0",
    result_backend="redis://redis:6379/0",
    task_ignore_result=True,
), )
celery = make_celery(app)

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.config['SECURITY_PASSWORD_SALT'] = os.environ.get("SECURITY_PASSWORD_SALT",
                                                      '146585145368132386173505678016728509634')
app.config["SECURITY_EMAIL_VALIDATOR_ARGS"] = {"check_deliverability": False}

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from market.views import json_rpc
from market.views import admin
from market.views import auth
from market.views import main
