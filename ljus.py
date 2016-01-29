import websocket

def send(option):
    ws = websocket.create_connection("ws://192.168.1.106:81")
    ws1 = websocket.create_connection("ws://192.168.1.107:81")
    print("Sending 'stuff'...")
    ws.send(option)
    ws1.send(option)
    print("Sent")
    print("Receiving...")
    result = ws.recv()
    print("Received {}".format(result))
    ws.close()