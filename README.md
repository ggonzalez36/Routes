# Prueba tecnica AITurning backend

Se crearon 4 metodos que definen

para ejecuitar el projecto

* python manage.py makemigrations
* python manage.py migrations
* python manage.py runserver


el aplicativo es backend y se divide en 4 webservices
Recomiendo probar con Postman

* http://127.0.0.1:8000/clients/bookDriver/

json body 

{
"idRequest":"1",
"driver":{"id":"1","lat":"10","lng":"15"},
"lat": "1",
"lng": "5"
}

* http://127.0.0.1:8000/clients/getAllRequests/



* http://127.0.0.1:8000/clients/getDriverRequests?id=1


* http://127.0.0.1:8000/clients/findNearDriver?lat=1&long=2

