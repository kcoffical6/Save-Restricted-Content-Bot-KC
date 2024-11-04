# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "26641371"))
API_HASH = getenv("API_HASH", "0852211c50c48131120e43b6eefaf828")
BOT_TOKEN = getenv("BOT_TOKEN", "6512161845:AAFk2j9npb6Jxr5CwOjda-0jVJhdDXl23o4")
OWNER_ID = int(getenv("OWNER_ID", "831370530"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://sharathjetty003:1CgLGiiQPpsk8Iwp@cluster0.ax69kxn.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = int(getenv("LOG_GROUP", "-4086789527""))
FORCESUB = getenv("FORCESUB", "-1002327114253")
