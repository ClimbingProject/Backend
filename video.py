from flask import Flask, jsonify, Blueprint, request, abort, send_file


video = Blueprint('video', __name__)


@video.route('/video')
def get_video():
    return send_file('zorro.mp4')#, attachment_filename='zorro.mp4')
