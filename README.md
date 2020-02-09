# Статистика зарплат по популярным языкам

Приложение получает статистику зарплат по популярным языкам программирования с **HeadHunter** и **SuperJob**.

[![asciicast](https://asciinema.org/a/kjc4bD8FiL6UYOni7ZhTzMSaP.svg)](https://asciinema.org/a/kjc4bD8FiL6UYOni7ZhTzMSaP)

### Установка

Для работы приложения требуется **Docker** и **Docker Compose**.

### Настройка

Подготовить файл для хранения API-токена сервиса:
```
cp .env.example .env
```

Зарегистрироваться в [API SuperJob](https://api.superjob.ru), получить **secret key** и указать его в `.env`:
```
SUPERJOB_SECRET_KEY=<secret_key>
```

Далее, там же добавить номер версии используемого **API SuperJob**:
```
SUPERJOB_API_VERSION=2.27
```

### Запуск

```
make run
```

Удаление всех временных файлов приложения:
```
make flush
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).