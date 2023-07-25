import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
#remove red
# Bot information
SESSION = environ.get('SESSION', 'Auto_Filters_Bot')
API_ID = int(environ.get('API_ID', ''))
API_HASH = environ.get('API_HASH', '')
BOT_TOKEN = environ.get('BOT_TOKEN', '')

# Bot pics and stickers
STICKERS = (environ.get('STICKERS', 'CAACAgUAAxkBAAEJLKBkeD9LiOezjPCmERpufnZ0dWrl2QAC-QwAAjJ64Fdi6S2huvv62y8E CAACAgUAAxkBAAEJLKJkeD9b8zRvOiHBkveN65cE8Xo3bwACBQcAAmfH4VcK_O85WZLeuC8E')).split()
PICS = (environ.get('PICS', 'https://graph.org/file/bea5a753b08ee6637ea19.jpg https://graph.org/file/79689d029702b89433802.jpg https://graph.org/file/e7d6b923dc3b5ac230f2d.jpg https://graph.org/file/d3f8356f68334d3d6469e.jpg https://graph.org/file/5929678d9b3ead121e0fe.jpg https://graph.org/file/d5bbd91bc31335cc5d767.jpg https://graph.org/file/3e9632d6c445ca43fce8f.jpg https://graph.org/file/1d7684b0aa371bb4cba52.jpg https://graph.org/file/953fb219ee7bcd047077e.jpg https://graph.org/file/ab51f955b0306ab3cee42.jpg https://graph.org/file/1a157b0d6dd42ea12c9a6.jpg https://graph.org/file/8dfdc6194a98c61e23633.jpg https://graph.org/file/8b4bac129ae77e36e3482.jpg https://graph.org/file/dbd94d6466ab540798dbd.jpg https://graph.org/file/2b4d482bebb59ba78cfd4.jpg https://graph.org/file/edfea7a6977abeeba2404.jpg')).split()

# Bot Admins
ADMINS = [int(admins) if id_pattern.search(admins) else admins for admins in environ.get('ADMINS', '').split()]
auth_users = [int(auth_users) if id_pattern.search(auth_users) else auth_users for auth_users in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []

# Channels
INDEX_CHANNELS = [int(index_channels) if id_pattern.search(index_channels) else index_channels for index_channels in environ.get('INDEX_CHANNELS', '').split()]
auth_channel = environ.get('AUTH_CHANNEL', '-1001948984400')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/+_yNt5j-90XBhM2M1')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/+rCvi2ObCCk5hOTk1')

# Bot settings
AUTO_FILTER = is_enabled((environ.get('AUTO_FILTER', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SPELL_CHECK = is_enabled(environ.get("SPELL_CHECK", "True"), True)
SHORTLINK = is_enabled((environ.get('SHORTLINK', "False")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "False")), False)
WELCOME = is_enabled((environ.get('WELCOME', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))

# Other
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>🚨 Requested Movie Name: {query} \n💁 Requested By: {message.from_user.mention} \n\n🏷 Title: <a href={url}>{title}</a> \n🎭 Genres: {genres} \n📆 Year: <a href={url}/releaseinfo>{year}</a> \n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10</b>")
FILE_CAPTION = environ.get("FILE_CAPTION", "<code>{file_name}</code>")
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "mdisklink.link")
SHORTLINK_API = environ.get("SHORTLINK_API", "48c239abf799bfcd27ac2c26a6698e895bc6d543")
WELCOME_TEXT = environ.get("WELCOME_TEXT", "Hello {mention}, Welcome to {title} group!")

# Log
LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("AUTO_FILTER is enabled.\n" if AUTO_FILTER else "AUTO_FILTER is disabled.\n")
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += (f"FILE_CAPTION enabled with value {FILE_CAPTION}, your files will be send along with this customized caption.\n" if FILE_CAPTION else "No FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("LONG_IMDB_DESCRIPTION enabled.\n" if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled, Plot will be shorter.\n")
LOG_STR += ("SPELL_CHECK Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK else "SPELL_CHECK Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in IMDB_TEMPLATE, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB_TEMPLATE is {IMDB_TEMPLATE}"
