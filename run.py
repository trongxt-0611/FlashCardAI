from mysocket import create_app, socketio

app = create_app()
# 192.168.0.14
socketio.run(app, host="localhost", port=8080)
