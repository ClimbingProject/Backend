# Backend
### For testing in local
- simply run main.py to start api on the terminal

        python3 main.py
- start DynamoDB in local

    - If you haven't downloaded dynamoDB, dowload from [here](https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html)
    - Start DynamoDB on the terminal

            java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb

You can check what's in DynamoDB by this command on the terminal

    aws dynamodb list-tables --endpoint-url http://localhost:8000

lsit table

    aws dynamodb list-tables --endpoint-url http://localhost:8000

scan items in the table

    aws dynamodb scan --table-name Users --endpoint-url http://localhost:8000


delete table

    aws dynamodb delete-table --table-name Users --endpoint-url http://localhost:8000

delete item from table

    aws dynamodb delete-item --table-name Users --key "{\"email\": {\"S\": \"miguel@gmail.com\"}, \"password\":{\"S\": \"python\"}}" --endpoint-url http://localhost:8000

get item from table

    aws dynamodb get-item --table-name Users --key  "{\"email\": {\"S\": \"miguel@gmail.com\"}, \"password\":{\"S\": \"python\"}}" --endpoint-url http://localhost:8000