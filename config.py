import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "22525529")

API_HASH = os.environ.get("API_HASH", "840111f82bbd1d2d3de5055afccf6a92")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6028582039:AAEFsw1OW-gXg1fq74uNgzakwl-98YhCTCY") 

CHANNEL = os.environ.get("CHANNEL", "")

STRING = os.environ.get("STRING", "")

DB_NAME = os.environ.get("DB_NAME","Name")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Name:Name@cluster0.m12ofgg.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "90"))

LAZY_PIC = os.environ.get("LAZY_PIC", "https://graph.org/file/875bc8c833cfa79f4c272.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5450011131').split()]

PORT = os.environ.get('PORT', '8080')
