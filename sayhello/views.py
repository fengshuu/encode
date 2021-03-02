# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""

from flask import render_template

from sayhello import app, qingwa
from sayhello.forms import HelloForm
from sayhello.models import Message
from sayhello.qingwa import decrypt_string, encrypt_string


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    message = Message()
    if form.validate_on_submit():
        inppp = form.body.data
        if inppp is not None or len(inppp) > 0:
            inppp = inppp.strip()
            if len(inppp) > 0:
                if inppp[0] in qingwa.trans_m:
                    body = decrypt_string(inppp)
                else:
                    body = encrypt_string(inppp)
                message = Message(body=body)
    return render_template('index.html', form=form, message=message)
