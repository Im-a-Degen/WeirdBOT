FROM python:3.9-slim

WORKDIR /var/WeirdBOT
ENV PYTHONIOENCODING="UTF-8" LANG="en_GB.UTF-8"
COPY requirements.txt WeirdBOT.py BOTrequiredDataPublic.py ./

RUN apt-get update && apt-get install -y python3.9-dev
RUN pip install -r requirements.txt

CMD ["python", "WeirdBOT.py"]