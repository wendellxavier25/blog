FROM python:3.11.3-alpine3.18
LABEL mantainer="wendell_xw20@hotmail.com"


ENV PYTHONDONTWRITEBYTECODE 1


ENV PYTHONUNBUFFERED 1


COPY djangoapp /djangoapp
COPY scripts /scripts


WORKDIR /djangoapp


EXPOSE 8000


RUN python -m venv /venv && \
  /venv/bin/pip install --upgrade pip && \
  /venv/bin/pip install -r /djangoapp/requirements.txt && \
  adduser --disabled-password --no-create-home duser && \
  mkdir -p /data/web/static && \
  mkdir -p /data/web/media && \
  chown -R duser:duser /venv && \
  chown -R duser:duser /data/web/static && \
  chown -R duser:duser /data/web/media && \
  chmod -R 755 /data/web/static && \
  chmod -R 755 /data/web/media && \
  chmod -R +x /scripts


ENV PATH="/scripts:/venv/bin:$PATH"


USER duser


CMD ["commands.sh"]