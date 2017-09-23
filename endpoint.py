'''
Created on 23 Aug 2017

@author: havannavar
'''
from app import app, api, parse_email, controller

@app.route(api.get('login'), methods=['POST'])
@parse_email.validate
def login():
    return controller.login()


def runserver():
    app.run(host='localhost', port=8081)

if __name__ == '__main__':
    runserver()