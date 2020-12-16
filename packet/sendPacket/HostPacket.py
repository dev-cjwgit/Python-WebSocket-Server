from packet.JSON import *
from importLib.ErrorLib import *


class HostPacket:
    @staticmethod
    def Entered_Player_Information_RealTime(key, name):
        try:
            msg = {
                'ACTION': 'ENTERED_PLAYER_INFORMATION_REALTIME',
                'INFO': {'Key': key,
                         'Name': name}
            }
            return JSON.toJSON(msg)
        except Exception:
            LogCat.log(ErrLevel.unknown, traceback.format_exc())
            return JSON.toJSON(errMsg_Unknown)

    @staticmethod
    def Player_Vote_Information_RealTime(name, number):
        try:
            msg = {
                'ACTION': 'PLAYER_VOTE_INFORMATION_REALTIME',
                'INFO': {'Name': name, 'Number': number}
            }
            return JSON.toJSON(msg)
        except Exception:
            LogCat.log(ErrLevel.unknown, traceback.format_exc())
            return JSON.toJSON(errMsg_Unknown)

    @staticmethod
    def Create_Success_Room(pin):
        try:
            msg = {
                'ACTION': 'RESULT',
                'INFO': {'Pin': pin}
            }
            return JSON.toJSON(msg)
        except Exception:
            LogCat.log(ErrLevel.unknown, traceback.format_exc())
            return JSON.toJSON(errMsg_Unknown)
