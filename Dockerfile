FROM python:3.9

WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN mkdir /usr/src/app/photos

RUN pip install --user -r requirements.txt
RUN pip install --user torch==1.13.0+cpu -f https://download.pytorch.org/whl/torch_stable.html

CMD ["python", "main.py"]