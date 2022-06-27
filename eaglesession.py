import asyncio
from pyrogram import Client

print("""\nWelcome To Eagle String Session\nGenerator © @EAGLEUB\n\n""")
print("""Enter Your Valid Details To Continue!\n\n """)

print("Enter your API values from my.telegram.org/apps below.\n\n")


async def main():
    api_id = int(input("API ID: "))
    api_hash = input("API HASH: ")
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        await app.send_message(
            "me",
            f"""<b>**This is your Eagle String Session**\n\n`{await app.export_session_string()}`\n\n**You have successfully generated your Eagle String Session ... Join @EAGLEUB for updates...<\b>"""
        )
        print(
            "Thanks for using Eagle Pyrogram String Generator Your String Session Successfully Saved In Your Telegram!!"
        )


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
