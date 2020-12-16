import time
from serverConstants.ServerSettings import ServerInfoSetting


class ErrLevel:
    information = 0
    warning = 1
    problom = 2
    critical = 3
    unknown = 4


class LogCat:
    @staticmethod
    def log(level, traceback_log):
        '''
        :param level:  0:information  |  1:warning  |  2:problem  |  3:critical
        :param traceback_log: traceback.format_exc()
        :return: None
        '''
        global first_pos
        try:
            str_body = '\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n'
            traceback_log = str(traceback_log) if type(traceback_log) is not str else traceback_log
            err_info = traceback_log.split('\n')[-2]

            now = time.localtime()
            time_str = "%04d년%02d월%02d일 - %02d시%02d분%02d초" % \
                       (now.tm_year,
                        now.tm_mon,
                        now.tm_mday,
                        now.tm_hour,
                        now.tm_min,
                        now.tm_sec)

            str_body += time_str + ' 발생\n\n'
            for i, err in enumerate(traceback_log.split('File "')):
                if i == 0:
                    continue
                elif i == 1:
                    first_pos = err.split('\n')[0]
                str_body += str(i) + ' : ' + (err.split('\n')[0] + '\n')

            str_body += '\n\n' + err_info
            str_body += '\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ'

            path = ServerInfoSetting.SERVER_FILE_PATH + 'loglist/'
            if level == ErrLevel.information:
                level = 'information'
            elif level == ErrLevel.warning:
                level = 'warning'
            elif level == ErrLevel.problom:
                level = 'problem'
            elif level == ErrLevel.critical:
                level = 'critical'
            elif level == ErrLevel.unknown:
                level = 'unknown'

            path += level + '/'

            err_str = err_info.split(': ')[0]
            f = open(path + err_str + '.txt', 'a')
            f.write(str_body + '\n\n\n')
            f.close()
            if ServerInfoSetting.SHOW_ERR_LOG_INFORMATION or \
                    ServerInfoSetting.SHOW_ERR_LOG_WARNING or \
                    ServerInfoSetting.SHOW_ERR_LOG_PROBLEM or \
                    ServerInfoSetting.SHOW_ERR_LOG_CRITICAL or \
                    ServerInfoSetting.SHOW_ERR_LOG_UNKNOWN:
                print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
                print('[' + level + '] : ' + time_str + '\n' + err_str + '\n' + first_pos + '')
                print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ')
        except Exception as e:
            print('LogCat Error : ' + str(traceback_log))
