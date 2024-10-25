# EH PATO - IA - API

API criada para a consulta de nossa IA.

## Como rodar

Tendo instalado o [Python3](https://www.python.org/downloads/) e o [pip](https://medium.com/@nara.guimaraes/instalando-o-pip-nolinux-windows-e-macos-um-guia-passo-a-passo-cc7b6d752b31), rode na pasta do projeto:

### `pip install virtualenv` ou `apt-get install python3-virtualenv`

Para instalarmos o virtualenv, que nos permite criar um ambiente virtual.

### `virtualenv venv`

Para criarmos um ambiente virtual.

### `source venv/bin/activate`

Para entrarmos no ambiente virtual

### `pip install pandas`
### `pip install scikit-learn`
### `pip install "fastapi[standard]"`

Para instalarmos as dependências

### `fastapi run ehPato.py`

Para iniciarmos a API.
