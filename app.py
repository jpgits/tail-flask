import sys
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    title = ["レイアウト", "TapIgnore"]
    #render-template-test
    if len(sys.argv) > 1 and sys.argv[1] == 'ttt':
        return render_template('layout.html', title=title[0])
    else:
        return render_template('index.html', title=title[1])

@app.route('/moves')
def moves():
    return render_template('moves.html')

@app.route('/project')
def project():
    return render_template('project.html')

if __name__ == '__main__':
    app.run(debug=True)
"""import sys, os, time, json, pickle, io, glob, random, string
import optparse
import urllib
from datetime import timedelta

from logging.config import dictConfig
dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            },
            "size-rotate": {
                "class": "logging.handlers.RotatingFileHandler",
                "filename": "./logs/flask.log",
                "maxBytes": 1000000,
                "backupCount": 5,
                "formatter": "default",
            },
        },
        "root": {
            "level": "INFO",
            "handlers": [ "console", "size-rotate", ],
        },
    }
)

from http import HTTPStatus
from flask import Flask, flash, redirect, url_for, request, render_template
from flask import session, jsonify, abort
from flask import Response, make_response, app
from markupsafe import Markup
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask( __name__ )

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('img/ghost.png')

def make_pin(size):
    return ''.join( random.choice(string.digits)for _ in range(size))
    return f'pin-{self.random_number(12)}'

@app.route('/')
def index():
    referrer = request.referrer
    if not referrer:
        referrer = '/'
    pin = make_pin(12)
    app.logger.info(f'{request.remote_addr} - - PING:\t{pin}\t{int(time.time())}\t/')
    ttl = 'template'
    return render_template('index.html', title=ttl, header_title=ttl, footer_title=ttl, pin=pin, referrer=referrer)

#--------------------
# ログ分析用
# 足跡をログに出力
#--------------------

@app.route('/api/ping', methods=['GET'])
def ping():
    pin  = request.args.get('pin', None)
    mark = request.args.get('mark', None)
    app.logger.info(f'{request.remote_addr} - - PING:\t{pin}\t{int(time.time())}\t{mark}')
    return ''

def parameter_info(pgm_name, opt):
    msg = [
        '-' * 24,
        f'   {"program":10}: {pgm_name}',
    ]
    for key in opt.__dict__.keys():
        msg.append(f'   {key:10}: {opt.__dict__[key]}')
    msg.append('-' * 24)
    return '\n' + '\n'.join(msg)

def parse_args():
    usage = 'usage: %prog --port PORT[18000]'
    op = optparse.OptionParser(usage=usage)
    op.add_option('--port', dest='port', default='18000')
    (opt, args) = op.parse_args()
    opt.port = int(opt.port)
    return(opt, args)

if __name__=='__main__':
    opt, args = parse_args()
    #app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.logger.info(parameter_info(os.path.basename(__file__), opt))
    app.run(host='0.0.0.0', port=opt.port, debug=True)
"""