# Fastapi_Trading
### Conducting various operations, transactions, notifying the user by mail if there have been changes in his transactions
&nbsp;  

---
### *Don't forget to change the data in the file .env*      
---
&nbsp; 
### You can run it as it is usually done:
```
python3 -m venv venv

source venv/bin/activate
```
### After activating the environment, install the dependencies:
```
pip install -r requirements.txt
```

### And then going to the SRC folder we write in the terminal:
```
uvicorn main:app --reload
```
---
### You can also run the project through docker:
```
docker compose build
```
### Then:
```
docker compose up
```
