def populate():
    from inspire import db
    import inspire.database as database
    
    u = database.User(email='acbart', password='tmppass', name='Austin Cory Bart', user_type=database.User.ADMIN)
    db.session.add(u)
    
    db.session.commit()