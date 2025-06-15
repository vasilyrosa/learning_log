# Learning Log

O **Learning Log** é uma aplicação web desenvolvida com Django que permite aos usuários registrar tópicos de estudo e fazer anotações sobre o que aprenderam em cada um deles. É ideal para acompanhar seu progresso em diferentes áreas de conhecimento.

## Funcionalidades

- Cadastro e autenticação de usuários
- Criação de tópicos de estudo personalizados
- Adição de entradas/anotações para cada tópico
- Visualização de todos os tópicos e detalhes de cada um
- Edição e exclusão de entradas (opcional)
- Interface responsiva com Bootstrap 3

## Tecnologias utilizadas

- Python 3.12
- Django 5.2
- Bootstrap 3 (django-bootstrap3)
- PostgreSQL (para deploy no Heroku)
- Gunicorn (para deploy)
- Heroku (deploy em nuvem)

## Como rodar localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/learning_log.git
   cd learning_log
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python3 -m venv ll_env
   source ll_env/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as migrações:**
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário (opcional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```

7. **Acesse no navegador:**
   ```
   http://127.0.0.1:8000/
   ```

## Deploy no Heroku

- O projeto já está preparado para deploy no Heroku, com arquivos `Procfile`, `requirements.txt` e `runtime.txt`.
- Basta criar um app no Heroku, adicionar o banco de dados Postgres e fazer o deploy.

## Estrutura do Projeto

```
learning_log/
├── learning_log/         # Configurações do projeto Django
├── learning_logs/        # App principal (tópicos e entradas)
├── users/                # App de autenticação de usuários
├── static/               # Arquivos estáticos (opcional)
├── templates/            # Templates HTML
├── requirements.txt
├── Procfile
├── runtime.txt
└── README.md
```

## Licença

Este projeto é livre para uso educacional.

---

Desenvolvido por [Everton Rosa](https://github.com/vasilyrosa)
