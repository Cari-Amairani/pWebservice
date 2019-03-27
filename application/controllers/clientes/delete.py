import config
import hashlib
import app

class Delete:
<<<<<<< HEAD
    
    def __init__(self):
        pass

=======

    def __init__(self):
        pass
>>>>>>> 93487404812230ed9806be6e6f32916afcce57c1
    def GET(self, id, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(id) # call GET_DELETE function
<<<<<<< HEAD
            elif session_privilege == 1: # guess user
=======
            elif privsession_privilegeilege == 1: # guess user
>>>>>>> 93487404812230ed9806be6e6f32916afcce57c1
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(id) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

<<<<<<< HEAD

    @staticmethod
    def GET_DELETE(id, **k):

=======
    @staticmethod
    def GET_DELETE(id, **k):
>>>>>>> 93487404812230ed9806be6e6f32916afcce57c1
        message = None # Error message
        id = config.check_secure_val(str(id)) # HMAC id validate
        result = config.model.get_clientes(int(id)) # search  id
        result.id = config.make_secure_val(str(result.id)) # apply HMAC for id
        return config.render.delete(result, message) # render delete.html with user data

<<<<<<< HEAD
    @staticmethod
=======
>>>>>>> 93487404812230ed9806be6e6f32916afcce57c1
    def POST_DELETE(id, **k):
        form = config.web.input() # get form data
        form['id'] = config.check_secure_val(str(form['id'])) # HMAC id validate
        result = config.model.delete_clientes(form['id']) # get clientes data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id = config.check_secure_val(str(id))  # HMAC user validate
            id = config.check_secure_val(str(id))  # HMAC user validate
            result = config.model.get_clientes(int(id)) # get id data
            result.id = config.make_secure_val(str(result.id)) # apply HMAC to id
            return config.render.delete(result, message) # render delete.html again
        else:
<<<<<<< HEAD
            raise config.web.seeother('/clientes') # render clientes delete.html 
=======
            raise config.web.seeother('/clientes') # render clientes delete.html
>>>>>>> 93487404812230ed9806be6e6f32916afcce57c1
