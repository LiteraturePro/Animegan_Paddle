import os
import io
import uuid
import sys
import cv2
import base64
import logging
import glob
import numpy as np
from PIL import Image
from io import BytesIO
from flask import Flask, render_template, make_response, flash
import flask
import paddlehub as hub

app = Flask(__name__)

#run_with_ngrok(app)   #starts ngrok when the app is run

def convert_bytes_to_image(img_name,img_bytes):
    #将bytes结果转化为字节流
    bytes_stream = BytesIO(img_bytes)
    #读取到图片
    roiimg = Image.open(bytes_stream)
    img_path = os.path.join('./input', img_name + ".jpg")
    imgByteArr = BytesIO()    #初始化一个空字节流
    roiimg.save(imgByteArr,format('PNG'))     #把我们得图片以‘PNG’保存到空字节流
    imgByteArr = imgByteArr.getvalue()    #无视指针，获取全部内容，类型由io流变成bytes。
    with open(img_path,'wb') as f:
        f.write(imgByteArr)

    return img_path


def paddl(input_img_path):
    model = hub.Module(name='animegan_v1_hayao_60', use_gpu=False)

    # 模型预测
    result = model.style_transfer(
        images=None,
        paths=[input_img_path],
        batch_size=1,
        output_dir='output',
        visualization=True,
        min_size=32,
        max_size=512
    )
    file = glob.glob(r"./output/*.jpg")
    for i in file:
        path = i
    return path 



@app.route('/')
@app.route('/api', methods=["POST", "GET"])
def api():
  try:
    img = flask.request.files["image"].read()
    img_name = str(uuid.uuid4())
    input_img_path = convert_bytes_to_image(img_name,img)
    image_save = paddl(input_img_path)
    with open(image_save, 'rb') as f:
      res = base64.b64encode(f.read())
    return res
  except Exception as e:
    logging.error(e)
    return "errorError occurred, please check the log output！"


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))