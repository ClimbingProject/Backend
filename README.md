# Backend
### For testing in local
- simply run main.py to start api on the terminal

        python3 main.py
- start DynamoDB in local

    - If you haven't downloaded dynamoDB, dowload from [here](https://docs.aws.amazon.com/ja_jp/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html)
    - Start DynamoDB on the terminal

            java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb

