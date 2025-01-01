import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv()

# Jeton du bot @Botfather
TG_BOT_TOKEN = os.environ.get("7783135016:AAHjQYyKamQ-PPPIK6vr9au82vtPln-o5V4")

# Votre API ID de my.telegram.org
APP_ID = int(os.environ.get("24817837"))

# Votre API Hash de my.telegram.org
API_HASH = os.environ.get("acd9f0cc6beb08ce59383cf250052686")

# ID de votre canal DB
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))

# ID du propriétaire
OWNER_ID = int(os.environ.get("OWNER_ID"))

# Port
PORT = os.environ.get("PORT", "8080")

# Base de données
DB_URI = os.environ.get("DATABASE_URL")
DB_NAME = os.environ.get("DATABASE_NAME")

# ID du canal de souscription forcée, si vous voulez activer la souscription forcée
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1"))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2"))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3"))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4"))

# Nombre de travailleurs du bot TG
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Message de démarrage
START_MSG = os.environ.get("START_MESSAGE", "<b>ʙᴏɴᴊᴏᴜʀ {first}\n\n ᴊᴇ ꜱᴜɪꜱ ᴜɴ ʙᴏᴛ ᴅᴇ ꜱᴛᴏᴄᴋᴀɢᴇ ᴅᴇ ꜰɪᴄʜɪᴇʀꜱ ᴍᴜʟᴛɪᴘʟᴇ, ᴊᴇ ᴘᴇᴜx ꜱᴛᴏᴄᴋᴇʀ ᴅᴇꜱ ꜰɪᴄʜɪᴇʀꜱ ᴘʀɪᴠéꜱ ᴅᴀɴꜱ ᴜɴ ᴄᴀɴᴀʟ ꜱᴘéᴄɪꜰɪé ᴇᴛ ᴅ'ᴀᴜᴛʀᴇꜱ ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀꜱ ᴘᴇᴜᴠᴇɴᴛ ʏ ᴀᴄᴄéᴅᴇʀ ᴠɪᴀ ᴜɴ ʟɪᴇɴ ꜱᴘéᴄɪᴀʟ » @team_netflix</b>")
try:
    ADMINS = []
    for x in (os.environ.get("ADMINS")).split():
        ADMINS.append(int(x))
except ValueError:
    raise Exception("ᴠᴏᴛʀᴇ ʟɪꜱᴛᴇ ᴅ'ᴀᴅᴍɪɴɪꜱᴛʀᴀᴛᴇᴜʀꜱ ɴᴇ ᴄᴏɴᴛɪᴇɴᴛ ᴘᴀꜱ ᴅ'ᴇɴᴛɪᴇʀꜱ ᴠᴀʟɪᴅᴇꜱ.")

# Message de souscription forcée 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ᴅéꜱᴏʟé {first}, ᴛᴜ ᴅᴏɪꜱ ᴅ'ᴀʙᴏʀᴅ ʀᴇᴊᴏɪɴᴅʀᴇ ᴍᴇꜱ ᴄʜᴀîɴᴇꜱ ᴘᴏᴜʀ ᴀᴄᴄéᴅᴇʀ ᴀᴜx ꜰɪᴄʜɪᴇʀꜱ..\n\n ᴀʟᴏʀꜱ, ꜱ'ɪʟ ᴛᴇ ᴘʟᴀîᴛ, ʀᴇᴊᴏɪɴꜱ ᴍᴇꜱ ᴄʜᴀîɴᴇꜱ ᴅ'ᴀʙᴏʀᴅ ᴇᴛ ᴄʟɪQᴜᴇ ꜱᴜʀ ʟᴇ ʙᴏᴜᴛᴏɴ 'ᴄʟɪQᴜᴇᴢ ɪᴄɪ ᴍᴀɪɴᴛᴇɴᴀɴᴛ'....!")

# Définissez votre légende personnalisée ici, mettez None pour désactiver la légende personnalisée
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>» ʙʏ @team_netflix</b>")

# Définir True si vous voulez empêcher les utilisateurs de transférer des fichiers du bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Définir True si vous voulez désactiver le bouton de partage des publications de votre canal
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

# Texte des statistiques du bot
BOT_STATS_TEXT = "<b>UPTIME DU BOT</b>\n{uptime}"

# Texte de réponse utilisateur
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ᴛᴜ ɴ'ᴇs ᴘᴀs ᴍᴏɴ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍᴏɴ ᴘʀᴏᴘʀɪéᴛᴀɪʀᴇ : @sewxiy"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
