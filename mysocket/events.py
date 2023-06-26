from flask import request
from flask_socketio import SocketIO
from flask_socketio import send, emit
import base64
import easyocr

from PIL import Image
from io import BytesIO
# from gradio_client import Client
socketio = SocketIO(logger=True, engineio_logger=False)
from manga_ocr import MangaOcr
mocr = MangaOcr()

@socketio.on("connect")
def handle_connect():
    print("Client connected!")
    emit("message", "connected!")

@socketio.on("recognize")
def handle_user_join(base64_data):
    # print(f"--------data: {message}")
    imgdata = base64.b64decode(base64_data)
    # Create an in-memory stream for the decoded image data
    stream = BytesIO(imgdata)
    # Open the image using PIL
    image = Image.open(stream)
    # filename = 'llllllllll.jpg'  # I assume you have a way of picking unique filenames
    text = mocr(image)

    # with open(filename, 'wb') as f:
    #     f.write(imgdata)

    emit("recognize_result", text)
