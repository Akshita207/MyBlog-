<h1>My Blog
</h1>
A Django-powered Blogging Site which allows users' to view posts and comment on it.

<h2>Getting Started</h2>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

<h2>Prerequisites</h2>
You should have Python3 and virtual environment installed on your computer. Install Python3 from https://www.python.org/ and then install virtual enviroment as shown below.
<pre>
pip install virtualenv
</pre>
<h2>
Installing
</h2>
First Clone this project to your PC.
then go into that directory and install the requirements.
<pre>
cd 
pip install -r requirements.txt
</pre>

Then create a super user
<pre>
cd src
python manage.py createsuperuser
</pre>

Fill the name,email and password and then runserver
<pre>
python manage.py runserver
</pre>

Then you are good to go.
