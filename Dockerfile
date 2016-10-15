FROM python:2.7
ENV PYTHONUNBUFFERED 1
ADD requirements.txt /
RUN pip install -r requirements.txt
RUN rm requirements.txt
