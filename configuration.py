import json
import os.path

CONFIG_NAME = "config.json"

def make_default():
    json_api = {
        "host": "localhost",
        "username": "admin",
        "password": "pfsense",
        "port": 20059
    }
    telegram = {
        "api_token": None
    }
    return {"json_api": json_api, "telegram": telegram}


def load_config():
    print "Loading"
    if not os.path.isfile(CONFIG_NAME):
        print "No config file found, creating default"
        return make_default()
    else:
        with open(CONFIG_NAME) as config_file:
            return json.load(config_file)


def save_config(config):
    with open(CONFIG_NAME,'w') as config_file:
        json.dump(config, config_file)


if __name__ == "__main__":
    config = load_config()
    print config
    save_config(config)

