# Python-CRUD
https://copilot.microsoft.com/chats/K3ibrMsCgrWqh2aEwv7uj

docker run --name mysql \
  -e MYSQL_ROOT_PASSWORD=pass \
  -e MYSQL_DATABASE=testdb \
  -p 3306:3306 \
  -d mysql:8

.. docker rm mysql ...

docker exec -it mysql mysql -u root -ppass

USE testdb;

CREATE TABLE items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT
);


mkdir app
cd app
pip install fastapi uvicorn mysql-connector-python

erstelle main.py

uvicorn main:app --host 0.0.0.0 --port 8000

Die interaktive FastAPI-Dokumentation öffnen:

http://localhost:8000/docs

Dort lassen sich alle implementierten Endpunkte (`GET`, `POST`, `PUT` und
`DELETE`) über **Try it out** ausführen. In GitHub Codespaces kannst du stattdessen
die weitergeleitete URL für Port 8000 mit `/docs` am Ende verwenden.


