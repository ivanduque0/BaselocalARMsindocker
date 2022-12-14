import requests
ka=[2,3]
try:
    ka.index(5)
    request_json = requests.get(url=f'https://webseguricel.up.railway.app/obtenerusuariosapi/orangepi2g/', auth=('27488274', 'CkretoxDxdxdXd'), timeout=3).json()
except requests.exceptions.ConnectionError:
    print("funciona")