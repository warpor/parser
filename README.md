## Зависимости
Для запуска контейнеров нужен `docker-compose v2.x.x.`

## Начальная настройка
Необходимо переименовать `.env_example` в `.env` и  `.env_tests_example` в `.env_tests`

## Запуск
Для запуска  необходимо выполнить комманду

```
docker compose -f docker-compose.yml build
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
## CI  
В проекте настроен CI и при каждом push и pull request код проверяется `mypy`(проверяется только папка `microservices`) и `flake8`.  
После проверки кода запускаются тесты для микросервисов.

# Описания проекта
![изображение](https://github.com/user-attachments/assets/5a923b65-2761-4f22-9c61-c5e757b806ee)  
`urls_service` - API для работы с приложением.  
`rabbit mq` - Хранит сообщения для работы web_parser_service. Сообщения содержат: url для старта, на какую глубину делать обход, количество одновременно загружаемых страниц.  
`web_parser_service` - Воркер, который читает сообщения из очереди и после обработки записывает их в БД.  
`mongo-db` - Бд для хранения.  

1. В `mongo-db` создан уникальный индекс на url, поэтому в `web_parser_service` не выполняется проверка на то, посещали уже эту страницу или нет. Если уже посещали, то в базу просто не добавится.
2. При обработке страниц в `web_parser_service` в файле `microservices/web_parser_service/config.json` задается параметр `mongo_batch_size`. Это параметр указывает, сколько значений в базу за раз мы будем отправлять. Значение выбрано +- случайно, для выставления корректного значения, нужно проводить нагрузочное тестирование.
3. Информация с web_parser_service логируется в папку `/logs/web_parser`
4. В роуте `/pages` для поиска используются параметры `title` и `url`. Если указаны оба поля, то поиск будет использовать ЛО "И", т.е. на выводе будут поля, удовлетворяющие обоим условиям.
5. В роуте `/pages` при указании параметров `title` или `url` для поиска используются регулярные выражения, и выводятся значения, которые содержат строку из параметра. К примеру, для параметра "example", могут быть следующие выводы: "eeexample", "example1", "eeexample2"

описание параметров из `microservices/web_parser_service/config.json`:  
  `request_timeout_in_seconds` - максимальное ожидание для запроса.  
  `max_timeout_is_seconds` - максимальное ожидание для задачи получения html страницы, перекрывает все другие параметры.   
  `retries_count` - количество повторных подключений для страницы.  
  `mongo_batch_size` - количество записей, одновременно добавляемых в бд.  
  `headers` - загаловки для запроса  


