# Build
### docker-compose up --build
- If unhealthy - repeat docker-compose up

# Dump
### $ docker exec -i welcome-to-docker-db-1 mysql -u root -proot < docker-entrypoint-initdb.d/init_db.sql
