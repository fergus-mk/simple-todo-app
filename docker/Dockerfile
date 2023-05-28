# ./docker/Dockerfile
FROM python:3.9.13

# specifying the working directory inside the container
WORKDIR /usr/src/app

# installing the Python dependencies
COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copying the contents of our app' inside the container
COPY ./app .


# defining env vars
ENV FLASK_APP=app.py
# watch app' files
ENV FLASK_DEBUG=true
ENV FLASK_ENV=development

# running Flask as a module, we sleep a little here to make sure that the DB is fully instanciated before running our app'
CMD ["sh", "-c", "sleep 5 \ 
    && python -m flask run --host=0.0.0.0"]