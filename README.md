
<h1 align="center">Test Work Customs Declaration</h1>

<h2 align="center"> Тестовое задание </h2>

<div align="center">
    
<div>
    <a href="https://pypi.org/project/gunicorn/"><img alt="Static Badge" src="https://img.shields.io/badge/gunicorn-21.2.0-darkgreen?labelColor=gray"></a>
    <a href="https://pypi.org/project/pydantic/"><img alt="Static Badge" src="https://img.shields.io/badge/pydantic-2.4.2-darkred?labelColor=gray"></a>
    <a href="https://pypi.org/project/uvicorn/"><img alt="Static Badge" src="https://img.shields.io/badge/uvicorn-0.23.2-darkgreen?labelColor=purple"></a>
</div>
<div>
    <a href="https://www.python.org/"><img width="48" height="48" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python"/></a>
    <a href="https://www.docker.com/"><img width="48" height="48" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg" alt="docker"/></a>
    <a href="https://fastapi.tiangolo.com/"><img width="48" height="48" src="https://cdn.worldvectorlogo.com/logos/fastapi-1.svg" alt=""/></a>
    <a href="https://www.sqlalchemy.org/"><img width="48" height="48" src="https://upload.wikimedia.org/wikipedia/commons/d/d7/SQLAlchemy.svg" alt=""/></a>
    <a href="https://clickhouse.com/"><img width="48" height="48" src="https://avatars.githubusercontent.com/u/54801242?s=200&v=4" alt=""/></a>
</div>

</div>

___

<h2>1. Установка</h2>

1.1 Клонируйте проект:
    
```bash
    git clone git@github.com:AndrewDyakonow/TestWorkCustomsDeclaration.git
```

1.2 Выполните команду построения докер образа и запуска контейнеров

```bash
    docker-compose up --build
```

___

<h2>2. Работа</h2>

2.1 После запуска контейнеров, по адресу http://127.0.0.1:8000/ будет доступно приложение.

Дальнейшие действия необходимо выполнять либо в API-платформе для разработчиков ``Postman``,
либо с помощью веб-интерфейса Swagger, доступного по адресу http://127.0.0.1:8000/docs/


***

<h2>3. Пример </h2>

 <h3>3.1 POSTMAN </h3>

3.1.1 Вставить ссылку на эндпоинт(http://127.0.0.1:8000/) в поле ввода запроса

3.1.2 В теле запроса указать параметры ``api_key``, ``client_id``
```html
{
    "api_key": str,
    "client_id": str
}
```

3.1.3 Нажать кнопку 'SEND'

В случае удачного создания таблицы в БД и записи в нее данных будет получен ответ:
    
    ``Декларации сохранены``

___


<h3>3.2 Swagger </h3>

3.2.1 Вставить ссылку на эндпоинт(http://127.0.0.1:8000/) в cтроку поиска, раскрыть выпадающее меню POST запроса

3.2.2 Нажать кнопку "Try it out"

3.2.3 В поле 'Request body' ввести атрибуты ``api_key``, ``client_id``, и нажать кнопку ``Execute``

```html
{
    "api_key": str,
    "client_id": str
}
```

3.2.4 В случае удачного создания таблицы в БД и записи в нее данных, в поле ``Server response`` будет отображён статус запроса:

    ``Декларации сохранены``