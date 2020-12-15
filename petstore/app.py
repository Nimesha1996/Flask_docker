from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Nim96chathu@@localhost:13306/petstore'
db = SQLAlchemy(app)
db.init_app(app)

if __name__ == '__main__':
    app.run()
