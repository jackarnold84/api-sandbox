import numpy as np
import pandas as pd
import io
from utils import response


def read_dataframe(fileContent):
    # read and check for header
    df_header = pd.read_csv(io.StringIO(fileContent))
    df_no_header = pd.read_csv(io.StringIO(fileContent), header=None)
    if tuple(df_header.dtypes) == tuple(df_no_header.dtypes):
        return df_no_header
    else:
        return df_header


def lambda_handler(event, context):

    # read query
    params = event['queryStringParameters']
    if ('fileContent' not in params):
        return response('Invalid query parameters', status=400)
    fileContent = params['fileContent']
    
    try:
        df = read_dataframe(fileContent)
    except Exception as e:
        print(e)
        return response({'validFile': False}, status=400)
    
    column_summary = []
    cols = df.columns
    dtypes = df.dtypes
    for i in range(len(cols)):
        if dtypes[i] == 'int64' or dtypes[i] == 'float64':
            data = df[cols[i]].dropna()
            column_summary.append({
                'name': str(cols[i]),
                'mean': round(data.mean(), 2),
                'entries': len(data),
                'std': round(data.std(), 2),
            })

    return response(
        {
            'validFile': True,
            'summary': column_summary,
        }
    )
