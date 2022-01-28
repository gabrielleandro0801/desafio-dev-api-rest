# API

## Pré requisitos para execução do projeto
- Ter o Docker instalado

## Executar a API
``` bash
docker-compose build && docker-compose up
```

## Rotas

### Portadores

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
    "userId": 1 (id único para o portador)
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

### Contas

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
    "message": "Account successfully created",
    "data": {
        "accountId": 1,
        "accountNumber": 446972,
        "bankBranch": "0001",
        "withdrawDailyLimit": 2000.0
    }
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
    "userId": 2
}
```

Response - 200
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

Response - 200
``` json
{
    "message": "The account has been successfully locked"
}
```

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

Response - 200
``` json
{
    "message": "The account has been successfully unlocked"
}
```

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

### Transações

### Realizar Depósito
**POST /v1/accounts/transactions**

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

Response - 400
``` json
{
    "message": "The status of the account does not allow transactions"
}
```

### Materiais de consulta
[Link 1](https://ichi.pro/pt/criar-e-preencher-um-banco-de-dados-postgres-com-docker-compose-247804571125807)

[Link 2](https://www.youtube.com/watch?v=b6pYcTr4pCs)

[Link 3](https://vsupalov.com/flask-sqlalchemy-postgres/)
