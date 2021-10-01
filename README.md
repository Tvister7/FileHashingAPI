<img src="https://img.shields.io/badge/fastapi-0.68.1-success">  <img src="https://img.shields.io/badge/postgres-12-blue">  <img src="https://img.shields.io/badge/python-3.9-critical">

# Описание

FastAPI+Celery приложение для вычисления md5 хэшей от произвольных файлов.

<hr>
# Инструкция по запуску

```
cd your_repository
git clone https://github.com/Tvister7/FileHashingAPI
cd FileHashingAPI
```
Убедитесь, что докер активен!

`docker-compose up`

Для запуска дополнительного воркера пропишите команду:

`docker-compose run celery_worker celery --app=celery_worker.celery worker -n workername`

# Порты сервисов и проверки:
Для проверки работоспособности приложение достаточно перейти на страницу документации API и выполнить необходимые запросы.

Заходим на localhost:8000/docs, выполняем POST-запрос, его ответом служит uuid для доступа к хэшу. Далее по GET-запросу вставляем этот uuid и вуа-ля: вы получили хэш!
Также доступны система отслеживания очереди flower по порту 5556 и pgadmin для просмотра результатов в базе по порту 5050.
