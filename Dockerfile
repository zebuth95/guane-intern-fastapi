FROM python:3.9

WORKDIR /app

COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
COPY . /app

RUN useradd appuser && chown -R appuser /app
USER appuser
RUN chmod a+w ./ -R

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]