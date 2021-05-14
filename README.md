# online-data-storage-web-application
************Horizon - An Online Data Storage Web Application****************

Steps to run this Project on your local PC :-
Download and Install WAMP server : https://drive.google.com/file/d/18Sn3d_DEcKohnRKnjOqDYY0wfa_ioQlC/view?usp=sharing
Download and install Python==3.8 or above
Install pip-virtual environment by running this command in cmd:
    >>pip install virtualenvwrapper-win
Create a virtual environment:
    >>mkvirtualenv <name_of_Environemnt> (eg: mkvirtualenv test)
    >>workon <name_of_environment>(eg: workon test)
Now run the followiing command in cmd:
    >>pip install requirements.txt
Or if installing requirements.txt doesnt work try it manually by installing each packages individually:
(Follow steps 1 and  only if above statement doesnt work)
1. pip install django
2. pip install django mysqlclient
Now rune these commands
python manage.py collectstatic
python manage.py makemigrations
python manage.py migrate
Finally run the server
python manage.py runserver
