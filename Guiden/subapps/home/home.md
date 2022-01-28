# Home subapplication documentation
## Files and directories
- `__init__.py` - Initializes `home` subapplication and registers endpoints with views from `views.py` file.
- `views.py` - Defines views for `home` subapplication.
- `\templates` - Contains templates for `home` subapplication.

## Endpoints
All endpoint names for this application starts with `home.*`. For example below endpoint names would look like `.endpoint_name` and that means the full endpoint name is `home.endpoint_name`.
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
            <td rowspan="2"><code>home.home</code></td>
            <td><code>/</code></td>
            <td rowspan="2">&#10134</td>
            <td rowspan="2">HTML rendered template</td>
            <td rowspan="2">
                Renders and returns home page from <code>home.j2</code> template.
                <br>Home page is application main page.
            </td>
        </tr>
        <tr>
            <td><code>/home</code></td>
        </tr>
    </tbody>
</table>
