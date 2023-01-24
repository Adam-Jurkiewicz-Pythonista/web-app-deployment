# web-app-deployment
How to easily deploy Flask or fastAPI on Deta.sh

Tutorial based on: https://fastapi.tiangolo.com/deployment/deta/

- w katalogu `fastapideta` wykonać:
```
$ deta new        
```
Wówczas automatycznie kod zostanie wysłany do serwisu.
``` ✔ 
Successfully created a new micro
{
        "name": "fastapideta",
        "id": "e33db508-dc5a-4aae-86da-b52ea9e1aefe",
        "project": "a0pz7w55",
        "runtime": "python3.9",
        "endpoint": "https://z6mjyg.deta.dev",
        "region": "eu-central-1",
        "visor": "disabled",
        "http_auth": "disabled"
}
Adding dependencies...
Collecting fastapi
  Downloading https://files.pythonhosted.org/packages/8f/89/adf4525d1870021b65ec562e83e9f46d96494ad95f238d0264ef1ab6b604/fastapi-0.89.1-py3-none-any.whl (55kB)
Collecting pydantic!=1.7,!=1.7.1,!=1.7.2,!=1.7.3,!=1.8,!=1.8.1,<2.0.0,>=1.6.2
  Downloading https://files.pythonhosted.org/packages/36/78/1755a9fe87b0480775bce2e812049669adbe4b006787257d288806caa580/pydantic-1.10.4-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.2MB)
Collecting starlette==0.22.0
  Downloading https://files.pythonhosted.org/packages/1d/4e/30eda84159d5b3ad7fe663c40c49b16dd17436abe838f10a56c34bee44e8/starlette-0.22.0-py3-none-any.whl (64kB)
Collecting typing-extensions>=4.2.0
  Downloading https://files.pythonhosted.org/packages/0b/8e/f1a0a5a76cfef77e1eb6004cb49e5f8d72634da638420b9ea492ce8305e8/typing_extensions-4.4.0-py3-none-any.whl
Collecting anyio<5,>=3.4.0
  Downloading https://files.pythonhosted.org/packages/77/2b/b4c0b7a3f3d61adb1a1e0b78f90a94e2b6162a043880704b7437ef297cad/anyio-3.6.2-py3-none-any.whl (80kB)
Collecting sniffio>=1.1
  Downloading https://files.pythonhosted.org/packages/c3/a0/5dba8ed157b0136607c7f2151db695885606968d1fae123dc3391e0cfdbf/sniffio-1.3.0-py3-none-any.whl
Collecting idna>=2.8
  Downloading https://files.pythonhosted.org/packages/fc/34/3030de6f1370931b9dbb4dad48f6ab1015ab1d32447850b9fc94e60097be/idna-3.4-py3-none-any.whl (61kB)
Installing collected packages: typing-extensions, pydantic, sniffio, idna, anyio, starlette, fastapi
Successfully installed anyio-3.6.2 fastapi-0.89.1 idna-3.4 pydantic-1.10.4 sniffio-1.3.0 starlette-0.22.0 typing-extensions-4.4.0
You should consider upgrading via the 'pip install --upgrade pip' command.
```