import config
import hashlib
import app

class Insert:

    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True:
            # session_username = app.session.username
<<<<<<< HEAD
            session_privilege = app.session.privilege  # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_INSERT() # call GET_INSERT() function
            elif session_privilege == 1: # guess user
=======
            session_username = app.session.privilege  # get the session_privilege
            if session_username == 0: # admin user
                return self.GET_INSERT() # call GET_INSERT() function
            elif session_username == 1: # guess user
>>>>>>> 93487404812230ed9806be6e6f32916afcce57c1
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
<<<<<<< HEAD
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_INSERT() # call POST_EDIT function
            elif session_privilege == 1: # guess user
=======
            session_username = app.session.privilege # get the session_privilege
            if session_username == 0: # admin user
                return self.POST_INSERT() # call POST_EDIT function
            elif privilege == 1: # guess user
>>>>>>> 93487404812230ed9806be6e6f32916afcce57c1
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

<<<<<<< HEAD
 @staticmethod
    def GET_INSERT():
        return config.render.insert() # render insert.html

    @staticmethod
=======

    def GET_INSERT():
        return config.render.insert() # render insert.html

>>>>>>> 93487404812230ed9806be6e6f32916afcce57c1
    def POST_INSERT():
        form = config.web.input() # get form data

        # call model insert_clientes and try to insert new data
        config.model.insert_clientes(
<<<<<<< HEAD
            form['nombre'],form['ape_mat'],form['ape_pat'],form['telefono'],form['correo'],
=======
            form['nombre'],form['ape_pat'],form['ape_mat'],form['telefono'],form['correo'],
>>>>>>> 93487404812230ed9806be6e6f32916afcce57c1
        )
        raise config.web.seeother('/clientes') # render clientes index.html
