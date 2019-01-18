from flask import Flask, jsonify, Blueprint, request, abort, send_file
import boto3
import localstack_client.session

video = Blueprint('video', __name__)


# curl -i -X POST -H "Content-Type: application/json" -d '{"file_name": "zorro.mp4"}' http://0.0.0.0:3001/video/upload
@video.route('/video/upload', methods=['POST'])
def get_video():
    try:
        session = localstack_client.session.Session()
        # s3 = boto3.client('s3') <- Change to this when deploy.
        s3 = session.client('s3') # this is for local development purpose only

        file_path = request.json.get('file_name')
        s3.upload_file(
            Filename=file_path,
            Bucket='cp_s3',
            Key=file_path,
            ExtraArgs={"GrantRead": 'uri=http://acs.amazonaws.com/groups/global/AllUsers'}
        )

        s3.put_object_acl(
            Bucket='cp_s3',
            Key=file_path,
            GrantRead='uri="http://acs.amazonaws.com/groups/global/AllUsers"'
        )
        return jsonify({'ok': file_path}), 201

    except Exception as e:
        print(e)
        return 'ERROR\n', 400

    # return send_file('zorro.mp4')#, attachment_filename='zorro.mp4')
