#调度配置 21 13 * * 1 python3 /ql/jd/31-35.py
from telethon import TelegramClient
import os
current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)
client = TelegramClient("bot31-35", "18466106", "f076086acc24640573dea29899fafe94", connection_retries=None).start()
async def main():
    await client.send_message("@chriszhuli_bot", "/farm 5aad1fb9f8c84e77b9190ccb6dd74b61&6b28fbfb3462411fa131364288d9f642&2eca17f9943e428280a3388e05814e51&eeb0a79a63be406b92e8d6cbc533366b&509395b46aec42f7b2bce5fd8691b1a5")
    await client.send_message("@chriszhuli_bot", "/pet MTE0MDQ3MzEwMDAwMDAwNDk0NDc0ODU=&MTExMTU4MDE0MjAwMDAwMDA5MTA0OTUxMw==&MTEzMzI1MTE4NDAwMDAwMDA2MTc3MDg5OQ==&MTExMjUxMTMzMDAwMDAwMDc2Nzc4OTEz&MTEyNjE3NTIzOTAwMDAwMDA5MzY0NjcyNw==")
    await client.send_message("@chriszhuli_bot", "/bean mlrdw3aw26j3xauuusfijr4o2nvbx67nuo5kl7y&g4wmjwdksxvx7p7jz4lbnuczsy&lxslbmbe3tkxfhbpuomhljetju3h7wlwy7o5jii&nkvdrkoit5o6426pyfrz432erhahh5t7n6usqja&v6n6ca3qujgk376ywwmaxfnibpvfiokib66udjy")
    await client.send_read_acknowledge("@chriszhuli_bot")
with client:
    client.loop.run_until_complete(main())
