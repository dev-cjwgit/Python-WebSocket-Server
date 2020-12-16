import asyncio
import websockets
import ssl
import pathlib
from handler.ServerHandler import ServerHandler
from handler.serverData.PeerConnection import *
from serverConstants.ServerSettings import ServerInfoSetting
from importLib.ErrorLib import *


async def accept(websocket, path):
    _accept = False
    while True:
        try:
            if not _accept:
                if ServerInfoSetting.SHOW_ENTER_USER:
                    print("연결")
                _accept = True
                connect_list.append(websocket)

            data = await websocket.recv()

            if ServerInfoSetting.SHOW_RECV_PACKET:
                print("recvice : " + data)

            await ServerHandler.recv(websocket, data)
        except websockets.exceptions.ConnectionClosedOK as e:
            try:
                if ServerInfoSetting.SHOW_EXIT_USER:
                    print('사용자종료')
                connect_list.remove(websocket)
            finally:
                return
        except websockets.exceptions.ConnectionClosedError as e:
            try:
                if ServerInfoSetting.SHOW_EXIT_USER:
                    print('사용자 강제종료')
                connect_list.remove(websocket)
            finally:
                return
        except Exception as e:
            try:
                print('알 수 없는 오류' + str(e))
                connect_list.remove(websocket)
                LogCat.log(ErrLevel.unknown, traceback.format_exc())
            finally:
                return


def main():
    # WebSockets
    # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    # localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
    # ssl_context.load_cert_chain(localhost_pem)

    start_server = websockets.serve(accept, ServerInfoSetting.SERVER_IP, ServerInfoSetting.SERVER_PORT)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
    print('Finish')


if __name__ == "__main__":
    try:
        # aes = AEScipher()
        # data = aes.encrypt('최진우')
        # res = ''
        # for i in data:
        #     res += chr(i)
        # res1 = ''
        # for i in '최진우'.encode('utf8'):
        #     res1 += chr(i)
        # jsonto = {
        #     'Action':'Enter',
        #     'Info':{'Pin':123456, 'Key':res, 'Name':'최진우'}
        # }
        # sendtodata = JSON.toJSON(jsonto)
        # print(sendtodata)
        main()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print('main Err : ' + str(e))