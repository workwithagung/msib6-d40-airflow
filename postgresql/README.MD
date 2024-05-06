1. Create folder postgresql
2. Create docker-compose.yml
3. Copy paste isian docker-compose.yml berikut
```
version: '2'
services:
  postgres-msib:
    image: postgres:15
    container_name: postgres-msib
    env_file:
      - .env
    volumes:
      - /var/lib/postgresql/data
    ports:
      - 5436:5432/tcp
```
4. Buat file .env dengan isian berikut
```
POSTGRES_PASSWORD = postgres
POSTGRES_USER = postgres
POSTGRES_DB = postgres
POSTGRES_HOST_AUTH_METHOD=trust
```
5. Masuk ke directory folder postgresql 
6. jalankan docker dengan command `docker compose up`
7. Buat koneksi dengan postgresql bisa pake extension mysql di vs code