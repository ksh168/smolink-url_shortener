# URL_Shortener - smolink

This project was born out of my curiosity for how URL Shorteners work.

This is a simple **URL shortener** in Flask.

Shortens URL upto length 512 characters to 6 characters.

Made using Flask-SQLAlchemy. This URL shortener will be able to redirect links and keep stats on the number of times each link was visited.

Also has **[HTTP Basic Authentication](https://web.archive.org/web/20190128010144/http://flask.pocoo.org/snippets/8/)** to view stats.

**All this data will be stored in a [sqlite3](https://www.sqlite.org/index.html) database**


* **"link" Table in the Database**
<img src="https://github.com/ksh168/url_shortener/blob/master/link%20table.png" width="50%" height="50%">




## User Interface

* **Index page**
<img src="https://raw.githubusercontent.com/ksh168/url_shortener/master/screenshots/Index.png">

* **Short URL generated**
<img src="https://raw.githubusercontent.com/ksh168/url_shortener/master/screenshots/short%20url%20generated.png">

* **Statistics (Needs HTTP Authentication)**
<img src="https://raw.githubusercontent.com/ksh168/url_shortener/master/screenshots/stats.png">



## Steps:

Always recommended to create a virtual environment

* Create **virtual environment** and install flask

	```pipenv install flask```

* To **start shell** and enter the venv

	```pipenv shell```

* **Dependencies:**(this step might not be needed)

	```pipenv install python-dotenv```

	```pipenv install sql-alchemy```

* To **run the app**

	**start shell** if not started
	```pipenv shell```
	
	```flask run```


### Now to create the database
1. Start python in terminal

	```python```

2.
	```python
		from url_shortener import create_app
	```

3.
	```python
		from url_shortener.extensions import db
	```

4.
	```python
		from url_shortener.models import Link
	```

5. **To create tables and database**

	```python
		db.create_all(app = create_app())
	```

6. To exit python console

	```python
		exit()
	```


* To **view database**, write in terminal

	`sqlite3 url_shortener/db.sqlite3`

* To **see the table names** in database

	```sql
		.tables
	```


* To **query the database**

	```sql
	SELECT * FROM link;
	```
* To **delete table contents but not table**

	```sql
	DELETE FROM link;
	```

* To exit sqlite3

	```sql
		.exit
	```


## Contributing [Currently open for OSF, NIT Warangal participants only]

* First off, thank you for considering contributing.

* There are many ways to contribute, from improving the documentation, submitting bug reports and feature requests or writing code which can be incorporated into project itself.

* Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

* Please make sure to update tests as appropriate.

* You can also edit the readme and make it more user friendly to help out new contributors.


### Link to resources for first timers:

* Working on your first Pull Request? You can learn how from this *free* series, [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github).

* Friendly tutorial: http://makeapullrequest.com/

* Feel free to ask for help; everyone is a beginner at first :smile_cat:


### Submitting a pull request
* The smaller the proposed change, the better. If you’d like to propose two unrelated changes, submit two pull requests.

* The more information, the better. Make judicious use of the pull request body. Describe what changes were made, why you made them, and what impact they will have for users.

* If this is your first pull request, it may help to understand [GitHub Flow](https://guides.github.com/introduction/flow/).

* Including screenshots/video of final interface/changes in your pull request is a must.

## Community
* You can chat with the community [here]().


## Acknowledgements

This project was made using **[GitHub Codespaces Beta](https://github.com/features/codespaces)**. Thanks to them for providing me early access to their such beautiful and useful feature.
