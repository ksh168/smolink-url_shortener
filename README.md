# url_shortener


This is a simple **URL shortener** in Flask.

Shortens URL upto length 512 characters to 6 characters.

Made using Flask-SQLAlchemy. This URL shortener will be able to redirect links and keep stats on the number of times each link was visited.

Also has **[HTTP Basic Authentication](https://web.archive.org/web/20190128010144/http://flask.pocoo.org/snippets/8/)** to view stats.

**All this data will be stored in a [sqlite3](https://www.sqlite.org/index.html) database**


* **"link" Table in the Database**
<img src="https://github.com/ksh168/url_shortener/blob/master/link%20table.png" width="50%" height="50%">


# Steps:

Always recommended to create a virtual environment

* creates **virtual environment** and install flask

	```pipenv install flask```

* to **start shell** and enter the venv

	```pipenv shell```

* **Dependencies:**

	```pipenv install python-dotenv```

	```pipenv install sql-alchemy```

* To **run the app**

	```flask run```


# Now to create the database
1. start python in terminal

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
	SELECT * FROM link
	```

* To exit sqlite3

	```sql
		.exit
	```





This project was made using [GitHub Codespaces Beta](https://github.com/features/codespaces).

Thanks to [Anthony](https://github.com/PrettyPrinted) and [Bulma](https://bulma.io/).
