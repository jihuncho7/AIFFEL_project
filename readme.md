## Test Instruction

- **Admin info**

  **id** : admin 

  **password** : admin

  

  ***db.sqlite included***

  ```
  activate your own venv

  pip install -r requirements.txt 
  python manage.py runserver
  python manage.py test
  ```

  

## Sign Up

- **URL**

  /signup/

- **Method:**

  `POST`

- **Sample Call:**

  ```bash
  curl -X POST "http://127.0.0.1:8000/signup/" -d "username=test2&password=test2"
  
  ```

- **Success Response:**

  - **Code:** 200 **Content:** 

    ```
    {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNjMwMjQwMywianRpIjoiNGE2OTM4YmIyYTllNDA3YWExNjk0NWU3Mjg0ODFmZjciLCJ1c2VyX2lkIjoiTm9uZSJ9.SCtM6oA9BfDw674ATR6YqplIgZPDzFWxThMGe2-KYbc",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2MjE2MzAzLCJqdGkiOiI0YzcwMGE3NjRiYTM0YmViOTJkMzIwY2I5ZmQ2ODliYyIsInVzZXJfaWQiOiJOb25lIn0.oEPL9Zc7ExG3OdikutHyiJKmQcHQLnTZC9VYubffjlM"
    }
    ```

    

- **Error Response:**

  - **Code:** 400 BAD REQUEST **Content:** 

    ```
    {
        "username": [
            "A user with that username already exists."
        ]
    }
    ```

    



## Get Token

- **URL**

  /token/

- **Method:**

  `POST`

- **Sample Call:**

  ```bash
  curl -X POST "http://127.0.0.1:8000/token/" -d "username=test2&password=test2"
  
  ```

- **Success Response:**

  - **Code:** 200 **Content:** `

    ```
    {
        "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNjI5ODAwNCwianRpIjoiMDg0YjY1NGQ1Y2I5NGI1Mjk4NWYzMTY4MTZiZjMzMDgiLCJ1c2VyX2lkIjo0fQ.TyNhi6Gx__St9JsFfsgRvmNjoncBeoEr-MeGdU5GO5Q",
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2MjExOTA0LCJqdGkiOiI2OWUxYWIxNWUwZDc0M2IxYTc5ZWQzOTE5OTk4NTlmNCIsInVzZXJfaWQiOjR9.6kFxZIL0sIDm3XuJJqmScAoNkpUqCvOCgJBxtTUTbT4"
    }
    ```

    

- **Error Response:**

  - **Code:** 401 Unauthorized **Content:** 

    ```
    {
        "detail": "No active account found with the given credentials"
    }
    ```



## Refresh Token

- **URL**

  /token/refresh/

- **Method:**

  `POST`

- **Sample Call:**

  ```bash
  curl -X POST "http://127.0.0.1:8000/token/refresh" -d "refresh=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyNjI5ODAwNCwianRpIjoiMDg0YjY1NGQ1Y2I5NGI1Mjk4NWYzMTY4MTZiZjMzMDgiLCJ1c2VyX2lkIjo0fQ.TyNhi6Gx__St9JsFfsgRvmNjoncBeoEr-MeGdU5GO5Q"
  
  ```

- **Success Response:**

  - **Code:** 200 **Content:** `

    ```
    {
        "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2MjEyMTE0LCJqdGkiOiI3Mzk0NjJhMmRkMWQ0YzZhOWVmMjU0NjJlMDg2ZjAxNSIsInVzZXJfaWQiOjR9.27-6gVyBRNsJmoJJ3kcnqcV7JIp4QSnRoJZFTe_pni4"
    }
    ```

    

- **Error Response:**

  - **Code:** 401 Unauthorized **Content:** 

    ```
    {
        "detail": "Token is invalid or expired",
        "code": "token_not_valid"
    }
    ```



## Show Question

- **URL**

  /question/:id

- **Method:**

  `GET`

- **URL Params**

  **Required:**

  `id=[integer]`

- **Request Header:**

  Authorization: {token type] {access token]

- **Sample Call:**

  ```bash
  curl -XGET "http://127.0.0.1:8000/question/" -H "Authorization: 
  Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2MjEyNjAyLCJqdGkiOiJjNjYyZ
  DRjYzdiMjE0ZTUwOWZiOWJhMGYxZjUzNTQ2NiIsInVzZXJfaWQiOjR9.LUpgOHh-95KiCnun48buvlu67Fyg0VOgPBle3_Ho7JI"
  
  ```

- **Success Response:**

  - **Code:** 200 **Content:** 

    ```
    {"id":1,"author_username":"admin","is_like_user":false,"get_likes":0,"Comment":[{"id":2,"author_username":"admin
    ","created_at":"2021-07-12T17:19:46.465264Z","context":"2nd","author":1,"post":1},{"id":1,"author_username":"adm
    in","created_at":"2021-07-12T17:12:55.635166Z","context":"댓글...
    ```

    

- **Error Response:**

  - **Code:** 404 NOT FOUND **Content:** `{"detail":"Not found."}`

  OR

  - **Code:** 401 UNAUTHORIZED **Content:** 

    ```
    {"detail":"Given token not valid for any token type","code":"token_not_valid","messages":[{"token_class":"Access
    Token","token_type":"access","message":"Token is invalid or expired"}]}
    ```



## Create Question

- **URL**

  /question/

- **Method:**

  `POST`

- **Request Header:**

  Authorization: {token type] {access token]

- **Sample Call:**

  ```bash
  curl -XPOST "http://127.0.0.1:8000/question/" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2MjEzMDQ2LCJqdGkiOiIwNDA3YzQyNTg0ZmU0ZWQ3OGM4YWNjNTAzNzMzMjY1MyIsInVzZXJfaWQiOjR9.qrpFF6Tb3ZJxxZkiOkyyoWiB7WNr4Q4ClJ5QX-mczSA" -d "title=yes, title &context=yes, context."
  
  ```

- **Success Response:**

  - **Code:** 200 **Content:** 

    ```
    {"id":4,"author_username":"test1","is_like_user":false,"get_likes":0,"Comment":[],"created_at":"2021-07-13T21:48
    :40.841021Z","title":"yes, title","context":"yes, context.","author":4,"like_user_set":[]}
    
    ```

    

- **Error Response:**

  - **Code:** 401 UNAUTHORIZED **Content:** 

    ```
    {"detail":"Given token not valid for any token type","code":"token_not_valid","messages":[{"token_class":"Access
    Token","token_type":"access","message":"Token is invalid or expired"}]}
    ```

    

## Update Question

- **URL**

  /question/:id

- **Method:**

  `PUT`

- **Request Header:**

  Authorization: {token type] {access token]

- **Sample Call:**

  ```bash
  curl -XPUT "http://127.0.0.1:8000/question/1/" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2MjEzMDQ2LCJqdGkiOiIwNDA3YzQyNTg0ZmU0ZWQ3OGM4YWNjNTAzNzMzMjY1MyIsInVzZXJfaWQiOjR9.qrpFF6Tb3ZJxxZkiOkyyoWiB7WNr4Q4ClJ5QX-mczSA" -d "title=fix, title.&context=fix, context."
  
  ```

- **Success Response:**

  - **Code:** 200 **Content:** 

    ```
    {"id":4,"author_username":"test1","is_like_user":false,"get_likes":0,"Comment":[],"created_at":"2021-07-13T21:48
    :40.841021Z","title":"yes, title","context":"yes, context.","author":4,"like_user_set":[]}
    
    ```

    

- **Error Response:**

  - **Code:** 401 UNAUTHORIZED **Content:** 

    ```
    {"detail":"Given token not valid for any token type","code":"token_not_valid","messages":[{"token_class":"Access
    Token","token_type":"access","message":"Token is invalid or expired"}]}
    ```

    

## Delete Question

- **URL**

  /question/:id

- **Method:**

  `DELETE`

- **Request Header:**

  Authorization: {token type] {access token]

- **Sample Call:**

  ```bash
  curl -XDELETE "http://127.0.0.1:8000/question/1/" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2MjEzMDQ2LCJqdGkiOiIwNDA3YzQyNTg0ZmU0ZWQ3OGM4YWNjNTAzNzMzMjY1MyIsInVzZXJfaWQiOjR9.qrpFF6Tb3ZJxxZkiOkyyoWiB7WNr4Q4ClJ5QX-mczSA"
  
  ```

- **Success Response:**

  - **Code:** 204 NO_CONTENT

    

- **Error Response:**

  - **Code:** 401 UNAUTHORIZED **Content:** 

    ```
    {"detail":"Given token not valid for any token type","code":"token_not_valid","messages":[{"token_class":"Access
    Token","token_type":"access","message":"Token is invalid or expired"}]}
    ```

    or

    **Code:** 404 Not Found **Content:** 

    ```
    {
        "detail": "Not found."
    }
    ```

    

## Update Question Like

- **URL**

  /question/:id/like/

- **Method:**

  `POST`

- **Request Header:**

  Authorization: {token type] {access token]

- **Sample Call:**

  ```bash
  curl -XPOST "http://127.0.0.1:8000/question/2/like/" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2MjE0OTYxLCJqdGkiOiIyOTNlYzIyNTc2ODU0YTg1YmQxY2JlODE5ODJiMTZhYyIsInVzZXJfaWQiOjR9.qilzMSvjQS42Xxz5EzBcwEOkvoE25BEo2hINlgl4bk4"
  
  ```

- **Success Response:**

  - **Code:** 201 CREATED

    

- **Error Response:**

  - **Code:** 401 UNAUTHORIZED **Content:** 

    ```
    {"detail":"Given token not valid for any token type","code":"token_not_valid","messages":[{"token_class":"Access
    Token","token_type":"access","message":"Token is invalid or expired"}]}
    ```

    

## Update Question UnLike

- **URL**

  /question/:id/like/

- **Method:**

  `DELETE`

- **Request Header:**

  Authorization: {token type] {access token]

- **Sample Call:**

  ```bash
  curl -XDELETE "http://127.0.0.1:8000/question/2/like/" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2MjE0OTYxLCJqdGkiOiIyOTNlYzIyNTc2ODU0YTg1YmQxY2JlODE5ODJiMTZhYyIsInVzZXJfaWQiOjR9.qilzMSvjQS42Xxz5EzBcwEOkvoE25BEo2hINlgl4bk4"
  
  ```

- **Success Response:**

  - **Code:** 204 NO_CONTENT

    

- **Error Response:**

  - **Code:** 401 UNAUTHORIZED **Content:** 

    ```
    {"detail":"Given token not valid for any token type","code":"token_not_valid","messages":[{"token_class":"Access
    Token","token_type":"access","message":"Token is invalid or expired"}]}
    ```

    

## Search Question

- **URL**

  /question/?search=

- **Method:**

  `GET`

- **URL Params**

  **Required:**

  `search=[str]`

- **Request Header:**

  Authorization: {token type] {access token]

- **Sample Call:**

  ```bash
  curl -XGET "http://127.0.0.1:8000/question/?search=2번" -H "Authorization: 
  Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2MjEyNjAyLCJqdGkiOiJjNjYyZ
  DRjYzdiMjE0ZTUwOWZiOWJhMGYxZjUzNTQ2NiIsInVzZXJfaWQiOjR9.LUpgOHh-95KiCnun48buvlu67Fyg0VOgPBle3_Ho7JI"
  
  ```

- **Success Response:**

  - **Code:** 200 **Content:** 

    ```
    [
        {
            "id": 2,
            "author_username": "admin",
            "is_like_user": false,
            "get_likes": 2,
            "Comment": [],
            "created_at": "2021-07-13T20:35:00.221560Z",
            "title": "2번째 글",
            "context": "2번째 컨텍스트",
            "author": 1,
            "like_user_set": [
                1,
                3
            ]
        }
    ]
    ```

    

- **Error Response:**

  

  - **Code:** 401 UNAUTHORIZED **Content:** 

    ```
    {"detail":"Given token not valid for any token type","code":"token_not_valid","messages":[{"token_class":"Access
    Token","token_type":"access","message":"Token is invalid or expired"}]}
    ```



## Show Comment

- **URL**

  /question/:id/comment/

- **Method:**

  `GET`

- **URL Params**

  **Required:**

  `id=[int]`

- **Request Header:**

  Authorization: {token type] {access token]

- **Sample Call:**

  ```bash
  curl -XGET "http://127.0.0.1:8000/question/2/comment/" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2MjE3NzgzLCJqdGkiOiIyODE2NWIwYTliZDY0ODkzOGYzYzJkOGVjYjk5ZWYxYyIsInVzZXJfaWQiOjR9.JPJoLKC5SU2xMS8EVKm3YNtKa_iBlw3wg3Ge-C58LQY"
  
  ```

- **Success Response:**

  - **Code:** 200 **Content:** 

    ```
    {"id":3,"author_username":"test1","created_at":"2021-07-13T23:04:56.717859Z","context":"yes, context.","author":
    4,"post":2}
    
    ```

    

- **Error Response:**

  - **Code:** 401 UNAUTHORIZED **Content:** 

    ```
    {"detail":"Given token not valid for any token type","code":"token_not_valid","messages":[{"token_class":"Access
    Token","token_type":"access","message":"Token is invalid or expired"}]}
    ```



## Create Comment

- **URL**

  /question/:id/comment

- **Method:**

  `POST`

- **URL Params**

  **Required:**

  `id=[int]`

- **Request Header:**

  Authorization: {token type] {access token]

- **Sample Call:**

  ```bash
  curl -XPOST "http://127.0.0.1:8000/question/2/comment/" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2MjE3NzgzLCJqdGkiOiIyODE2NWIwYTliZDY0ODkzOGYzYzJkOGVjYjk5ZWYxYyIsInVzZXJfaWQiOjR9.JPJoLKC5SU2xMS8EVKm3YNtKa_iBlw3wg3Ge-C58LQY" -d "context=yes, context."
  
  ```

- **Success Response:**

  - **Code:** 200 **Content:** 

    ```
    {"id":3,"author_username":"test1","created_at":"2021-07-13T23:04:56.717859Z","context":"yes, context.","author":
    4,"post":2}
    
    ```

    

- **Error Response:**

  - **Code:** 401 UNAUTHORIZED **Content:** 

    ```
    {"detail":"Given token not valid for any token type","code":"token_not_valid","messages":[{"token_class":"Access
    Token","token_type":"access","message":"Token is invalid or expired"}]}
    ```



## Update Comment

- **URL**

  /question/:id/comment/:id/

- **Method:**

  `PUT`

- **URL Params**

  **Required:**

  `id=[int]`

- **Request Header:**

  Authorization: {token type] {access token]

- **Sample Call:**

  ```bash
  curl -XPUT "http://127.0.0.1:8000/question/2/comment/3/" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2MjE3NzgzLCJqdGkiOiIyODE2NWIwYTliZDY0ODkzOGYzYzJkOGVjYjk5ZWYxYyIsInVzZXJfaWQiOjR9.JPJoLKC5SU2xMS8EVKm3YNtKa_iBlw3wg3Ge-C58LQY" -d "context=yes, context."
  
  ```

- **Success Response:**

  - **Code:** 200 **Content:** 

    ```
    {"id":3,"author_username":"test1","created_at":"2021-07-13T23:04:56.717859Z","context":"yes, context.","author":
    4,"post":2}
    
    ```

    

- **Error Response:**

  - **Code:** 401 UNAUTHORIZED **Content:** 

    ```
    {"detail":"Given token not valid for any token type","code":"token_not_valid","messages":[{"token_class":"Access
    Token","token_type":"access","message":"Token is invalid or expired"}]}
    ```

    

## Delete Comment

- **URL**

  /question/:id/comment/:id/

- **Method:**

  `DELETE`

- **URL Params**

  **Required:**

  `id=[int]`

- **Request Header:**

  Authorization: {token type] {access token]

- **Sample Call:**

  ```bash
  curl -XDELETE "http://127.0.0.1:8000/question/2/comment/3/" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2MjE3NzgzLCJqdGkiOiIyODE2NWIwYTliZDY0ODkzOGYzYzJkOGVjYjk5ZWYxYyIsInVzZXJfaWQiOjR9.JPJoLKC5SU2xMS8EVKm3YNtKa_iBlw3wg3Ge-C58LQY"
  
  ```

- **Success Response:**

  - **Code:** 204 NO_CONTENT

    

- **Error Response:**

  - **Code:** 401 UNAUTHORIZED **Content:** 

    ```
    {"detail":"Given token not valid for any token type","code":"token_not_valid","messages":[{"token_class":"Access
    Token","token_type":"access","message":"Token is invalid or expired"}]}
    ```

    

## Show Question got most likes of the Months

- **URL**

  /qofmonth/

- **Method:**

  `GET`

- **Request Header:**

  Authorization: {token type] {access token]

- **Sample Call:**

  ```bash
  curl -XGET "http://127.0.0.1:8000/qofmonth/" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjI2MjE4NDk5LCJqdGkiOiI2NGRiNGEzYzUwMWQ0ZDViOWU4OWJkZWFjNTc5OWU4NSIsInVzZXJfaWQiOjR9.J27yQfDrHGG4uob0HDwSYZhi5BYZLUlUS3Z4tMDl40Y"
  
  ```

- **Success Response:**

  - **Code:** 200 **Content:** 

    ```
    [
        {
            "id": 2,
            "author_username": "admin",
            "is_like_user": false,
            "get_likes": 2,
            "Comment": [
                {
                    "id": 3,
                    "author_username": "test1",
                    "created_at": "2021-07-13T23:04:56.717859Z",
                    "context": "yes, context.",
                    "author": 4,
                    "post": 2
                }
            ],
            "created_at": "2021-07-13T20:35:00.221560Z",
            "title": "2번째 글",
            "context": "2번째 컨텍스트",
            "author": 1,
            "like_user_set": [
                1,
                3
            ]
        }
    ]
    ```

    

- **Error Response:**

  - **Code:** 401 UNAUTHORIZED **Content:** 

    ```
    {"detail":"Given token not valid for any token type","code":"token_not_valid","messages":[{"token_class":"Access
    Token","token_type":"access","message":"Token is invalid or expired"}]}
    ```

