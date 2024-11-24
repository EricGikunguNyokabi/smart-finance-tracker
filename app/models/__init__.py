# app/models/__init__.py
from app import db

class User(db.Model):
    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=True) 
    middle_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True) 
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    otp = db.Column(db.String(6), nullable=True)  
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())  
    otp_created_at = db.Column(db.DateTime, default=db.func.current_timestamp()) 
    username = db.Column(db.String(100), unique=True, nullable=False)
    dob = db.Column(db.Date, nullable=False)

    def __repr__(self):  # Readable Representation
        return f"<User  {self.username}>"
    
    # Flask-Login requires these properties
    @property
    def is_active(self):
        return True  # You can implement your own logic here

    @property
    def is_authenticated(self):
        return True  # Always return True for authenticated users

    @property
    def is_anonymous(self):
        return False  # Always return False for authenticated users

    def get_id(self):
        return str(self.user_id)  # Return the user ID as a string
    
    # the __repr__ method in Python is a special method used to define how an object is represented as a string, primarily for debugging and development purposes.


# flask db migrate -m "Updated user model columns"
# flask db migrate -m "Initial migration"

# flask db upgrade