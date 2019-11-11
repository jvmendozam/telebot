
FROM python:3

ADD bot.py /

#RUN apt install python-pip -y
RUN  pip install python-telegram-bot
RUN pip install pystrich

CMD [ "python", "./bot.py" ]


