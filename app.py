import os
import io
import uuid
import sys
import cv2
import base64
import logging
import numpy as np
from PIL import Image
from io import BytesIO
from flask import Flask, render_template, make_response, flash
import flask

import paddl
app = Flask(__name__)


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

@app.route('/')
@app.route('/animegan_v1_hayao_60', methods=["POST", "GET"])
def animegan_v1_hayao_60():
  try:
    img = flask.request.files["image"].read()
    num = 0
    img_name = str(uuid.uuid4())
    input_img_path = convert_bytes_to_image(img_name,img)
    output_img_path = paddl.main(num,input_img_path)
    # output_img_path = os.path.join('./output', img_name + ".png")
    with open(output_img_path, 'rb') as f:
      res = base64.b64encode(f.read())
    if os.path.exists(input_img_path):  # 如果文件存在
      os.remove(input_img_path)  
    else:
      logging.error('no such file')  # 则返回文件不存
    if os.path.exists(output_img_path):  # 如果文件存在
      os.remove(output_img_path)  
    else:
      logging.error('no such file')  # 则返回文件不存在
    return res
  except Exception as e:
    logging.error(e)
    return "errorError occurred, please check the log output！"

@app.route('/animegan_v2_hayao_64', methods=["POST", "GET"])
def animegan_v2_hayao_64():
  try:
    img = flask.request.files["image"].read()
    num = 1
    img_name = str(uuid.uuid4())
    input_img_path = convert_bytes_to_image(img_name,img)
    output_img_path = paddl.main(num,input_img_path)
    # output_img_path = os.path.join('./output', img_name + ".png")
    with open(output_img_path, 'rb') as f:
      res = base64.b64encode(f.read())
    if os.path.exists(input_img_path):  # 如果文件存在
      os.remove(input_img_path)  
    else:
      logging.error('no such file')  # 则返回文件不存
    if os.path.exists(output_img_path):  # 如果文件存在
      os.remove(output_img_path)  
    else:
      logging.error('no such file')  # 则返回文件不存在
    return res
  except Exception as e:
    logging.error(e)
    return "errorError occurred, please check the log output！"

@app.route('/animegan_v2_hayao_99', methods=["POST", "GET"])
def animegan_v2_hayao_99():
  try:
    img = flask.request.files["image"].read()
    num = 2
    img_name = str(uuid.uuid4())
    input_img_path = convert_bytes_to_image(img_name,img)
    output_img_path = paddl.main(num,input_img_path)
    # output_img_path = os.path.join('./output', img_name + ".png")
    with open(output_img_path, 'rb') as f:
      res = base64.b64encode(f.read())
    if os.path.exists(input_img_path):  # 如果文件存在
      os.remove(input_img_path)  
    else:
      logging.error('no such file')  # 则返回文件不存
    if os.path.exists(output_img_path):  # 如果文件存在
      os.remove(output_img_path)  
    else:
      logging.error('no such file')  # 则返回文件不存在
    return res
  except Exception as e:
    logging.error(e)
    return "errorError occurred, please check the log output！"

@app.route('/animegan_v2_paprika_74', methods=["POST", "GET"])
def animegan_v2_paprika_74():
  try:
    img = flask.request.files["image"].read()
    num = 3
    img_name = str(uuid.uuid4())
    input_img_path = convert_bytes_to_image(img_name,img)
    output_img_path = paddl.main(num,input_img_path)
    # output_img_path = os.path.join('./output', img_name + ".png")
    with open(output_img_path, 'rb') as f:
      res = base64.b64encode(f.read())
    if os.path.exists(input_img_path):  # 如果文件存在
      os.remove(input_img_path)  
    else:
      logging.error('no such file')  # 则返回文件不存
    if os.path.exists(output_img_path):  # 如果文件存在
      os.remove(output_img_path)  
    else:
      logging.error('no such file')  # 则返回文件不存在
    return res
  except Exception as e:
    logging.error(e)
    return "errorError occurred, please check the log output！"

@app.route('/animegan_v2_paprika_97', methods=["POST", "GET"])
def animegan_v2_paprika_97():
  try:
    img = flask.request.files["image"].read()
    num = 4
    img_name = str(uuid.uuid4())
    input_img_path = convert_bytes_to_image(img_name,img)
    output_img_path = paddl.main(num,input_img_path)
    # output_img_path = os.path.join('./output', img_name + ".png")
    with open(output_img_path, 'rb') as f:
      res = base64.b64encode(f.read())
    if os.path.exists(input_img_path):  # 如果文件存在
      os.remove(input_img_path)  
    else:
      logging.error('no such file')  # 则返回文件不存
    if os.path.exists(output_img_path):  # 如果文件存在
      os.remove(output_img_path)  
    else:
      logging.error('no such file')  # 则返回文件不存在
    return res
  except Exception as e:
    logging.error(e)
    return "errorError occurred, please check the log output！"

@app.route('/animegan_v2_paprika_98', methods=["POST", "GET"])
def animegan_v2_paprika_98():
  try:
    img = flask.request.files["image"].read()
    num = 5
    img_name = str(uuid.uuid4())
    input_img_path = convert_bytes_to_image(img_name,img)
    output_img_path = paddl.main(num,input_img_path)
    # output_img_path = os.path.join('./output', img_name + ".png")
    with open(output_img_path, 'rb') as f:
      res = base64.b64encode(f.read())
    if os.path.exists(input_img_path):  # 如果文件存在
      os.remove(input_img_path)  
    else:
      logging.error('no such file')  # 则返回文件不存
    if os.path.exists(output_img_path):  # 如果文件存在
      os.remove(output_img_path)  
    else:
      logging.error('no such file')  # 则返回文件不存在
    return res
  except Exception as e:
    logging.error(e)
    return "errorError occurred, please check the log output！"

@app.route('/animegan_v2_shinkai_33', methods=["POST", "GET"])
def animegan_v2_shinkai_33():
  try:
    img = flask.request.files["image"].read()
    num = 6
    img_name = str(uuid.uuid4())
    input_img_path = convert_bytes_to_image(img_name,img)
    output_img_path = paddl.main(num,input_img_path)
    # output_img_path = os.path.join('./output', img_name + ".png")
    with open(output_img_path, 'rb') as f:
      res = base64.b64encode(f.read())
    if os.path.exists(input_img_path):  # 如果文件存在
      os.remove(input_img_path)  
    else:
      logging.error('no such file')  # 则返回文件不存
    if os.path.exists(output_img_path):  # 如果文件存在
      os.remove(output_img_path)  
    else:
      logging.error('no such file')  # 则返回文件不存在
    return res
  except Exception as e:
    logging.error(e)
    return "errorError occurred, please check the log output！"

@app.route('/animegan_v2_shinkai_53', methods=["POST", "GET"])
def animegan_v2_shinkai_53():
  try:
    img = flask.request.files["image"].read()
    num = 7
    img_name = str(uuid.uuid4())
    input_img_path = convert_bytes_to_image(img_name,img)
    output_img_path = paddl.main(num,input_img_path)
    # output_img_path = os.path.join('./output', img_name + ".png")
    with open(output_img_path, 'rb') as f:
      res = base64.b64encode(f.read())
    if os.path.exists(input_img_path):  # 如果文件存在
      os.remove(input_img_path)  
    else:
      logging.error('no such file')  # 则返回文件不存
    if os.path.exists(output_img_path):  # 如果文件存在
      os.remove(output_img_path)  
    else:
      logging.error('no such file')  # 则返回文件不存在
    return res
  except Exception as e:
    logging.error(e)
    return "errorError occurred, please check the log output！"

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))