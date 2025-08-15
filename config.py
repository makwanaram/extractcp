import os

class Config(object):
    # Telegram Bot ka token
    BOT_TOKEN = "7983413191:AAGMbDb9bqTTT68pMjjRd0Q4Y6y4UCyHITo"
    # Telegram API ki ID
    API_ID = 22727464
    # Telegram API ki hash key
    API_HASH = "f0e595a263c89aa17f6571b8af296ced"
    # Admin users ki IDs (comma se separate ki hui)
    ADMIN = '887699812'.split(',')
    # Admin IDs ko integer list mein convert karna
    ADMIN_ID = [int(id) for id in ADMIN]
    # MongoDB database ka URL
    DB_URL = "mongodb+srv://makwanaram:Hackthis008@cluster0.w69onvk.mongodb.net/?retryWrites=true&w=majority&appName=cpvodak"
    # Database ka naam
    DB_NAME = "MY_BOT_DB"
    # Text log channel ki ID
    TXT_LOG = -1002807057819
    # Authentication log channel ki ID
    AUTH_LOG = -1002807057819
    # Hit log channel ki ID
    HIT_LOG = -1002807057819
    # DRM dump channel ki ID
    DRM_DUMP = -1002807057819
    # Main channel ki ID
    CHANNEL = -1002807057819
    # Channel ka link
    CH_URL = "https://t.me/botnewmy"
    # Bot ke owner ka Telegram link
    OWNER = "https://t.me/jackmaheta"
    # Thumbnail image ka URL
    THUMB_URL = "https://telegra.ph/file/example-thumb-image.jpg" #Replace by with your Thumb URL
    # API host ka URL
    HOST = "https://www.masterapi.tech/"

