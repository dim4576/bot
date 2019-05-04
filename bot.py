from BotHandler import BotHandler
import datetime
import pickle
from models import ExecutorModel, ExecutorsModel

def push_units(base):
    with open('base.db', 'wb') as f:
        pickle.dump(base, f)

def pull_units():
    try:
        with open('base.db', 'rb') as f:
            return pickle.load(f)
    except Exception:
        base = ExecutorsModel()
        with open('base.db', 'wb') as f:
            pickle.dump(base, f)
        return base


token = "791919604:AAHEro1MZTV27yYouRLrmLjTGxuHJVEPDkk"

greet_bot = BotHandler(token)
greetings = ('здравствуй', 'привет', 'ку', 'здорово')
now = datetime.datetime.now()


def main():
    new_offset = None
    today = now.day
    hour = now.hour

    base = pull_units()

    while True:
        base = pull_units()
        greet_bot.get_updates(new_offset)

        last_update = greet_bot.get_last_update()
        if last_update != []:
            last_update_id = last_update['update_id']
            last_chat_text = last_update['message']['text']
            last_chat_id = last_update['message']['chat']['id']
            last_chat_name = last_update['message']['chat']['first_name']

        new_offset = last_update_id + 1

        if last_chat_text == '/reg':
            current = last_chat_id
            greet_bot.send_message(last_chat_id, 'enter serial: <[your phone number] [sity] [wish of work (y/n)]> without <> and []')
            while True:
                greet_bot.get_updates(new_offset)

                last_update = greet_bot.get_last_update()
                if last_update != []:
                    last_update_id = last_update['update_id']
                    last_chat_text = last_update['message']['text']
                    last_chat_id = last_update['message']['chat']['id']
                    last_chat_name = last_update['message']['chat']['first_name']
                    if current == last_chat_id:
                        unit = ExecutorModel()
                        unit.setId(current)
                        unit.setName(last_chat_name)
                        k = [i.strip() for i in last_chat_text.split()]
                        unit.setNumber(k[0])
                        unit.setSity(k[1])
                        if k[2] == 'y':
                            unit.setWish(True)
                        base.add(unit)
                        unit = None
                        push_units(base)
                        break



        new_offset = last_update_id + 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
