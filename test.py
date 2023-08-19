from telethon.sync import TelegramClient
from colorama import init, Fore, Style
import os
import shutil
import pathlib


async def check_valid_session(session):
    init(autoreset=True)
    api_id = 18754300
    api_hash = "c29179284fad5aa1f2818bfe27956ea9"

    session_file = f"under\\{session}"
    client = TelegramClient(session_file, api_id, api_hash)

    try:
        async with client:
            await client.start()
            me = await client.get_me()
            print(
                f"Сессия {Fore.YELLOW}{session}{Style.RESET_ALL} {Fore.GREEN}валидна{Style.RESET_ALL}\n"
                f"и перенесена в папку {Fore.CYAN}sessions"
            )
            source_path = f"under/{session}"
            destination_path = f"sessions/{session}"
            await client.disconnect()
            await shutil.move(source_path, destination_path)

            await os.remove(f"under\\{session}")

    except Exception as e:
        print(e)


async def main():
    files = os.listdir("under")

    for file in files:
        await check_valid_session(file)


# Запускаем асинхронную функцию
if __name__ == "__main__":
    import asyncio

    list = []

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
