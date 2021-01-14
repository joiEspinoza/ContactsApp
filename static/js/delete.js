
const btnDelete = document.querySelectorAll( ".btn-delete" );
//crea nodos

if( btnDelete )
{

    const btnArray = Array.from( btnDelete );
    
    btnArray.forEach( ( btn ) => { 

            btn.addEventListener( "click", ( event ) => {

                if( !confirm( "Are you sure you want delete this?" ) )
                {
                    event.preventDefault();
                };

            });

    });
  
};