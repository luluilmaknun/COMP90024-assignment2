# syntax=docker/dockerfile:1

FROM python:3.9.7

WORKDIR /src

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8081
#CMD ["sleep", "3600"]
CMD ["/bin/bash","-c","python app.py"]


