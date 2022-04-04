
## Formatar código
```sh
python -m black .
```
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Migrações

### Criar
`poetry run alembic revision --autogenerate -m "nome"`

### Aplicar
`poetry run alembic upgrade head`

## Autenticação
A autenticação é implementada com JWT. Apenas é necessário informar o token *Bearer*.

Há dois tipos de role: *admin* e *user*. Naturalmente, mais roles podem ser criadas, uma vez que só ficam armanezadas no token.
Há uma rota `/auth/token` para a criação de tokens, mas é necessário um token com role *admin* para utilizá-la.

Para criar um token admin, execute o comando abaixo. Os parâmetros do método `sign_jwt` são *nome*, *role* e tempo para expiração em segundos. Se for 0, o token não expira.

`python -c "from app.services.dependencies.auth.auth_handler import sign_jwt; print(sign_jwt('admin', 'admin', 0))"`

Não esqueça de definir a variável de ambiente JWT_SECRET antes de gerar qualquer token. Um secret pode ser gerado com o seguinte comando:

`openssl rand -base64 32`

## Testes

### Executar testes
`poetry run pytest`

### Executar testes com cobertura
`poetry run pytest --cov-report term-missing --cov=app`