# TodoList---Python - fastapi

Branch:
  - Main: Local api - CRUD
  - MongoDB: 
      - Connection with a Mongo DB, CRUD with tasks and items 
      - CRUD by users
      - TODO: Auth
  - Mysql: 
      - TODO: Auth, Connection with a Mongo DB, CRUD with tasks and items, users

To run:
  python -m uvicorn main:app --reload
 
Tests:
  python -m pytest routers/test_items.py -vv
  python -m pytest test_main.py -vv
