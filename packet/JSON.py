import json
from importLib.ErrorLib import *


class JSON():
    @staticmethod
    def toJSON(obj):
        try:
            return json.dumps(obj, ensure_ascii=False)
        except Exception as e:
            LogCat.log(ErrLevel.unknown, traceback.format_exc())
            return None


    @staticmethod
    def toData(body):
        try:
            return json.loads(body)
        except json.decoder.JSONDecodeError:
            return None
        except Exception:
            LogCat.log(ErrLevel.unknown, traceback.format_exc())
            return None