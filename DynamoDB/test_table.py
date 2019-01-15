import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
table = dynamodb.create_table(
    TableName='test',
    KeySchema=[
        {
            'AttributeName': 'email',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'user_id',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    LocalSecondaryIndexes=[
        {
            'IndexName': 'typeLSIndex',
            'KeySchema': [
                {
                    'AttributeName': 'email',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'full_name',
                    'KeyType': 'RANGE'  #Sort key
                }
                ],
            'Projection': {
                'ProjectionType': 'INCLUDE',
                'NonKeyAttributes': ['user_id']
            }
        }
    ],
    GlobalSecondaryIndexes=[
            {
                'IndexName': 'GSI',
                'KeySchema': [
                    {
                        'AttributeName': 'password',
                        'KeyType': 'HASH'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'KEYS_ONLY',
                    },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                }
            }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'email',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'user_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'full_name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'password',
            'AttributeType': 'S'
        }
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