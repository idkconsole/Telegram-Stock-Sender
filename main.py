import asyncio
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

async def main():
    api_id = ''
    api_hash = ''

    session_string = None

    async with TelegramClient(StringSession(session_string), api_id, api_hash) as client:
        if session_string is None:
            pass
     

        group_ids = ['doscord', 'DiscordMp', 'paradisewts', 'LIGITSHOP', 'spiritwtb', 'sikeyyop', 'theneonmp', 'SpaceWts', 'sparkwtb', 'spikewts', 'kittywts']

        message_to_send = '''Discord Verified Bot

- Oge
- Pull warr
- Uhq names

Bin: ??

- Mm Accepted
- Custom Names Available
- Shop/Vouches - @discordverifiedbot | @discordverifiedbots
- Autobuy - https://consoleuwu.sellix.io/product/64ddeadec2f15'''

        counter = 1 

        while True:
            for group_id in group_ids:
                try:
                    await client.send_message(group_id, message_to_send)
                    print(f"[{counter}] Sent Stock In {group_id}")
                    counter += 1  
                except Exception as e:
                    print(f"Skipping {group_id} due to {e}")
            for i in range(1800, 0, -1):
                print(f"\r{i} seconds left until the next message.", end='')
                await asyncio.sleep(1)
            print()

if __name__ == '__main__':
    asyncio.run(main())
