import logging
import logging.config
import yaml

def setupLogging():
    with open('logging.yaml', 'rt') as file:
        config = yaml.safe_load(file.read())
        logging.config.dictConfig(config)
