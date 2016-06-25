import API2
import telepot
import time
import configuration


def handle_plugins(user, args):
    message = ""
    for p in api.plugins():
        message += p["name"] + "\n"
    bot.sendMessage(user["id"], message)


def handle_online(user, args):
    players = api.players.online()
    count = len(players)
    msg = ""
    if count == 0:
        msg = "No players are online"
    else:
        for player in players:
            print player
            msg += player["name"] + "\n"
    bot.sendMessage(user["id"], msg)


commands = {
    "plugins": handle_plugins,
    "online": handle_online
}


def handle_msg(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print content_type, chat_type, chat_id
    if 'text' in msg and msg['text'][0] == "/":
        text = msg["text"]
        user = msg["from"]
        elements = text.strip().split(" ")
        cmd = elements[0][1:]
        args = elements[1:]
        print cmd
        print args
        if cmd in commands:
            commands[cmd](user, args)
        else:
            bot.sendMessage(user["id"], "Invalid Command")




# Load config
config = configuration.load_config()

# Setup server connection
conn = API2.Connection(host=config["json_api"]["host"], username=config["json_api"]["username"], password=config["json_api"]["password"], port=config["json_api"]["port"])
api = API2.JSONAPI(conn)

# Setup telegram connection
bot = telepot.Bot(config["telegram"]["api_token"])

bot.notifyOnMessage(handle_msg)

print "Running"

while True:
    time.sleep(30)
