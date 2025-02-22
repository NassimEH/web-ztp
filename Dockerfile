FROM python:3.9

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ../ . 
ENV PORT=67
EXPOSE 67

RUN cd dhcp_server/ 

CMD ["python3", "dhcp_server.py"]