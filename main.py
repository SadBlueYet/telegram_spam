import asyncio
import os
from telethon.sync import TelegramClient, functions


async def read_session():
    files = os.listdir("sessions")
    session_list = []

    for file in files:
        session_list.append(file)

    return session_list


async def send_sticker(client, chat, session):
    try:
        entity = await client.get_entity(chat)
        channel_entity = await client.get_entity(
            "mamuebal555"
        )  # Получение чата для пересылки

        await client.send_message(entity, "/start")
        await client.send_message(entity, "/next")

        async for message in client.iter_messages(channel_entity, limit=1):
            if message.media:
                await client.send_file(entity, message.media)

        print("Сообщение успешно отправлено", session)
    except Exception as e:
        print("Возникла непредвиденная ошибка: ", e, session)
        pass


async def unblock_user(blocked_chats, client):  # Разблокировка чатов
    async with client:
        for chat in blocked_chats:
            await client(functions.contacts.UnblockRequest(chat))


async def check_blocked_chats(chats, client):
    for chat in chats:
        try:
            entity = await client.get_entity(chat)
            await client.send_message(entity, "/start")
        except Exception as e:
            print("Возникла непредвиденная ошибка: ", e)


async def work(session):
    api_id = 18754300
    api_hash = "c29179284fad5aa1f2818bfe27956ea9"

    # Путь к файлу сессии
    session_file = f"sessions\\{session}"

    # Создаем Telegram клиента
    client = TelegramClient(session_file, api_id, api_hash)
    async with client:
        chats = [
            "chatbot",
            "random_pacar_bot",
            "secretchat01bot",
            "AnonyMeetBot",
            "RandomChatssBot",
            "random_chat_anonymous_bot",
            "secretchat02bot",
            "secretchat03bot",
            "secretchat04bot",
            "secretchat05bot",
            "secretchat06bot",
            "RandomPacarBot",
            "RandomMeetBot",
            "roleplay_chatbot",
            "Anonymousrandomchattt_bot",
        ]

        await check_blocked_chats(chats, client)
        while True:
            for chat in chats:
                await send_sticker(client, chat, session)


async def main():
    session_list = await read_session()
    tasks = []
    for session in session_list:
        task = asyncio.create_task(work(session))
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
