import re, logging
from os import environ
from Script import script

def is_enabled(type, value):
    data = environ.get(type, str(value))
    if data.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif data.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        print(f'Error - {type} is invalid, exiting now')
        exit()

def is_valid_ip(ip):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.match(ip_pattern, ip) is not None

# Bot information
API_ID = environ.get('13050924')
if API_ID == 0:
    print('Error - API_ID is missing, exiting now')
    exit()
else:
    API_ID = API_ID
API_HASH = environ.get('fe442e491c1841a12daeb6754d133739')
if API_HASH == 0:
    print('Error - API_HASH is missing, exiting now')
    exit()
BOT_TOKEN = environ.get('6140001085:AAGmOgkCQilSIsKFowkxcMV_j1QhUY1zyHM')
if BOT_TOKEN == 0:
    print('Error - BOT_TOKEN is missing, exiting now')
    exit()
PORT = intenviron.get('PORT', '80')

# Bot pics
PICS = (environ.get('PICS', 'https://telegra.ph/file/58fef5cb458d5b29b0186.jpg https://telegra.ph/file/f0aa4f433132769f8970c.jpg https://telegra.ph/file/f515fbc2084592eca60a5.jpg https://telegra.ph/file/20dbdcffaa89bd3d09a74.jpg https://telegra.ph/file/6045ba953af4def846238.jpg')).split()

# Bot Admins
ADMINS = environ.get('1598575940')
if ADMINS == 0:
    print('Error - ADMINS is missing, exiting now')
    exit()
else:
    ADMINS = [admins for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [index_channels if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS', '').split()]
if INDEX_CHANNELS == 0:
    print('Info - INDEX_CHANNELS is empty')
AUTH_CHANNEL = [int(auth_channels) for auth_channels in environ.get('AUTH_CHANNEL', '').split()]
if AUTH_CHANNEL == 0:
    print('Info - AUTH_CHANNEL is empty')
LOG_CHANNEL = environ.get('LOG_CHANNEL', '')
if LOG_CHANNEL == 0:
    print('Error - LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = LOG_CHANNEL
IS_FSUB = is_enabled('IS_FSUB', True)

# support group
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '')
if SUPPORT_GROUP == 0:
    print('Error - SUPPORT_GROUP is missing, exiting now')
    exit()
else:
    SUPPORT_GROUP = int(SUPPORT_GROUP)

# for chatGPT
OPENAI_API = environ.get('OPENAI_API', '')
if OPENAI_API == 0:
    print('Info - OPENAI_API is empty')

# MongoDB information
DATABASE_URL = environ.get("mongodb+srv://vasanthakumar200612:Vasanthkumar@200612@autofilterbot.zidghl6.mongodb.net/?retryWrites=true&w=majority&appName=AutoFilterBot")
if DATABASE_URL == 0:
    print('Error - DATABASE_URL is missing, exiting now')
    exit()
DATABASE_NAME = environ.get("AutoFilterBot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/HA_Bots_Support')
OWNER_USERNAME = environ.get("OWNER_USERNAME", "https://t.me/Hansaka_Anuhas")
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/HA_Bots')
FILMS_LINK = environ.get('FILMS_LINK', 'https://t.me/HA_Films_World')
TUTORIAL = environ.get("TUTORIAL", "https://t.me/HA_Bots")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/HA_Bots")

# Bot settings
DELETE_TIME = int(environ.get('DELETE_TIME', 3600)) # Add time in seconds
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_BTN = int(environ.get('MAX_BTN', 10))
LANGUAGES = [language.lower() for language in environ.get('LANGUAGES', 'english hindi telugu tamil kannada malayalam').split()]
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "mdiskshortner.link")
SHORTLINK_API = environ.get("SHORTLINK_API", "36f1ae74ba1aa01e5bd73bdd0bc22aa915443501")
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]
PM_DELETE_TIME = int(environ.get('PM_DELETE_TIME', 600))

# boolean settings
IS_VERIFY = is_enabled('IS_VERIFY', False)
AUTO_DELETE = is_enabled('AUTO_DELETE', False)
WELCOME = is_enabled('WELCOME', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', False)
LONG_IMDB_DESCRIPTION = is_enabled("LONG_IMDB_DESCRIPTION", False)
LINK_MODE = is_enabled("LINK_MODE", True)
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
IMDB = is_enabled('IMDB', True)
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
SHORTLINK = is_enabled('SHORTLINK', False)

PAYMENT_QR = environ.get('PAYMENT_QR', 'http://graph.org/file/cacbbea472e5a48ce0d64.jpg')

# for stream
IS_STREAM = is_enabled('IS_STREAM', True)
BIN_CHANNEL = environ.get("BIN_CHANNEL", "")
if len(BIN_CHANNEL) == 0:
    print('Error - BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "")
if len(URL) == 0:
    print('Error - URL is missing, exiting now')
    exit()
else:
    if URL.startswith(('https://', 'http://')):
        if not URL.endswith("/"):
            URL += '/'
    elif is_valid_ip(URL):
        URL = f'http://{URL}/'
    else:
        print('Error - URL is not valid, exiting now')
        exit()

#others
REACTIONS = [
    "🔥", "❤️", "😍", "⚡", "😇",
    "🤩", "🎉", "🤗", "🤩", "😎",
    "🤝", "🤯", "🤓"
]
