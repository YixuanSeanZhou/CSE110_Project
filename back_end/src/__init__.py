from flask import jsonify

from .setup import app, login_manager

from .models.user import User

# -----------------------------------------------
# DO NOT EDIT ABOVE THE LINE

from .apis.user import user_api_bp as uapi
from .apis.major import major_api_bp as mapi
from .apis.minor import minor_api_bp as minor_api

app.register_blueprint(uapi, url_prefix="/api/users")
app.register_blueprint(mapi, url_prefix="/api/majors")
app.register_blueprint(minor_api, url_prefix="/api/minors")


@app.route("/")
def hello_world():
    return jsonify({'gary': 'planner'}), 200


# DO NOT EDIT BELOW THE LINE
# -----------------------------------------------
@login_manager.user_loader
def load_user(user_id):
    '''
    Function used to be a default loader for flask login.
    '''
    return User.get_user_by_id(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    '''
    Function used to turn down people who aren't logged in trying to
    access routes that are locked down.
    '''
    return jsonify({'reason': "Not logged in!"}), 403
