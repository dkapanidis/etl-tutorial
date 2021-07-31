# ETL Tutorial

Simple ETL workflow using [Scrapy], [S3], [SQS], [Python] & [Pandas].

[Scrapy]: https://scrapy.org/
[S3]: https://aws.amazon.com/s3/
[SQS]: https://aws.amazon.com/sqs/
[Python]: https://www.python.org/
[Pandas]: https://pandas.pydata.org/

The objective is to scrap periodically a website, store the data in a JSON format in an AWS S3 bucket. For each file upload a message is generated in AWS SQS and an ETL process reads the message, opens the new file, transforms it to a different JSON format and stores it in a separate AWS S3 bucket.

> The tutorial is explained in detail on the [blog](https://codingholygrail.com)

