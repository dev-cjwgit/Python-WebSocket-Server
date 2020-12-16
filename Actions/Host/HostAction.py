from encryption.ChiperAES import AEScipher
from handler.serverData.ServerDatas import LectureRoom
from importLib.ErrorLib import *
from packet.JSON import JSON
from handler.serverData.PeerConnection import connect_list
from packet.sendPacket.HostPacket import HostPacket
from packet.sendPacket.PlayerPacket import PlayerPacket

errMsg_NotOpenRoom = {
    'ACTION': 'ERROR',
    'INFO': {'Message': '열려있는 강의가 아닙니다.'}
}

errMsg_AlreadyOpenRoom = {
    'ACTION': 'ERROR',
    'INFO': {'Message': '이미 사용중인 핀번호입니다.'}
}


class HostAction:
    @staticmethod
    async def open_Room(websocket):
        try:
            pin = LectureRoom.acquirePin()
            if pin != 0:
                LectureRoom.openRoom(websocket, pin)
                await websocket.send(HostPacket.Create_Success_Room(pin))
            else:
                await websocket.send(JSON.toJSON(errMsg_AlreadyOpenRoom))

        except Exception:
            LogCat.log(ErrLevel.unknown, traceback.format_exc())
            await websocket.send(JSON.toJSON(errMsg_Unknown))

    @staticmethod
    async def close_Room(websocket, pin: int):
        try:
            # if type(pin) is not int:
            #     raise TypeError("허용하지 않는 데이터입니다.")
            if LectureRoom.existRoom(pin):
                LectureRoom.closeRoom(pin)
                LectureRoom.releasePin(pin)
            else:
                await websocket.send(JSON.toJSON(errMsg_NotOpenRoom))
        except TypeError as e:
            raise e
        except Exception:
            LogCat.log(ErrLevel.unknown, traceback.format_exc())
            await websocket.send(JSON.toJSON(errMsg_Unknown))

    @staticmethod
    async def start_Vote(websocket, pin:int, title, ex1, ex2, ex3, ex4):
        try:
            # if type(pin) is not int or \
            #         type(title) is not str or \
            #         type(ex1) is not str or \
            #         type(ex2) is not str or \
            #         type(ex3) is not str or \
            #         type(ex4) is not str:
            #     raise TypeError('허용하지 않는 데이터입니다.')

            if LectureRoom.existRoom(pin):
                lecture_info = LectureRoom.getRoom(pin)
                if lecture_info != 0:
                    var = lecture_info.peer_list
                    for i in var:
                        try:
                            await var[i][0].send(PlayerPacket.Start_Vote(title, ex1, ex2, ex3, ex4))
                        except Exception:
                            pass
                else:
                    await websocket.send(JSON.toJSON(errMsg_NotOpenRoom))
            else:
                await websocket.send(JSON.toJSON(errMsg_NotOpenRoom))
        except TypeError as e:
            raise e
        except Exception:
            LogCat.log(ErrLevel.unknown, traceback.format_exc())
            await websocket.send(JSON.toJSON(errMsg_Unknown))

    @staticmethod
    async def end_Vote(websocket, pin:int):
        try:
            # if type(pin) is not int:
            #     raise TypeError('pin 번호가 잘못 되었습니다.')
            if LectureRoom.existRoom(pin):
                lecture_info = LectureRoom.getRoom(pin)
                if lecture_info != 0:
                    var = lecture_info.peer_list
                    for i in var:
                        try:
                            await var[i][0].send(PlayerPacket.End_Vote())
                        except Exception:
                            pass
                else:
                    await websocket.send(JSON.toJSON(errMsg_NotOpenRoom))
            else:
                await websocket.send(JSON.toJSON(errMsg_NotOpenRoom))
        except TypeError as e:
            raise e
        except Exception:
            LogCat.log(ErrLevel.unknown, traceback.format_exc())
            await websocket.send(JSON.toJSON(errMsg_Unknown))
