FROM mohammadahadi/ffmpy
WORKDIR /bot
COPY requirements.txt /bot/
RUN pip install --upgrade pip
RUN apt-get -y install libopus0
RUN pip install -r requirements.txt
COPY . /bot
CMD python bot.py