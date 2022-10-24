FROM python:3.9
 
WORKDIR /fastapi-simple-app
 
COPY ./requirements.txt /fastapi-simple-app/requirements.txt
 
RUN pip install --no-cache-dir --upgrade -r /fastapi-simple-app/requirements.txt
 
COPY ./app /fastapi-simple-app/app
 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]