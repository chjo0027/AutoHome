import websocket

def send(option):
    ws = websocket.create_connection("ws://192.168.1.106:81")
    ws1 = websocket.create_connection("ws://192.168.1.107:81")
    ws.send(option)
    ws1.send(option)
    ws.close()