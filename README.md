
# Market - Backend Project

Backend project based on python 3.11 with fastapi to publish web microservices with CRUD for supermarkets and products.


## Installating

Clone the repo

```bash
  git clone https://github.com/AndresOrozcoDev/market_backend_python.git
```

Install virtual environment

```bash
  pip install virtualenv
```

Create virtual environment

```bash
  python -m venv env
```

Activate virtual environment

```bash
  env\Scripts\activate
```

Install requirements.txt file

```bash
  pip install -r requirements.txt
```

Create requirements.txt file

```bash
  pip freeze > requirements.txt
```

Run the project

```bash
  py main.py
```

Run project as server

```bash
  uvicorn main:app --reload
```


## API Reference

#### Get supermarkets

```bash
  GET /api/supermarkets
```

#### Get supermarket

```bash
  GET /api/supermarket/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of item to fetch |

#### Post supermarket

```bash
  POST /api/supermarket
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | **Required**. Name of new supermarket |

#### Put supermarket

```bash
  PUT /api/supermarket/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of item to fetch |

#### Delete supermarket

```bash
  DELETE /api/supermarket/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `int` | **Required**. Id of item to fetch |


## Author

- [@AndresOrozcoDev](https://github.com/AndresOrozcoDev)
