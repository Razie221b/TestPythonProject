import configparser

config = configparser.ConfigParser()
config.read('config.ini')

browser_name = config.get('Playwright', 'browser')
is_headless = config.getboolean('Playwright', 'headless')
time_out = config.getint('Playwright', 'timeout')
