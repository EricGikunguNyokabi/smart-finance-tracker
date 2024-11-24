PROJECT TITLE
smart-personal-finance-tracker ==========================================
    This project is for helping people manage their money.
        This is made posible by tracking day to day life transactions either by expenditure or investments.

    IndexPage/
        A brief view of the usage of app with modern designs using js, and bootstrap

    Reports/
        Once a user logs in and updates their expenditure details, then they're redirected to dashboard where they can see their expenditure reports(Yearly,Monthly,Weekly,Daily) Using figures and graphs.
    
    Goal-Plan/
        One can set goals and system will monitor and display the accomplishments according to data feed.

    Articles/
        Here is where you get financial literacy and learn from different authors on money management skills and where to invest.

    AI Model
        There will be Incorporation of machine learning technology using users data to determine-trends, forecast-trends and optimize on expenditure and investments directions.


PROJECT LAYOUT ===========================================================
├── env/
├── smart-finance-tracker/                            
|   ├── app/             
|   |   ├── __init__.py                  
|   |   ├── config.py                     
|   |   ├── models/                       # Folder for database models
|   |   |   ├── __init__.py                # Initialize models module
|   |   |   ├── user.py                    # User model
|   |   |   ├── income.py                  # Income model
|   |   |   ├── expense.py                 # Expense model
|   |   |   ├── investment.py              # Investment model
|   |   |   └── financial_prediction.py    # AI model for predictions
|   |   ├── views/                        # Views or routes
|   |   |   ├── __init__.py                # Initialize views module
|   |   |   ├── auth.py                    # Routes for user authentication
|   |   |   ├── income.py                  # Routes for income management
|   |   |   ├── expense.py                 # Routes for expense management
|   |   |   ├── investment.py              # Routes for investment management
|   |   |   ├── prediction.py              # Routes for AI predictions
|   |   |   └── report.py                 
|   |   ├── templates/                     
|   |   ├── static/                        # Static files (CSS, JS, images)
|   |   ├── forms/                         # Forms for user input
|   |   ├── services/                     
|   |   └── __init__.py                    # App initialization
|   ├── migrations/                        # Database migrations
|   ├── instance/                          
|   ├── requirements.txt                   
|   ├── run.py    
|   ├── .env        
|   ├── .gitignore                       
|   └── README.md                          # Backend documentation

# pip install flask-migrate
# pip install decouple
# pip install --upgrade python-decouple
# pip uninstall decouple
# pip freeze | grep decouple

# pip install pymysql
# pip install flask-wtf
# pip install email-validator

# deactivate  # Exit the current virtual environment
# rm -rf env  # Remove the existing virtual environment
# python3 -m venv env  # Create a new virtual environment
# source env/bin/activate  # Activate the new virtual environment
# pip install -r requirements.txt  # Reinstall dependencies

# When using environment variables defined in .env file, you should install the python-dotenv package. This package allows Flask to load these environment variables automatically. Run the following command:
# pip install python-dotenv

# pip install cryptography


DATABASE MIGRATIONS
Initialize the migrations directory
# flask db init
Create the migration script
# flask db migrate -m "Upgrade user model columns"
Apply the migration to the database
# flask db upgrade




GIT COMMANDS =============================================================
    git init
    git add README.md
    git commit -m first commit: Adding README.md
    git branch -M main
    git remote add origin https://github.com/EricGikunguNyokabi/smart-finance-tracker.git
    git push -u origin main

    ...push an existing repository from the commandline
    git remote add origin https://github.com/EricGikunguNyokabi/smart-finance-tracker.git
    git branch -M main
    git push -u origin main


.gitignore ================================================================
# ignore all .a files
*.a

# but do track lib.a, even though you're ignoring .a files above
!lib.a

# only ignore the TODO file in the current directory, not subdir/TODO
/TODO

# ignore all files in any directory named build
build/

# ignore doc/notes.txt, but not doc/server/arch.txt
doc/*.txt

# ignore all .pdf files in the doc/ directory and any of its subdirectories
doc/**/*.pdf





