PITCH-60-APP
Author
MACRINE ALICE ADHIAMBO "ALICIA"[https://github.com/Alicia-krynne]

Description
This is a flask application that allows users to post one minute pitches and also allows other users who have signed up to comment and upvote or downvote a pitch. It also allows a person to signup to be able to access the functionalities of the application

SCREENSHOTS

![HOME PAGE](window.png)

![PROFILE](prettyprofile.png)

![Pitch](pitch2.png)

![log-in-window](login.png)

CLONNG THE  REPOSITORY:
https://github.com/Alicia-krynne/PITCH-60-APP.git
Move to the folder and install requirements
cd pitch pitch-app
pip install -r requirements.txt (to  install dependecies)
Exporting Configurations
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
Running the application
python3 manage.py server
Testing the application
python3 manage.py test
Open the application on your browser 127.0.0.1:5000.

Technology used
1. Python :This is the main language in this project to create the methods and funtions needed. 
2. HTML: for creating the pages that are in the web app. also using HTML to manipulate the display. 
3. css : this is the styling language used for this app. Bootsrap is also added to make styling more efficient. 
4. shell&powershell : used to combine the flexibility of scripting, command-line speed, and the power of a GUI-based admin tool, in this case for our app.
5. Heroku :  for deploying the  app 

Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug.

Contact Information
If you have any question or contributions, please email me at [alicakryne@outlook.com]

License
MIT License:
Copyright (c) 2021 Macrine Alice Adhiambo
