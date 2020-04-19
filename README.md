## Notes APIRouter

FastAPI example inspired by this [article](https://testdriven.io/blog/fastapi-crud/).

Dependencies:

* FastAPI v0.46.0
* Docker v19.03.5
* Python v3.8.1
* Pytest v5.3.2
* Databases v0.2.6


## Usage

To run the project type on the terminal:

```shell
$ docker-compose up --build -d
```

Ensure the notes table was created:

```shell
$ docker-compose exec db psql --username=hello_fastapi --dbname=hello_fastapi_dev
```

To run the test suite:

```shell
$ docker-compose exec app pytest . -vv
```
