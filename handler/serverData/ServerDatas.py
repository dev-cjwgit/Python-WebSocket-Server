import random

from handler.entity.EntityForm import RoomForm
from importLib.ErrorLib import *


class LectureRoom:
    lecture_list = dict()  # 실시간으로 진행중인 강의들
    pin_list = [_ for _ in range(100000, 1000000)]

    @classmethod
    def openRoom(cls,websocket, pin):
        cls.lecture_list[pin] = RoomForm(websocket)

    @classmethod
    def closeRoom(cls, pin):
        del cls.lecture_list[pin]

    @classmethod
    def existRoom(cls, pin):
        return pin not in cls.pin_list if 100000 <= pin <= 999999 else False

    @classmethod
    def getRoom(cls, pin):
        try:
            return cls.lecture_list[pin]
        except KeyError:
            return 0

    @classmethod
    def acquirePin(cls):
        try:
            pin = random.sample(cls.pin_list, 1)
            # pin = [123456]
            cls.pin_list.remove(pin[0])
            return pin[0]
        except ValueError:
            return 0
        except Exception:
            LogCat.log(ErrLevel.unknown, traceback.format_exc())
            return None

    @classmethod
    def releasePin(cls, pin):
        try:
            if pin not in cls.pin_list:
                cls.pin_list.append(pin)
                return True
            else:
                return False
        except Exception:
            LogCat.log(ErrLevel.unknown, traceback.format_exc())