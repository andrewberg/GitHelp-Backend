# GitHelp-Backend

##### Contributers: Andrew Berg, Joy Bushnell, Jared Kraemer


This project will be used to store the lessons and other materials used in the GitHelp app for ios. The project will be composed of a MYSQL database that stores JSON objects and will use Flask to setup routes and to access the database.


Material from lesson tutorials used from: 
 [https://git-scm.com/](https://git-scm.com/ "Git command reference")


iOS backend written in Python using Flask<br />
<br />
Usage:<br />
*** Assumes starting in cloned GitHelp-Backend directory ***
*** APP FUNCTIONS WITHOUT THIS IF YOU DO NOT WANT TO GO THROUGH TROUBLE OF SERVER CONFIG ***
*** https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-16-04 DO THIS FIRST ***
1. Open up a UNIX-based command line terminal.<br />
2. Go through process of having Python2.7, most Linux distros come with preinstalled.<br />
3. To install python: sudo add-apt-repository ppa:fkrull/deadsnakes-python2.7 <br />
sudo apt-get update 
sudo apt-get install python2.7
4. Navigate to the directory of the download leaderboards files.
5. Do: sudo pip install --upgrade pip setuptools<br />
6. Do: sudo pip install virtualenv<br />
7. Do: virtualenv flask
Creates a flask virtual environment
8. Do: source ./flask/bin/activate
This opens the virtual environment
9. Do: pip install flask
This will install flask framework
11. Do: sudo apt-get install python-pip python-dev libmysqlclient-dev
12. Do: pip install mysqlclient
13. Do: cd ./sql
14. Do: mysql -u root -p PASSWORD YOU CREATED WHEN INSTALLING MYSQL
15. Do: source create_new.sql
16. Do: quit
17. Do: cd ../
18. Do: python parse_lessons.py
19. Do: python parse_quizzes.py
20. Do: flask ./flask/git-help-main.py
21. Do: python ./flask/git-help-main.py
22. You should receive this: <br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)<br />
23. You will now be able to locally access the server API by IP, 127.0.0.1:5000.<br />
    Example: 127.0.0.1:5000/jmt/typingtest/list will list the leaderboards for the TypingTest.<br />
24. In the GitHelp project, change the IPs in the APIResources.swift to http://127.0.0.1:5000/lessons<br />
  instead of http://45.55.51.127/lessons.json if you want to run the system on your local machine.<br />
25. In the GitHelp project, change the IPs in the APIResourcesQuiz.swift to http://127.0.0.1:5000/quizzes<br />
  instead of http://45.55.51.127/quizzes.json if you want to run the system on your local machine.<br />
26. You can use deactivate to get out of the virtualenv flask