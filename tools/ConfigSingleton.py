import yaml

class ConfigSingleton:
    '''单例配置类'''
    _instance = None

    def __init__(self):
        f = open('config.yml', encoding='utf-8')
        self.config = yaml.load(f)
        f.close()


    @classmethod
    def getInstance(cls):
        if cls._instance == None:
            cls._instance = ConfigSingleton()
            return cls._instance
        return cls._instance

if __name__ == '__main__':
    s = ConfigSingleton.getInstance()
    s2 = ConfigSingleton.getInstance()
    print(s.config)
    print(id(s))
    print(id(s2))
