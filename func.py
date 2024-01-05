import vk_api
import ast
import csv


def downloader(token: str, user_id: int) -> None:

    vk_session = vk_api.VkApi(token=token)
    session_api = vk_session.get_api()
    user_id = user_id

    f = open('vk_messages.txt', 'x', encoding="utf-8")

    lastMessage = session_api.messages.getHistory(count=1, peer_id=user_id)
    requestCount = int(lastMessage['items'][0]['id'] / 200 + 1)
    print("RequestCount (request - 200 messages): " + str(requestCount))

    for i in range(1, requestCount + 1):
        history = session_api.messages.getHistory(count=200, peer_id=user_id, start_message_id=200 * i)
        history = history['items']
        for j in reversed(history):
            f.write(str(j) + "\n")
        print("download "+str(i/requestCount*100)+"%")

    f.close()
    print("Done!")


def repeat_filt() -> None:

    inputFile = open('vk_messages.txt', 'r', encoding="utf-8")
    outputFile = open('vk_messages_processed.txt', 'w', encoding="utf-8")
    lastNum = 0

    for line in inputFile:
        myDict = ast.literal_eval(line)
        num = myDict['conversation_message_id']
        if (num > lastNum):
            outputFile.write(line)
            lastNum = num

    inputFile.close()
    outputFile.close()

    print("Done!")


def csv_table_maker(You: str, user_name: str) -> None:

    with open("vk_messages_processed.txt", "r", encoding="utf-8") as f:
        with open(f"{user_name}_file.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=";")
            for i in f:
                user = i.split(", ")[1]
                mess = i.split(", ")[-1][9:-3:1]
                if i.split(", ")[-1][1:5] == "text" and mess != '':
                    if user.split(" ")[-1] == '255425921':
                        writer.writerow([You, mess])
                    else:
                        writer.writerow([user_name, mess])

    print("Done!")
