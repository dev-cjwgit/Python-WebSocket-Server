from packet.JSON import *
from importLib.ErrorLib import *


class PlayerPacket:
    @staticmethod
    def Start_Vote(title, ex1, ex2, ex3, ex4):
        try:
            msg = {
                'ACTION': 'START_VOTE',
                'INFO': {'Title': title,
                         'First_Example': ex1,
                         'Second_Example': ex2,
                         'Third_Example': ex3,
                         'Fourth_Example': ex4}
            }
            return JSON.toJSON(msg)
        except Exception:
            LogCat.log(ErrLevel.unknown, traceback.format_exc())
            return JSON.toJSON(errMsg_Unknown)

    @staticmethod
    def End_Vote():
        try:
            msg = {
                'ACTION': 'END_VOTE',
                'INFO': 'Nothing'
            }
            return JSON.toJSON(msg)
        except Exception:
            LogCat.log(ErrLevel.unknown, traceback.format_exc())
            return JSON.toJSON(errMsg_Unknown)
