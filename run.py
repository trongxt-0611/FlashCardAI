from mysocket import create_app, socketio

app = create_app()
# 192.168.0.14
socketio.run(app, host="localhost", port=8080)
# sudo nohup /home/ubuntu/FlashCardAI/venv/bin/python3 run.py > log.txt 2>&1 &
