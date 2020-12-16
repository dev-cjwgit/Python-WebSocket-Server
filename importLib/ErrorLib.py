import traceback
from logcat.Logcat import LogCat, ErrLevel


errMsg_Unknown = {
    'ACTION': 'ERROR',
    'INFO': {'Message': '알 수 없는 오류가 발생하였습니다.'}
}

errMsg_WrongType = {
    'ACTION': 'ERROR',
    'INFO': {'Message': '허용하지 않는 데이터입니다.'}
}