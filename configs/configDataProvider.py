import configparser
import os

from urllib.parse import urljoin

config = configparser.ConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'configs.ini')
config.read(config_path)

if not config.has_section('Playwright') or not config.has_section('Application'):
    raise RuntimeError("Missing sections in configs.ini")

browser_name = config.get('Playwright', 'browser')
is_headless = config.getboolean('Playwright', 'headless')
time_out = config.getint('Playwright', 'timeout')
width = config.getint('Playwright', 'width')
height = config.getint('Playwright', 'height')
ignoreHttpsErrors = config.getboolean('Playwright', 'ignoreHttpsErrors')

baseURL = config.get('Application', 'baseURL')
listURL = urljoin(baseURL, config.get('Endpoints', 'list'))
numberAdditionURL = urljoin(baseURL, config.get('Endpoints', 'numberAddition'))
numberDivisionURL = urljoin(baseURL, config.get('Endpoints', 'numberDivision'))
passwordRestoreURL = urljoin(baseURL, config.get('Endpoints', 'passwordRestore'))
updateProfileURL = urljoin(baseURL, config.get('Endpoints', 'updateProfile'))
numberMultiplicationURL = urljoin(baseURL, config.get('Endpoints', 'numberMultiplication'))
