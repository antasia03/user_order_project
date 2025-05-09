Django Orders API
### О проекте
Это простое серверное приложение на Django для управления пользователями и заказами.
Позволяет создавать, получать и обновлять пользователей и их заказы через REST API.

### Технологии
Python 3.10+
Django 4.x
Django REST Framework
PostgreSQL
Docker

### Установка и запуск
1. Клонируйте репозиторий
git clone <your-repo-url>
cd <project-folder>

2. Запустите PostgreSQL
Можно через Docker:
docker run --name postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres
Или используйте свою базу, указав параметры подключения в settings.py.

3. Установите зависимости и примените миграции
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python manage.py migrate

4. Запустите сервер
python manage.py runserver
Или через Docker Compose (если есть):
docker-compose up --build

### API
Пользователи
1. Создать пользователя
POST http://localhost:8000/api/users/
Тело запроса:
{
  "username": "nastya",
  "password": "your_password",
  "email": "nastya@example.com",
  "age": 25
}

2. Получить список пользователей
GET http://localhost:8000/api/users/

3. Обновить пользователя
PATCH http://localhost:8000/api/users/{id}/

Заказы
1. Создать заказ
POST http://localhost:8000/api/orders/
Тело запроса:
{
  "title": "Заказ на доставку",
  "description": "Доставить букет по адресу ул. Ленина, 5",
  "user": 2
}
При создании заказа проверяется, что пользователь с указанным ID существует.

2. Получить список заказов
GET http://localhost:8000/api/orders/

3. Обновить заказ
PATCH http://localhost:8000/api/orders/{id}/

### Доступ к API
Эндпоинты для работы с пользователями (например, просмотр списка пользователей) доступны без аутентификации.
Для создания, изменения и просмотра заказов требуется JWT-аутентификация.

### JWT-аутентификация
Для доступа к защищённым эндпоинтам API используется JWT-токен.

1. Получение токена
Отправьте POST-запрос на:
POST http://localhost:8000/api/token/
Content-Type: application/json
Тело запроса:
{
  "username": "your_username",
  "password": "your_password"
}
В ответе вы получите:
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}

2. Использование токена
Для доступа к защищённым ресурсам добавляйте в заголовок запроса:
Authorization: Bearer <your_access_token>

3. Обновление токена
Отправьте POST-запрос на:
POST http://localhost:8000/api/token/refresh/
Content-Type: application/json
Тело запроса:
json
{
  "refresh": "your_refresh_token"
}

### Особенности
Пароли пользователей хранятся в зашифрованном виде.
При создании заказа проверяется существование пользователя.
Корректная обработка ошибок с понятными сообщениями.