# Guiden main app documentation
## Files and directories
- `__init__.py` - Initialize application. It's mainly responsible for:
    + load default and custom configuration
    + apply needed middleware
    + prepare connection with database server for work
    + register subapplications
- `default_configs.py` - Contains default configurations like:
    + `Config` - Standard configuration
    + `DevelopmentConfiguration` - Configuration for development purpose
- `mongo.py` - Defines MongoDB database connection and function for initialize that connection.
    + `init(app: Flask)` - Function initializing MongoDB server connection in `client` variable and database instace in `db` variable.
    + `client` - Database server client connection.
    + `db` - Database instance getted from `client`.
- `templates\` - Directory of templates uses globally in whole Guiden application.
- `static\` - Directory of static files uses globally in whole Guiden application.
    + `scss\` - Directory of SCSS files
    + `css\` - Directory of CSS files (mainly) compiled from `scss\` directory.
        - `*.scss.css` - Files compiled from `scss\` directory. In development every request runs compilation. In production compilation should be done before first start of application.
        - `*.css` - Files originally writed in CSS.
- `subapps\` - Directory containing all subapplications uses by main application.

## Subapplications
- [**home** subapplication](.\subapps\home\home.md)
    Responsible for sharing home page endpoints.

## Endpoints
<table>
    <thead>
        <tr>
            <th>Endpoint name</th>
            <th>URL rule</th>
            <th>Parameters explanation</th>
            <th>Return</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>static</code></td>
            <td><code>/static/&lt;path:filename&gt;</code></td>
            <td>
                <ul>
                    <li>
                        <b><code>path:filename</code></b>
                        <br>Path of the accessing file.
                    </li>
                </ul>
            </td>
            <td>Any file accessible from static files directory, selected by <code>filename</code> parameter.</td>
            <td>Returns file selected by <code>filename</code> parameter from static files directory.</td>
        </tr>
    </tbody>
</table>

