import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27407065"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "5d2da4e9d218a170ca248b7cd2b93e2a")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://subhashkumar1918:D1c2qIPskJCpKuWY@cluster0.chcac00.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
