FROM python:3.13.1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p allure-results

CMD ["pytest", "-v", "--alluredir", "allure-results"]