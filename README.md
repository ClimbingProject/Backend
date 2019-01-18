# Backend
### For testing in local
- simply run main.py to start API on the terminal

        python3 main.py

- start mongoDB in terminal

        mongo ds157574.mlab.com:57574/climbing_project -u cp -p climbing_project1

- start AWS S3 on local

        $ pip3 install localstack awscli-local
        $ localstack start

- upload file to local S3

        awslocal s3 cp test2.txt s3://cp_s3/ --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers

- delete file from local S3

        awslocal s3 rm s3://cp_s3/zorro.mp4

Link for local S3 [tutorial]('https://medium.com/@andyalky/developing-aws-apps-locally-with-localstack-7f3d64663ce4')