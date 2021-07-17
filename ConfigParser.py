import configparser


class ConfigParser:
    def __init__(self):
        self.config_parser = self.config_parser()
        self.LOGIN = self.config_parser[0]
        self.PASSWORD = self.config_parser[1]
        self.ADMIN_FRONT = self.config_parser[2]
        self.USER_FRONT = self.config_parser[3]



    def config_parser(self):
        path = '././configuration.config'
        path_py = '../../configuration.config'
        config = configparser.ConfigParser()
        try:
            config.read(path)
        except configparser.NoSectionError:
            config.read(path_py)
        login = config.get('user', 'username')
        password = config.get('user', 'password')
        admin_front = config.get('url', 'admin_front')
        user_front = config.get('url', 'user_front')
        return login, password, admin_front, user_front




