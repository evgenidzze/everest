# Build
### docker-compose up --build
 - If unhealthy - repeat docker-compose up

# Dump
$ docker exec -i welcome-to-docker-db-1 mysql -u root -proot market > docker-entrypoint-initdb.d/init_db.sql
_____________________________________________________________________________________________________

# JSON-RPC API для отримання статусу замовлення

Цей JSON-RPC API надає можливість отримати статус замовлення за номером замовлення. Для взаємодії з API потрібна авторизація.

## Авторизація

Авторизація здійснюється за допомогою базової авторизації. Ви повинні передавати дані авторизації у заголовку запиту.

Прямий доступ до API без авторизації заборонений.

## Запит

Запит на отримання статусу замовлення має бути зроблений методом POST до URL-шляху `/api`.

Ваш запит повинен містити JSON-RPC об'єкт у тілі запиту:

```json
{
  "jsonrpc": "2.0",
  "method": "get_order_status",
  "params": {
    "order_num": 1
  },
  "id": 1
}
```
## Відповідь
У відповіді ви отримаєте JSON-RPC об'єкт зі статусом замовлення:

```json
{
  "jsonrpc": "2.0",
  "result": "PROCESSING",
  "id": 1
}
```

Якщо статус замовлення неможливо отримати або відбулася помилка, ви отримаєте відповідь з помилкою:
```json
{
  "jsonrpc": "2.0",
  "error": {
    "code": 401,
    "message": "Authentication required"
  },
  "id": 1
}
```
