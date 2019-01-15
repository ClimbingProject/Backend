import boto3
from boto3.dynamodb.conditions import Key, Attr


# Get the service resource.
dynamodb = boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('test')

# {} : String Set
# [] : List

def write_data():
    table.put_item(
                Item={
                    'email': 'test@gmail.com',
                    'user_id': 'test.jon',
                    'full_name': 'Jon',
                    'password': 'test',
                    'follower': {'a', 'b', 'c'}
                }
            )
    table.put_item(
        Item={
            'email': 'a@gmail.com',
            'user_id': 'a.jon',
            'full_name': 'Jon A',
            'password': 'a',
            'follower': {'l', 'm', 'n'}
        }
    )

    table.put_item(
        Item={
            'email': 'test@gmail.com',
            'user_id': 'test2.jon',
            'full_name': 'Jon 2',
            'password': 'test2',
            'follower': {'x', 'y', 'z'}
        }
    )


def check_data():
    response = table.query(KeyConditionExpression=Key("email").eq('test@gmail.com'))
    print(response['Items'])

    print(table.scan(TableName='test', IndexName='typeLSIndex')['Items'])

    print(table.query(
    IndexName='typeLSIndex',
    KeyConditionExpression=Key('email').eq('test@gmail.com') & Key('full_name').eq('Jon') #& Key('user_id').eq('tset.jon')
)['Items'])

    # Valid expression. orの中の最初に見つけた物を返す。この場合'a@gmail.com'
    print(table.query(
        KeyConditionExpression=Key('email').eq(('a@gmail.com') or ('test@gmail.com'))
    )['Items'])


    print(table.get_item(Key={'email': 'test@gmail.com', 'user_id': 'test.jon'}
    )['Item'])

    # hash keyのemailがtest@gmail.comのを全て返すかGSIのhash keyのpasswordがtest２を返す。前者がtrueならそこで終わる
    # もし接続詞が 'or' じゃなくて ',' だと両方帰ってくる
    # 接続詞が 'and'　の場合は両方の条件を満たす物が帰ってくる
    resp = (table.query(KeyConditionExpression=Key("email").eq('test@gmail.com'))['Items']),  (table.query(IndexName='GSI', KeyConditionExpression=Key("password").eq('test2'))['Items'])
    print(resp)

    print(len(table.query(KeyConditionExpression=Key("email").eq('test@gmail.com'))['Items'][0]['follower']))

