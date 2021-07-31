import logging

import pandas as pd

logger = logging.getLogger(__name__)

def transform_etl(data: any) -> any:
    df = pd.DataFrame(data)
   
    # rename "text" column to "message"
    df.rename(columns = {"text": "message"}, inplace = True)
    # drop "author" column
    df.drop(columns =["author"], inplace = True)

    return df.to_json(orient='records')

