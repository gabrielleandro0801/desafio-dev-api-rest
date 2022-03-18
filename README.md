<h1 align="center">Dock API</h1>

<div id="pre_requisitos">
    <h2 align="left">Pré requisitos para execução do projeto</h2>
    <p>Ter o <a href="https://docs.docker.com/get-docker/">Docker</a> instalado</p>
</div>

<div id="execucao">
    <h2 align="left">Executar a API</h2>
</div>

``` shell
docker-compose build && docker-compose up
```

<div id="rotas">
    <h2 align="center">Rotas</h2>
</div>

<div id="portadores">
    <h3 align="center">Portadores</h3>
</div>

### Criar Portador
**POST /v1/users**

Request
``` json
{
    "name": "Marcos",
    "doc": "00011122233"
}
```

Response - 201
``` json
{
    "message": "User successfully created",
    "id": 1
}
```

Response - 422
``` json
{
    "message": "There is already a user using this document"
}
```

### Deletar Portador
**DELETE /v1/users/{userId}**

Response - 204

Response - 404
``` json
{
    "message": "User not found"
}
```

<div id="contas">
    <h3 align="center">Contas</h3>
</div>

### Criar Conta
**POST /v1/accounts**

Request
``` json
{
    "userId": 2
}
```

Response - 201
``` json
{
    "accountId": 1,
    "accountNumber": 446972,
    "bankBranch": "0001",
    "withdrawDailyLimit": 2000.0
}
```

Response - 422
``` json
{
    "message": "This account already exists"
}
```

Response - 404
``` json
{
    "message": "User not found"
}
```

### Consultar Conta
**GET /v1/accounts/{accountId}**

Response - 200
``` json
{
    "status": "ACTIVE",
    "accountNumber": 446972,
    "bankBranch": "0001",
    "transferDailyLimit": 2000.0,
    "balance": 2853.75,
    "userId": 2
}
```

Response - 404
``` json
{
    "message": "Account not found"
}
```

### Deletar Conta
**DELETE /v1/accounts/{accountId}**

Response - 204

Response - 404
``` json
{
    "message": "Account not found"
}
```

Response - 409
``` json
{
    "message": "The account must be active in order to be closed"
}
```

### Bloquear Conta
**POST /v1/accounts/{accountId}/lock**

Response - 204

Response - 404
``` json
{
    "message": "Account not found"
}
```

Response - 409
``` json
{
    "message": "The account must be active in order to be locked"
}
```

### Desbloquear Conta
**DELETE /v1/accounts/{accountId}/lock**

Response - 204

Response - 404
``` json
{
    "message": "Account not found"
}
```

Response - 409
``` json
{
    "message": "The account must be locked in order to be unlocked"
}
```

<div id="transacoes">
    <h3 align="center">Transações</h3>
</div>

### Realizar Depósito
**POST /v1/transactions**

Request
``` json
{
    "accountId": 2,
    "operationType": "DEPOSIT",
    "amount": 150.50
}
```

Response - 201
``` json
{
    "message": "Transaction successfully performed"
}
```

Response - 422
``` json
{
    "message": "The status of the account does not allow transactions"
}
```

Response - 404
``` json
{
    "message": "Account not found"
}
```

### Realizar Saque
**POST /v1/transactions**

Request
``` json
{
    "accountId": 2,
    "operationType": "WITHDRAW",
    "amount": 150.50
}
```

Response - 201
``` json
{
    "message": "Transaction successfully performed"
}
```

Response - 422
``` json
{
    "message": "The status of the account does not allow transactions"
}
```

Response - 422
``` json
{
    "message": "This withdraw will surpass the daily limit"
}
```

Response - 422
``` json
{
    "message": "This account does not have enough balance"
}
```

Response - 404
``` json
{
    "message": "Account not found"
}
```

### Consultar Extrato
**GET /v1/transactions/{accountId}**

Query Param | Obrigatório | Tipo | Restrições
------ | ------ | ------ | ------
page | Não | Inteiro | Valores mínimo e máximo: 0 e 50
limit | Não | Inteiro | Valores mínimo e máximo: 0 e 50
from | Não | Date ISO-8601 |
to | Não | Date ISO-8601 | 

Response - 200
``` json
{
    "previousPage": null,
    "currentPage": 0,
    "nextPage": null,
    "last": true,
    "totalPages": 1,
    "totalItems": 3,
    "maxItemsPerPage": 50,
    "totalItemsPage": 3,
    "items": [
        {
            "id": 1,
            "date": "2022-01-28T19:40:01.972200",
            "value": 450.0,
            "operationType": "DEPOSIT"
        },
        {
            "id": 2,
            "date": "2022-01-28T19:40:05.588400",
            "value": 550.0,
            "operationType": "DEPOSIT"
        },
        {
            "id": 3,
            "date": "2022-01-28T19:40:09.965900",
            "value": 125.0,
            "operationType": "DEPOSIT"
        }
    ]
}
```

Response - 404
``` json
{
    "message": "Account not found"
}
```

<div id="execucao">
    <h2 align="left">Materiais de Consulta</h2>
    <a href="https://ichi.pro/pt/criar-e-preencher-um-banco-de-dados-postgres-com-docker-compose-247804571125807">Docker Compose + Postgres</a><br>
    <a href="https://www.youtube.com/watch?v=b6pYcTr4pCs">Python + Postgres</a><br>
    <a href="https://vsupalov.com/flask-sqlalchemy-postgres/">SQLAlchemy</a>
</div>
