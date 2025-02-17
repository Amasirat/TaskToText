from datetime import datetime
ENV_FILE = ".env"
OUT_DIR = "out.txt"
CHECKBOX = ":white_square_button:"
CHECKMARK = ":white_check_mark:"

def get_today():
    today = str(datetime.now())
    date = today.split(' ')
    return date[0]

def get_env(key: str):
    with open(ENV_FILE, "r") as envFile:
        for line in envFile:
            pair = line.split('=')
            if(pair[0] == key):
                return pair[1]
        
    raise Exception(f"Could not find needed Environment Variable {key}")

API_TOKEN = get_env("API_TOKEN")