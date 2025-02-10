# Quorum Coding Challenge

## Installation Guide

### Clone the Repository
```sh
$ git clone https://github.com/igorpuorro/quorum-coding-challenge.git
```

### Change to Project Root Directory
```sh
$ cd quorum-coding-challenge/
```

### Create a Virtual Environment
```sh
$ python3 -m venv .venv
```

### Activate the Virtual Environment
```sh
$ source .venv/bin/activate
```

### Install Dependencies
```sh
$ pip install -r requirements.txt
```

### Change to Project Directory
```sh
$ cd quorum_project/
```

### Run Automated Setup
The token generated at the end of the setup aims to be used in Swagger UI to authorize access to restricted endpoints.
```sh
$ python manage.py setup_quorum_app
```

#### Command Output:
```sh
Running migrations...
Operations to perform:
  Apply all migrations: admin, auth, authtoken, contenttypes, quorum_app, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying authtoken.0001_initial... OK
  Applying authtoken.0002_auto_20160226_1747... OK
  Applying authtoken.0003_tokenproxy... OK
  Applying authtoken.0004_alter_tokenproxy_options... OK
  Applying quorum_app.0001_initial... OK
  Applying sessions.0001_initial... OK
Loading data...
Data loaded successfully!
Creating superuser...
Superuser created successfully!
Generating DRF token...
Generated token 099b7ffb6d74595c49c3967fcc453cfa918a4edc for user quorum
Setup completed successfully!
```

### Check for CSV Data Load Errors
Check for CSV data that failed to be loaded into the SQLite3 database.
```sh
$ cat load_data.log
```

### Run Automated Tests
```sh
$ python manage.py test quorum_app
```

### Start the Application
```sh
$ python manage.py runserver
```

### Application URLs
- **Application UI**: [http://localhost:8000/](http://localhost:8000/)
- **Django admin**: [http://localhost:8000/admin/](http://localhost:8000/admin/)
- **Swagger UI**: [http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)

### Swagger UI Authorization
The current implementation uses token-based authentication to restrict access to the endpoints under `/api/v1/model-view-set/`.

The token was provided in the "Run Automated Setup" step.

Find the **Authorize** button on the Swagger UI page ([http://localhost:8000/api/docs/](http://localhost:8000/api/docs/)). It will open a modal. In the **Value** field, enter (replace with the actual generated token):
```
Token 099b7ffb6d74595c49c3967fcc453cfa918a4edc
```
