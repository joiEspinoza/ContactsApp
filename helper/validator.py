
def validatorForm( formValues = {} ):
    
    for value in formValues:

        if value == "":

            return False
        
           
####################################################


def emailValidator( email ):

    if email.find( "." ) == -1 or email.find( "@" ) == -1:

        return False

