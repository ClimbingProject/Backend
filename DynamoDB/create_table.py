import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
table = dynamodb.create_table(
    TableName='Users',
    KeySchema=[
        {
            'AttributeName': 'email',
            'KeyType': 'HASH'  #Partition key
        }#,
        #{
        #    'AttributeName': 'password',
        #    'KeyType': 'RANGE'  #Sort key
        #}
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'email',
            'AttributeType': 'S'
        }#,
        #{
        #    'AttributeName': 'password',
        #    'AttributeType': 'S'
        #},

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
"""

table = dynamodb.create_table(
    TableName='Videos',
    KeySchema=[
        {
            'AttributeName': 'name',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'id',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)
"""
print("Table status:", table.table_status)