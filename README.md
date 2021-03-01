#  Desenvolvimento
**Pré Requisitos**
- Python3.8
- [Pipenv](https://pypi.org/project/pipenv/)
- [Google Key](https://developers.google.com/maps/documentation/javascript/get-api-key)

##  Instalação
Após clonar o projeto, com o *pipenv* instalado, execute o comando de instalação na pasta raiz
```
pipenv install
```

**Ativar ambiente de desenvolvimento**

```
pipenv shell
```

**Variáveis de ambiente**
- Copie o *.env.example* e renomei para *.env*
- Insira os dados do banco de dados
- Insira a credencial do google em **GOOGLE_KEY**
- Gere a chave do sistema e insira em SECRET_KEY:
```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

**Executando**
```
python manage.py runserver
```

**Testes**

```
python manage.py test
```
