
class RoomForm:
    def __init__(self, websocket):
        self.host = websocket
        self.peer_list = dict()
