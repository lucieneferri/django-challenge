# Django Challenge

## How to start the project 

The main docker-compose file has all the services and the requirement file has all the dependencies to run the application, so:

To initialize the docker container run on the bash terminal:

```
docker-compose up
```
To stop the container run:
```
docker-compose down
```


#
## ENDPOINTS

## Sign-up

**Path:** `api/sign-up`

**Method:** `POST`

**Json Body:**
```json
{
	"username":"User1",
	"password":"123",
	"password_confirm":"123",
	"email":"user@gmail.com",
	"is_staff": "True"
}
```

**Response:**
```json
{
	"username": "User1",
	"email": "user@gmail.com",
	"is_staff": true
}
```
#
## Login

**Path:** `api/login`

**Method:** `POST`

**Json Body:**
```json
{
	"username":"User1",
	"password":"123"
}
```

**Response:**
```json
{
	"token": "c1e8676edd93404ba3ddf12ebf55657c34ccc8ac"
}
```
#

## Author

**Path:** `api/author`

**Method:** `POST`

**Content-Type** `multipart/form-data`

`name`: `Author1`

`picture`: `<file.>`

**Response:**
```json
{
	"id_author": "43c0f183-6306-4aee-a615-20ae6c0decbd",
	"name": "Author1",
	"picture": "http://127.0.0.1:8000/media/5-pontos-saude-do-homem.jpg"
}

```
**Path:** `api/author`

**Method:** `GET`


**Response:**
```json
{
    "id_author": "43c0f183-6306-4aee-a615-20ae6c0decbd",
    "name": "Author1",
    "picture": "http://127.0.0.1:8000/media/5-pontos-saude-do-homem.jpg"
}
```

**Path:** `api/author/43c0f183-6306-4aee-a615-20ae6c0decbd`

**Method:** `PUT`

**Content-Type** `multipart/form-data`

`name`: `Author2`

`picture`: `<file.>`

**Response:**
```json
{
	"id_author": "43c0f183-6306-4aee-a615-20ae6c0decbd",
	"name": "Author2",
	"picture": "http://127.0.0.1:8000/media/5-pontos-saude-do-homem.jpg"
}

```


**Path:** `api/author/43c0f183-6306-4aee-a615-20ae6c0decbd`

**Method:** `DELETE`

**Response:**

204 No Content
#

## Article

**Authorized and Admin Users**

**Path:** `api/article`

**Method:** `POST`

**Json Body:**
```json
{
	"author": "43c0f183-6306-4aee-a615-20ae6c0decbd",
	"category":"Category",
	"title":"Article title",
	"summary":"This is a summary of the article",
	"firstParagraph":"<p>This is the first paragraph of this article</p>",
	"body":"<div><p>Second paragraph</p><p>Third paragraph</p></div>"
}

```

**Response:**
```json
{
	"id_article": "465e88cd-92cc-4b46-8935-a66cbc60857e",
	"author": "43c0f183-6306-4aee-a615-20ae6c0decbd",
	"category": "Category",
	"title": "Article title",
	"summary": "This is a summary of the article",
	"firstParagraph": "<p>This is the first paragraph of this article</p>"
}

```
**Authorized and Admin Users**

**Path:** `api/article`

**Method:** `GET`


**Response:**
```json
{
    "id_article": "465e88cd-92cc-4b46-8935-a66cbc60857e",
		"author": {
			"id_author": "43c0f183-6306-4aee-a615-20ae6c0decbd",
			"name": "candy",
			"picture": "http://127.0.0.1:8000/media/5-pontos-saude-do-homem.jpg"
		},
		"category": "Category",
		"title": "Article title",
		"summary": "This is a summary of the article",
		"firstParagraph": "<p>This is the first paragraph of this article</p>",
		"body": ""
}
```
**Anonymous User**

**Path:** `api/article`

**Method:** `GET`


**Response:**
```json
{
    "id_article": "d88b0c1d-761e-429d-adbd-fdf3c7fc77fd",
		"author": {
			"id_author": "43c0f183-6306-4aee-a615-20ae6c0decbd",
			"name": "candy",
			"picture": "http://127.0.0.1:8000/media/5-pontos-saude-do-homem.jpg"
		},
		"category": "Category2",
		"title": "Article title 2",
		"summary": "This is a summary of the article",
		"firstParagraph": "<p>This is the first paragraph of this article</p>"
}
```

**Authorized and Admin Users**

**Path:** `api/article/d88b0c1d-761e-429d-adbd-fdf3c7fc77fd`

**Method:** `PUT`

**Json Body:**
```json
{
	"author": "43c0f183-6306-4aee-a615-20ae6c0decbd",
	"category":"Category2",
	"title":"Article title 2",
	"summary":"This is a summary of the article",
	"firstParagraph":"<p>This is the first paragraph of this article</p>",
	"body":"<div><p>Second paragraph</p><p>Third paragraph</p></div>"
}

```

**Response:**
```json
{
	"id_article": "d88b0c1d-761e-429d-adbd-fdf3c7fc77fd",
	"author": "43c0f183-6306-4aee-a615-20ae6c0decbd",
	"category": "Category2",
	"title": "Article title 2",
	"summary": "This is a summary of the article",
	"firstParagraph": "<p>This is the first paragraph of this article</p>"
}

```
**Authorized and Admin Users**

**Path:** `api/article/d88b0c1d-761e-429d-adbd-fdf3c7fc77fd`

**Method:** `DELETE`

**Response:**

204 No Content
#














