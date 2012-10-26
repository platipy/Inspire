

Checkout a branch for your project

If you make changes to the tables, make sure you reset the server (with the "-r" command line option)

To make a function callable from the client conspyre library, simply decorate it with
    @app.conspyre(blueprint)
You will then have access to:
    named parameters
    g.user
    g.metadata
    
    
Database manipulation:
    Adding
    Removing
    Updating
    Deleting
    Querying
    
    Making a table
        Changing an already made table
    
    Flushing
    Committing
    