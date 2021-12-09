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
`git clone https://github.com/tlendev/foodchain-api.git`

2. Enter into cloned repository directory (usually by `cd foodchain-api`)

- If you want to use virtual environment activate it before steps below

3. Run `pip3 install -r requirements.txt` to install required python packages

4. Go to [Configuration](#Configuration) and configure application via environment variables (and/or by creating `.env` file) or in config file setted by `GUIDEN_CFG` enviroment variable.

## Configuration
### Which configuration are required?
- `FLASK_RUN_PORT`
- `FLASK_RUN_HOST`
- `FLASK_ENV`
- `FLASK_APP`
- `SECRET_KEY` - Recommended in production for safety reasons
### Enviroment variables only configuration
Entire configuration below you can do only by creating and modifying below environment
variables or putting them into `.env` file.

- `FLASK_RUN_PORT = <port>`
    <br>(Optional) [[default: `5000`]]
    <br>Port from which you want to starts app

- `FLASK_RUN_HOST = <host>`
    <br>(Optional) [[default: `127.0.0.1`]]
    <br>Host from which you want to starts app

- `FLASK_ENV = <development/production>`
    <br>(Optional) [[default: `production`]]
    <br>In development process (only) you want set this to "development"

- `FLASK_APP = FoodChainAPI`
    <br>**Required if you running app by `'flask run'` command**
    <br>App main package. If you need to modify this value, that means you
    propably changed something for your own risk.

- `GUIDEN_CFG = <Configuration file path>`

### Other configuration options

- `SECRET_KEY = "<Random secret key>"`
    <br>**(Optional)** [*By default application use constant predefined key*]
    <br>Secret Key for application instance. **In production we recommend to provide it and keep it in secret.**
    <br>**It's recommended to set this value via environment variables instead of config file.**

- `MONGO_HOST = "<Database connection host address>"`
    **(Optional)** <br>[*Default: "localhost"*]
- `MONGO_PORT = "<Database connection port>"`
    **(Optional)** <br>[*Default: "27017"*]
- `MONGO_USER = "<Database authentication username>"`
    **(Optional)**
- `MONGO_PASS = "<Database authentication password>"`
    **(Optional)**
- `MONGO_DBNAME = "<Database name>`
    **(Optional)** <br>[*Default: "Guiden"*]
- `MONGO_OPTS = "<Database connection options>`
    **(Optional)**
## Run in development
Simply just run command below in main repository location

### Method A - By `flask` command
```bash
flask run
```

## Run in production
For now, try to guide with
[this site](https://flask.palletsprojects.com/en/2.0.x/deploying/index.html). Currently we are not sure whether our application can be properly runned in production by default.

Propably in the future we will provide support and own guide for this.

If you need to import main flask app file into wsgi probably it would be this
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
