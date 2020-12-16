from Actions.Host.HostAction import HostAction
from importLib.ErrorLib import *
from Actions.Player.PlayerAction import PlayerAction
from packet.JSON import JSON


class ServerHandler:
    @staticmethod
    async def recv(websocket, json):
        try:
            packet = JSON.toData(json)
            if packet is None:
                raise TypeError()

            opcode = packet['ACTION']
            if opcode == 'OPEN_ROOM':
                await HostAction.open_Room(websocket)
            elif opcode == 'CLOSE_ROOM':
                await HostAction.close_Room(websocket, packet['INFO']['Pin'])
            elif opcode == 'START_VOTE':
                await HostAction.start_Vote(websocket,
                                            packet['INFO']['Pin'],
                                            packet['INFO']['Title'],
                                            packet['INFO']['First_Example'],
                                            packet['INFO']['Second_Example'],
                                            packet['INFO']['Third_Example'],
                                            packet['INFO']['Fourth_Example'])
            elif opcode == 'END_VOTE':
                await HostAction.end_Vote(websocket, packet['INFO']['Pin'])
            elif opcode == 'PLAYER_LOGIN':
                await PlayerAction.loggined(websocket, packet['INFO']['Pin'], packet['INFO']['Name'])
            else:
                print('No OpCode')

        except KeyError:
            await websocket.send(JSON.toJSON(errMsg_WrongType))
        except TypeError:
            await websocket.send(JSON.toJSON(errMsg_WrongType))
        except Exception:
            await websocket.send(JSON.toJSON(errMsg_Unknown))
            LogCat.log(ErrLevel.unknown, traceback.format_exc())
