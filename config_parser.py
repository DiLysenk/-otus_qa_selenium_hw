import configparser


class ConfigParser:

    def __init__(self):
        self.parsed = self.config_parser()
        self.LOGIN = self.parsed[0]
        self.PASSWORD = self.parsed[1]
        self.ADMIN_FRONT = self.parsed[2]
        self.USER_FRONT = self.parsed[3]
        self.apikey = self.parsed[4]
        self.apiuser = self.parsed[5]


    def config_parser(self):
        path = ['./test.config', '../test.config', '../../test.config', '././test.config']
        config = configparser.ConfigParser()
        for i in range(len(path)):
            try:
                config.read(path[i])
            except configparser.NoSectionError:
                raise AssertionError("конфигурационный файл не найден")
            if i == len(path) - 1:
                print("конфигурационный файл не найден")
                break
        login = config.get('user', 'username')
        password = config.get('user', 'password')
        admin_front = config.get('url', 'admin_front')
        user_front = config.get('url', 'user_front')
        api_key = config.get('api', 'user')
        api_user = config.get('api', 'apikey')
        return login, password, admin_front, user_front
