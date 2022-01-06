# Guiden
## Technology stack
- Python
- Flask
- MongoDB

## Dependencies:
- Python 3.10.1 or higher
- MongoDB server 4.4.6
- Python packages described in [`requirements.txt`](requirements.txt) file

## Basic instalation
1. Clone this repository:
`git clone https://github.com/EnderASz/Guiden.git`

2. Enter into cloned repository directory (usually by `cd Guiden`)

- If you want to use virtual environment activate it before steps below

3. Run `pip3 install -r requirements.txt` to install required python packages

4. Go to [Configuration](#Configuration) and configure application via environment variables (and/or by creating `.env` file) or in config file setted by `GUIDEN_CFG` enviroment variable.

## Configuration
### Enviroment variables only configuration
Entire configuration below can be done only by creating and modifying below environment
variables or putting them into `.env` file.
|Variable name|Default value|Optional|Description|
|-------------|-------------|--------|-----------|
|FLASK_RUN_PORT|`5000`|:white_check_mark:|Port from which you want to publish app|
|FLASK_RUN_HOST|`localhost`|:white_check_mark:|Host address from which you want to starts app|
|FLASK_ENV|`production`|:white_check_mark:|In development process (only) probably you want set this to `development`. In production it's recommended to set this to `production`.
|FLASK_APP|:heavy_minus_sign:|If you running app by `flask run`|That should be set to `Guiden` - Application main package
|GUIDEN_CFG|:heavy_minus_sign:|:white_check_mark:|Application configuration file path

### Other configuration options
|Variable name|Default value|Optional|Description|
|-------------|-------------|--------|-----------|
|SECRET_KEY|By default application use constant predefined key|:white_check_mark:|Secret Key for application instance.<br>**In production we recommend to provide it and keep it in secret.**
|MONGO_HOST|`localhost`|:x:|Database server host address|
|MONGO_PORT|`27017`|:x:|Database server port number|
|MONGO_USER|:heavy_minus_sign:|:white_check_mark:|Database server authentication username|
|MONGO_PASS|:heavy_minus_sign:|:white_check_mark:|Database server authentication password|
|MONGO_DBNAME|`Guiden`|:x:|Uses database name|
|MONGO_OPTS|:heavy_minus_sign:|:white_check_mark:|Database server connection options|

## Run in development
Simply just run command below in the main repository location
```bash
flask run
```

## Run in production
For now, try to guide with
[this site](https://flask.palletsprojects.com/en/2.0.x/deploying/index.html). Currently we are not sure whether our application can be properly runned in production by default.

Propably in the future we will provide support and own guide for this.

If you need to import main flask app file into WSGI probably it would be this
same package, which is pointed by `FLASK_APP` enviroment variable.

## CLI commands
### Help
To check availble app CLI commands simply run below command:
```cmd
flask --help
```

### Run application through flask CLI command
Look here:
[Flask documentation - Run the Development Server](https://flask.palletsprojects.com/en/2.0.x/cli/#run-the-development-server)

### Run python shell with app context
Look here:
[Flask documentation - Open a Shell](https://flask.palletsprojects.com/en/2.0.x/cli/#open-a-shell)

### Show application routes and endpoints
To show application url routes and endpoints simply run below command:
```cmd
flask routes
```
That command should show you a table design like the one below:
|Endpoint|Methods|Rule
|--------|-------|----
|`[subapp.]endpoint_name`|`METHOD_NAME`|`/url/rule/<parameter_type:parameter>`|
|`static`|`GET`|`/static/<path:filename>`|
|`home.home`|`GET`|`/home`|
|`home.home`|`GET`|`/`|
|...|...|...

## Application structure and functionality documentation
Application structure and functionality documentation is available [here](./Guiden/Guiden.md).
