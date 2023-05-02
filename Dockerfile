FROM python:3.11-alpine

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python -m venv $VIRTUAL_ENV && pip install --upgrade pip

COPY requirements/* ./
RUN pip install -r prod.txt

WORKDIR /opt/app

COPY blog/ ./

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0", "app:app"]
