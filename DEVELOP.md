# Develop

### Quotes Scrapy

To bootstrap Quotes Scrapy:

```sh
scrapy startproject quotes_scrapy
# create spider `quotes_scrapy/quotes_scrapy/quotes_spider.py`
# add FEED configuration `quotes_scrapy/quotes_scrapy/settings.py`
```

To run crawler:

```sh
scrapy crawl quotes
```

It will crawl the website and upload a JSON file on the S3 bucket.

### SQS

To simulate a file upload on SQS:

```sh
aws sqs send-message --queue-url https://sqs.eu-west-1.amazonaws.com/275974460551/etl-example --message-body '{
"Records": [
  {
    "s3": {
      "bucket": {
        "name": "harbur-etl-example"
      },
      "object": {
        "key":"items-2021-08-01T10-07-29.json"
      }
    }
  }
]}'
```

### Quotes ETL

To run quotes_etl:

```sh
python quotes_etl
```

It will run until all existing messages are consumed by the ETL and then exit.