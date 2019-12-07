from website.models import WebSite

def authenticate(password):
    user = WebSite.check_password(password)
    if user.route in Website.routes:
        return user

def identity(payload):
    user_id = payload['identity']
    return WebSite.find_by_id(user_id)
