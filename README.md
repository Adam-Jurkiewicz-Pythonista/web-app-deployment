# web-app-deployment
How to easy deploy Flask or fastAPI on Deta.sh

- Command `deta new` in directory `flaskdeta`:
```
Successfully created a new micro
{
        "name": "flaskdeta",
        "id": "501bf3ca-c1ec-4caf-bd11-337719a0a3a7",
        "project": "a0pz7w55",
        "runtime": "python3.9",
        "endpoint": "https://4gkjc9.deta.dev",
        "region": "eu-central-1",
        "visor": "disabled",
        "http_auth": "disabled"
}
Adding dependencies...
Collecting flask
  Downloading https://files.pythonhosted.org/packages/0f/43/15f4f9ab225b0b25352412e8daa3d0e3d135fcf5e127070c74c3632c8b4c/Flask-2.2.2-py3-none-any.whl (101kB)
Collecting itsdangerous>=2.0
  Downloading https://files.pythonhosted.org/packages/68/5f/447e04e828f47465eeab35b5d408b7ebaaaee207f48b7136c5a7267a30ae/itsdangerous-2.1.2-py3-none-any.whl
Collecting Jinja2>=3.0
  Downloading https://files.pythonhosted.org/packages/bc/c3/f068337a370801f372f2f8f6bad74a5c140f6fda3d9de154052708dd3c65/Jinja2-3.1.2-py3-none-any.whl (133kB)
Collecting Werkzeug>=2.2.2
  Downloading https://files.pythonhosted.org/packages/c8/27/be6ddbcf60115305205de79c29004a0c6bc53cec814f733467b1bb89386d/Werkzeug-2.2.2-py3-none-any.whl (232kB)
Collecting click>=8.0
  Downloading https://files.pythonhosted.org/packages/c2/f1/df59e28c642d583f7dacffb1e0965d0e00b218e0186d7858ac5233dce840/click-8.1.3-py3-none-any.whl (96kB)
Collecting importlib-metadata>=3.6.0; python_version < "3.10"
  Downloading https://files.pythonhosted.org/packages/26/a7/9da7d5b23fc98ab3d424ac2c65613d63c1f401efb84ad50f2fa27b2caab4/importlib_metadata-6.0.0-py3-none-any.whl
Collecting MarkupSafe>=2.0
  Downloading https://files.pythonhosted.org/packages/06/3b/d026c21cd1dbee89f41127e93113dcf5fa85c6660d108847760b59b3a66d/MarkupSafe-2.1.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
Collecting zipp>=0.5
  Downloading https://files.pythonhosted.org/packages/d8/20/256eb3f3f437c575fb1a2efdce5e801a5ce3162ea8117da96c43e6ee97d8/zipp-3.11.0-py3-none-any.whl
Installing collected packages: itsdangerous, MarkupSafe, Jinja2, Werkzeug, click, zipp, importlib-metadata, flask
Successfully installed Jinja2-3.1.2 MarkupSafe-2.1.2 Werkzeug-2.2.2 click-8.1.3 flask-2.2.2 importlib-metadata-6.0.0 itsdangerous-2.1.2 zipp-3.11.0
You should consider upgrading via the 'pip install --upgrade pip' command.
```