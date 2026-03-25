FROM python:3.11-slim

RUN pip install pandas numpy matplotlib seaborn scikit-learn scipy requests

RUN ls

WORKDIR /app/pipeline/

RUN ls

COPY . /app/pipeline/

RUN ls

CMD [ "bash" ]