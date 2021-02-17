from configparser import ConfigParser
file = "C:/Users/shuai.wang/PycharmProjects/loginPage/Config/config.ini"

class config():
    config = ConfigParser()
    config.read(file)
    userName = config["account"]["user"]
    passWord = config["account"]["pass"]
    homePage = config["homepage"]["url"]


