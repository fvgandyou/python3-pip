FROM python:3.8

WORKDIR /owner_modules
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r /owner_modules/requirements.txt

COPY . /owner_modules

CMD bash -c "while true; do sleep 1; done"