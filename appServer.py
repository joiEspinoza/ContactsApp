from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#----------------------------------------->

app = Flask( __name__ )

################################################################

app.config[ "MYSQL_HOST" ] = "localhost"
app.config[ "MYSQL_USER" ] = "root"
app.config[ "MYSQL_PASSWORD" ] = ""
app.config[ "MYSQL_DB" ] = "flaskcruddb"
dataBase = MySQL( app )

################################################################

@app.route( "/" )

def index():
    return render_template( "index.html" )

################################################################

@app.route( "/add_contact", methods = [ 'POST' ] )

def addContact():
    if request.method == "POST":

        fullName = request.form[ "fullname" ]
        phone    = request.form[ "phone" ]
        email    = request.form[ "email" ]

        cursor   = dataBase.connection.cursor()
        cursor.execute( "INSERT INTO contacts ( fullname, phone, email ) VALUES ( %s, %s, %s )", ( fullName, phone, email ) )
        dataBase.connection.commit()

        flash( "Created" )
        return redirect( url_for( "index" ) )
        # dispara la funcion de la ruta

##################################################################

@app.route( "/edit_contact" )

def editContact():
    return "edit screen"

################################################################

@app.route( "/delete_contact" )

def deleteContact():
    return "delete screen"

################################################################

#---------------------------------------------

if __name__ == "__main__":  
    app.run( port = 3000, debug = True )

#---------------------------------------------

