import websockets

from handler.serverData.ServerDatas import LectureRoom
from importLib.ErrorLib import *
from packet.JSON import JSON
from packet.sendPacket.HostPacket import HostPacket

uid_user = 1

errMsg_NotOpenRoom = {
    'ACTION': 'ERROR',
    'INFO': {'Message': '열려있는 강의가 아닙니다.'}
}


class PlayerAction:
    @staticmethod
    async def loggined(websocket, pin: int, name: str):
        global uid_user
        try:
            if type(pin) is not int or \
                    type(name) is not str:
                raise TypeError('허용하지 않는 데이터입니다.')
            if LectureRoom.existRoom(pin):
                lecture_info = LectureRoom.getRoom(pin)
                lecture_info.peer_list[uid_user] = (websocket, name)
                try:
                    await lecture_info.host.send(HostPacket.Entered_Player_Information_RealTime(uid_user, name))
                except websockets.exceptions.ConnectionClosedOK:
                    print()
                    pass  # host가 연결이 끊겼을 경우
                uid_user += 1
            else:
                await websocket.send(JSON.toJSON(errMsg_NotOpenRoom))

        except TypeError as e:
            raise e
        except Exception:
            LogCat.log(ErrLevel.unknown, traceback.format_exc())
            await websocket.send(JSON.toJSON(errMsg_Unknown))
