# autoseller
 Сайт по продажам авто. Агрегаттор 

## Установка
Требования:
- Python 3.6+
- PostgreSQL 9.6 / MySQL 5.7 / SQLite 3.7.11+
- Django 4.0+

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Настройка базы данных
В файле `autoseller/settings.py` в переменной `DATABASES` указать настройки подключения к базе данных.

### Создание таблиц в базе данных
```bash
python manage.py migrate
```

### Создание суперпользователя
```bash
python manage.py createsuperuser
```

### Запуск сервера
```bash
python manage.py runserver
```

## Разработка
### Создание миграций
```bash
python manage.py makemigrations
```

### Применение миграций
```bash
python manage.py migrate
```

### Создание Марок авто
```bash
python manage.py brands
```

### Создание трансмиссий
```bash
python manage.py transmissions
```

### Создание типов кузова
```bash
python manage.py body_type
```

### Создание базового суперпользователя
```bash
python manage.py user

Login: admin
Password: admin

```

### Создание загрузка статических данных
```bash
python manage.py collectstatic
```

### Старт проекта
```bash
python manage.py runserver
```