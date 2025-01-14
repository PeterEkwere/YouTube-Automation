import os
import sys
import dotenv


# NOTE: Global constants
RETRY = 3
LOADING_TIMEOUT = 10
LONG_LOADING_TIMEOUT = 30
STAND_BY_TIMEOUT = 15
TRANSITION_TIMEOUT = 5
SHORT_TIMEOUT = 2
MEDIUM_WAIT = [10, 20]
SHORT_WAIT = [2, 5]
VERY_SHORT_WAIT = [0, 1]
LONG_WAIT = [20, 40]
WIDE_WAIT = [1, 10]
PASTE_PERCENTAGE = 50
DISK_SPACE = 80.0
CHANGED_PASSWORD_SEPARATOR = '::::'
PASSWORD_LENGTH = 25
ACCOUNT_DISABLED_MESSAGE = 'Account disabled'
ACCOUNT_VERIFICATION_MESSAGE = 'Account required verification steps'
ACCOUNT_REQUIRED_CAPTCHA_MESSAGE = 'Account required captcha'
ACCOUNT_REJECTED_MESSAGE = 'Account rejected because of suspicious action'
ACCOUNT_PASSWORD_CHANGED_MESSAGE = 'Password changed'


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except (Exception, SyntaxError):
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# NOTE: Configuration
CWD = resource_path("")
TEMP_FOLDER = resource_path("temp")
os.makedirs(TEMP_FOLDER, exist_ok=True)
LOG_FILE = os.path.join(TEMP_FOLDER, 'output.log')
PROFILE_GOOGLE_FOLDER = os.path.join(TEMP_FOLDER, 'profiles')
BLANK_PROFILE_FOLDER = os.path.join(TEMP_FOLDER, 'blank_profiles')
PATCHED_DRIVER = os.path.join(TEMP_FOLDER, 'chromedriver.exe')
CHANGED_EMAILS_FILE = os.path.join(TEMP_FOLDER, 'changed_emails.log')
FALSE_EMAIL_FILE = os.path.join(TEMP_FOLDER, 'false_email.log')
PROXY_FOLDER = os.path.join(TEMP_FOLDER, 'proxy')
