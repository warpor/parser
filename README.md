## Начальная настройка
Необходимо переименовать `.env_example` в `.env` и  `.env_tests_example` в `.env_tests`



## Запуск
Для запуска  необходимо выполнить комманду

```
docker compose -f docker-compose.yml up
```

После запуска api дооступно по адресу http://localhost:8000/docs

## Запуск тестов
Перед запуском тестов стоит удалить запущенные контейнеры
```
docker compose -f docker-compose.test.yml --profile tests down  
```
Для  запуска тестов сервиса web parser

```
docker compose -f docker-compose.test.yml up web_parser_tests --abort-on-container-exit
```

Для  запуска тестов сервиса urls service
```
docker compose -f docker-compose.test.yml up web_parser_tests --abort-on-container-exit
```
После проверки  тестов запущенные контейнеры нужно удалить
```
docker compose -f docker-compose.test.yml --profile tests down  
```

