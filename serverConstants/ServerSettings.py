import os


class ServerInfoSetting:

    SERVER_FILE_PATH = '/'.join((os.path.dirname(os.path.realpath(__file__))).split('/')[0:-1]) + '/'
    #############################################################
    #                        DB Settings                        #
    #############################################################
    DB_HOST = '192.168.1.54'
    DB_USER = 'root'
    DB_PASSWORD = '!@Ss1235'
    DB_PORT = 3306
    DB_NAME = 'quizall'
    DB_LOGIN = 'user_account'

    DB_MAX_POOL_SIZE = 1000
    DB_TIMEOUT = 2
    DB_AUTO_COMMIT = True
    #############################################################
    #                      Server Settings                      #
    #############################################################
    SERVER_IP = '192.168.1.54'
    SERVER_PORT = 2000
    #############################################################
    #                     Log Show Settings                     #
    #############################################################
    SHOW_RECV_PACKET = False
    SHOW_SEND_PACKET = False

    SHOW_ERR_LOG_INFORMATION = True
    SHOW_ERR_LOG_WARNING = True
    SHOW_ERR_LOG_PROBLEM = True
    SHOW_ERR_LOG_CRITICAL = True
    SHOW_ERR_LOG_UNKNOWN = True

    SHOW_ENTER_USER = False
    SHOW_EXIT_USER = False

    SHOW_POOL_LOG = True  # DB Logs
