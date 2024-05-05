# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "28350930")

API_HASH = os.environ.get("API_HASH", "80eeb1c7c4219b4db82f6b626b324e71")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6815899376:AAE5sNEPysFLCqKN-h_x-3GZ4JDTn5e2vAI") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Ratul") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "Ratulr_bot")     

DB_URL = os.environ.get("DB_URL", ""mongodb+srv://mssorifmadan0:kv6YX5WdCnNwy2Kk@cluster0.nomo1m0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0)
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5771398688').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
