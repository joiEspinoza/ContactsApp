from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from helper import validator

#----------------------------------------->

app = Flask( __name__ )

################################################################

app.config[ "MYSQL_HOST" ] = "localhost"
app.config[ "MYSQL_USER" ] = "root"
app.config[ "MYSQL_PASSWORD" ] = ""
app.config[ "MYSQL_DB" ] = "flaskcruddb"
dataBase = MySQL( app )

################################################################

app.secret_key = "mysecretekey"

################################################################

@app.route( "/" )

def index():

    cursor = dataBase.connection.cursor()
    cursor.execute( "SELECT * FROM contacts" )
    response = cursor.fetchall()

    return render_template( "index.html", contacts = response )

################################################################

@app.route( "/add_contact", methods = [ 'POST' ] )

def addContact():

    if request.method == "POST":

        fullName = request.form[ "fullname" ]
        phone    = request.form[ "phone" ]
        email    = request.form[ "email" ]

        res = validator.validatorForm( { fullName, phone, email } )

        if res == False:
            flash( "all info is required" )
            return redirect( url_for( "index" ) )

        if validator.emailValidator( email ) == False:
            flash( "Valid email is required" )
            return redirect( url_for( "index" ) )


        cursor = dataBase.connection.cursor()
        cursor.execute( "INSERT INTO contacts ( fullname, phone, email ) VALUES ( %s, %s, %s )", ( fullName, phone, email ) )
        dataBase.connection.commit()


        flash( "Created successfuly" )
        return redirect( url_for( "index" ) )
        # dispara la funcion de la ruta

##################################################################

@app.route( "/get_contact/<string:contactId>" )

def editContact( contactId ):
    
    cursor = dataBase.connection.cursor()
    cursor.execute( "SELECT * FROM contacts WHERE id = {0}".format( contactId ) )
    response = cursor.fetchall()

    return render_template( "update.html", contact = response )

#-----------------------------------------------------------------

@app.route( "/update_contact/<string:contactId>", methods = [ 'POST' ] )

def updateContact( contactId ):

    if request.method == "POST":

        fullName = request.form[ "fullname" ]
        phone    = request.form[ "phone" ]
        email    = request.form[ "email" ]

        cursor = dataBase.connection.cursor()
        cursor.execute( "UPDATE contacts SET fullname = %s, phone = %s, email = %s WHERE id = %s",( fullName, phone, email, contactId ) )
        dataBase.connection.commit()  

        flash( "Updated successfuly" )
        return redirect( url_for( "index" ) )

################################################################

@app.route( "/delete_contact/<string:id>" )

def deleteContact( id ):

    cursor = dataBase.connection.cursor()
    cursor.execute( "DELETE FROM contacts WHERE id = {0}".format( id ) )
    dataBase.connection.commit()

    flash( "Deleted successfuly" )
    return redirect( url_for( "index" ) )

################################################################


#---------------------------------------------

if __name__ == "__main__":  
    app.run( port = 3000, debug = True )

#---------------------------------------------

