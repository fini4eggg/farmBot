from telegram.telegrambot import TelegramBot
from checkbirdname import check_name
from farm import Farm
import time

if __name__ == '__main__': #точка входа
    update_id = 0
    start_message_id = 0
    while 1 < 2: #
        new_messages_as_json = TelegramBot.get_new_messages_as_json(update_id + 1) #class telegram

        if new_messages_as_json != "error":
            if "result" in new_messages_as_json:
                results = new_messages_as_json["result"]
                if len(results) > 0:
                    for result in results:
                        text = ""
                        chat_id = 0
                        chat_user_name = ""

                        if "update_id" in result: #если существует
                            update_id = max(update_id, result["update_id"])

                        if "message" in result: #объект сообщения
                            message = result["message"]

                            if "text" in message: #достаём данные
                                text = message["text"]

                            if "chat" in message:
                                chat = message["chat"]
                                if "id" in chat:
                                    chat_id = chat["id"]
                                if "first_name" in chat:
                                    chat_user_name = chat["first_name"]

                        m = 1
                        for i in range(m):
                            farm = Farm()
                            bird = check_name(text)
                            print(bird)
                            message_super = farm.get_eggs(bird)
                            print(f"Сообщение от {chat_user_name}: \"{text}\", чат ID: {chat_id}")
                            start_message_id = start_message_id + 1
                            post_message_as_json = TelegramBot.post_message(chat_id, f"Ответочка {i+1} № {start_message_id}")

                            if post_message_as_json != "error":
                                if "ok" in post_message_as_json:
                                    if post_message_as_json["ok"]:
                                        print(f"Ответочка ушла -> {chat_user_name}")
                                    else:
                                        print(f"Oops... Ответочка{i+1} не ушла")
                                else:
                                    print(f"Oops... Ответочка{i+1} не ушла")
                            else:
                                print("...")  # Новых сообщений нет
        else:
            print("Oops...")

        time.sleep(1)