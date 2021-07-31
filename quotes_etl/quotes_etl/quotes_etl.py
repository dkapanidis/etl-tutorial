import json
import logging
from s3_client import s3_write
from transform_etl import transform_etl
from s3_client import s3_read

from sqs_client import sqs_delete_message, sqs_receive_message

logger = logging.getLogger(__name__)
QUEUE_URL = 'https://sqs.eu-west-1.amazonaws.com/275974460551/etl-example'
DESTINATION_BUCKET = "harbur-etl-example-output"

def run():
    while True:
        parse_message()

def parse_message():
    # get next message from SQS
    logger.info("receiving next message")
    msgs = sqs_receive_message(QUEUE_URL)

    # exit if there are no more messages
    if (len(msgs)==0):
        logger.info("no messages found")
        exit(0)

    for msg in msgs:
        # parse msg body to read filename and bucket
        msg_body = json.loads(msg["Body"])
        for record in msg_body["Records"]:
            bucket = record["s3"]["bucket"]["name"]
            filename = record["s3"]["object"]["key"]

            # read file from origin S3
            logger.info("downloading file s3://%s/%s", bucket, filename)
            file_body = json.loads(s3_read(bucket, filename))

            # do some file transformation using
            transformed_body = transform_etl(file_body)

            # write file to destination S3
            logger.info("uploading file s3://%s/%s", DESTINATION_BUCKET, filename)
            s3_write(DESTINATION_BUCKET, filename, transformed_body)

        # remove message from queue
        sqs_delete_message(QUEUE_URL, msg['ReceiptHandle'])
        logger.info("message deleted")
