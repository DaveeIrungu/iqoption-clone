this is for you. you will be updating it..
this is not markdown, lol;

** SETUP **
1. ensure you have python 3.6 installed.
2. create a virtualenv environment called venv
	virtualenv venv
3. activate the virtualenv
	venv\scripts\activate
4. install the requirements inside venv, warning- if you install requirements without activating venv,
they are installed globally, which risk messing other libraries, (you'll know what am talking about when you have
10 projects in your computer with different requirements).
5. you are set up. a quick overview of the layout.
    /backend
	/app
	    /routes  #put views in this folder
	    /sockets #will put websocket logic here
	    /templates	#incase of any templates
	    __init__.py #entry point
           #since I'll be using API, it gets easier. for you.

        /frontend
	   #this will contain JS. communication will be through API, so get familiar with flask API.
	   #it is easier than you think.
    *when you are new to flask, you tend to put all your logic in one place, coz you probably 
     haven't heard about blueprints, or you are still new to MVC logic. dont worry, work your way,
     we'll correct here and there, as you teach me also ;).


***********************************************************************************************************************
Note that the routes.py cannot access the app folder in the directory
Hence, it cannot access the forms (login and sign up) that I've created and the variables/methods within the form classes
That's the only setback so far
