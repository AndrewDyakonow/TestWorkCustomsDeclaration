Задание:
1) Написать end point и сервис, который на вход получает данные для авторизации в Озон, 
2) далее получив данные собирает данные по методу -https://docs.ozon.ru/api/seller/#operation/PostingAPI_GetEtgb
за период today() -4 
3) и записывает в базу ClickHouse.

Дополнительно:
1) Должно быть учтено удаление дублей.
2) Мультипотоковость будет плюсом.
3) Использование celery или другого варианта распределенного выполнения заданий, также будет плюсом.




91735e17-24f7-41a8-b992-38ca79375c94
1574361