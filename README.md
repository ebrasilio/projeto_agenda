<h2>prj_agenda</h2>

Como criar ambiente de desenvolvimento, crie a pasta do projeto e dentro dela crie o ambiente virtual:
``` 
mkdir projeto_agenda
cd projeto_agenda/
python3  -m venv env
source env/bin/activate
```

(para fechar a virtual env digite deactivate)

 instalar o Django:
```
pip3 install django
```
Para inicializar o projeto:
```
django-admin startproject agenda 
cd agenda
```
O projeto se chama agenda e dentro dele vamos inicializar os apps 
```
cd agenda

django-admin startapp agenda
django-admin startapp agendador
django-admin startapp accounts

```
<h2>Rodar projeto após git-clone:</h2>
Para iniciar este projeto, após cloná-lo como ele está:

```
cd projeto_agenda/agenda

python3 manage.py makemigrations 
python3 manage.py migrate
python3 manage.py runserver
```

