# Django API with GraphQL

## How to setup this project

- Step 1: Start virtualenv
	```shell
	$ source graphqlenv/bin/activate
	```
- Step 2: Migrate Django app
	```shell
	$ python manage.py makemigrations
	$ python manage.py migrate
	```
- Step 3: Create a super user for demo.
	```shell
	$ python manage.py createsuperuser
	admin / django@123
	```

- Step 4: Run project.
	```shell
	$ python manage.py runserver
	```


## How to test this project
- Be sure you added some data in Django admin (http://127.0.0.1:8000/admin)
- Try the first GraphQL query: http://127.0.0.1:8000/graphql/
	```javascript
		query{
		  allProducts{
		    id,
		    title,
		    description
		  }
		}
	```

	// Result:
	```javascript
	{
	  "data": {
	    "allProducts": [
	      {
	        "id": "1",
	        "title": "iPhone 8",
	        "description": "iPhone 8, 64GB"
	      }
	    ]
	  }
	}
	```

	// Single product
	```javascript
	query{
	  product(id:1){
	    title
	  }
	}
	```
	// Result:
	```javascript
	{
	  "data": {
	    "product": {
	      "title": "iPhone 8"
	    }
	  }
	}
	```
