# frexco_desafio2
![Interface  cadastro](https://user-images.githubusercontent.com/82342478/159362207-b056002b-8c75-4dd7-880b-3cb9b36fc6b5.png)
<img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
<img alt="Django" src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/> 
<a target="blank" href=https://www.linkedin.com/in/juliano-xavier-06a0b3161/><img alt=”Linkedin” src="https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white"/>
   </a>
   
### Desafio: 
Construir pelo menos dois endpoints utilizando Django:
  - Cadastrar usuário, fornecendo o login, senha e data de nascimento
  - Senha deixar como opcional, se não fornecido gerar uma senha aleatória.
  - Consultar usuários cadastrados.
  - Deve ser possível consultar em XLSX, CSV ou JSON.

### Inicializando
Requesitos: 
- Python , venv

```Para inicializar locamente 
Clone esse repositorio: 
$ git clone https://github.com/zycki-gif/frexco_desafio2.git
```

```
#Na pasta local abra o terminal e execute: 
$ python -m venv venv
$ source venv/Scripts/activate
$ python manage.py makemigrations api
$ python manage.py migrate api
$ python manage.py runserver
```


```
# Rodando Localmente

Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
Django version 3.2.6, using settings 'api_config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Usando
```
- Abra seu navegador e va para localhost:8000
- Preencha os campos obrigatorios
- Selecione o tipo do arquivo para download
```
![format type](https://user-images.githubusercontent.com/82342478/159363102-af487246-0589-416d-9542-bdabfebe502e.png)


