# Book reservations application

## Схема базы данных
![](./readme_images/db.png)

## Установка и запуск

Скопируйте репозиторий используя следующую команду:

```bash
git clone https://github.com/YuryRass/book_reservations.git
```

Затем перейдите в каталог с проектом:

```bash
cd book_reservations
```

Также в корне проекта переименуйте конфигурационный файл `.env-example` на `.env`:

```bash
mv .env-example .env
```

Для запуска проекта введите команду:


```bash
docker compose up -d --build
```

После запуска можно переходить по адресу: http://127.0.0.1:8000/docs и проверять все endpoint-ы приложения
