from website.db import db
import json

class WebSite(db.Model):
    __tablename__ = "test"
    routes= ['gouda','test1','test2']

    route_id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String, nullable=False)
    route = db.Column(db.String, nullable=False)
    
    def __init__(self, password, route):
        self.password = password
        self.route = route

    def __repr__(self):
        return 'WebSite(password {}, route {})'.format(self.password, self.route)
    def make_json(self):
        data = {}
        data['password'] = self.password
        data['route'] = self.route
        return json.dumps(data)

    @classmethod
    def check_password(cls,password):
        query = cls.query.filter_by(password=password).first_or_404()
        return query

    @classmethod
    def find_by_id(cls,_id):
        query=cls.query.filter_by(id=_id).first_or_404()
        return query


