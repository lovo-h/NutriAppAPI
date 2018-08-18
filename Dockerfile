FROM python:alpine
LABEL maintainer = "Hector Lovo <lovohh@gmail.com>"

ENV USER nutriappapi
ENV HOME /home/${USER}

WORKDIR ${HOME}/

COPY requirements.txt ${HOME}/

RUN pip install --no-cache-dir -r requirements.txt

COPY . ${HOME}/

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
