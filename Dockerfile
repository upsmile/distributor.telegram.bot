FROM python:latest
COPY . /
WORKDIR /
RUN pip install -r requirements.txt
RUN mkdir /vendors
WORKDIR /vendors
RUN git clone git://github.com/vibora-io/vibora.git
WORKDIR /vendors/vibora
RUN python build.py
WORKDIR /vendors
RUN pip install ./vibora
EXPOSE 8083/tcp
WORKDIR /
ENTRYPOINT ["python", "./app.py"]