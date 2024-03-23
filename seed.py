from models import User, db
from app import app

with app.app_context():
    # Create all tables
    db.drop_all()
    db.create_all()

    # If table isn't empty, empty it
    User.query.delete()

    # Add users
    joe_smith = User(first_name='Joe', 
                     last_name='Smith', 
                     image_url = 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')

    jane_smooth = User(first_name='Jane', 
                     last_name='Smooth', 
                     image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWomPds9w5emH_C6RY8xF7KRCJe6I5zwVsuw&usqp=CAU')

    bob_korn = User(first_name='Bob', 
                     last_name='Korn', 
                     image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR77iOanUEwD6cR1bth7E0y0jnAJCnDH6Zp1Q&usqp=CAU')

    # Add new objects to session, so they'll persist
    db.session.add(joe_smith)
    db.session.add(jane_smooth)
    db.session.add(bob_korn)

    # Commit--otherwise, this never gets saved!
    db.session.commit()