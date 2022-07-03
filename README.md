Projeto Integrador 2 desenvolvido pelo grupo 019 - Univesp
<ul>
    <li>Agatha Chaves</li>
    <li>Ariana Maira Bezerra Marcelino</li>
    <li>Bruno Monserrat Perillo</li>
    <li>Emilia Maria dos Santos Brasilio</li>
    <li>Erick Bento Dias Ferreira</li>
    <li>Gisely Lima da Silva</li>
    <li>José Guilherme Paciléo Zanardo</li>
    <li>Taísa Salton Vieira</li>
</ul>

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
Para iniciar este projeto, após cloná-lo, entrar na página do projeto:

```
cd projeto_agenda/agenda
```
Instalar e configurar o pacote crispy_forms para uso de templates:
```
pip install django-crispy-forms
```
Incluir o app no settings.py do projeto nos seguintes campos:
```
INSTALED_APPS = [
    ...
    'crispy_forms', 
]

CRISPY_TEMPLATE_PACK = 'uni_form'
```
Agora subir o projeto com o manage:
```
python3 manage.py makemigrations 
python3 manage.py migrate
python3 manage.py runserver
```
