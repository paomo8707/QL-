#调度配置 21 13 * * 1 python3 /ql/jd/1-5.py
from telethon import TelegramClient
import os
current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)
client = TelegramClient("bot1-5", "13357355", "efe90ec3efaeaddd9b0b98b56e0f2070", connection_retries=None).start()
async def main():
    await client.send_message("@chriszhuli_bot", "/farm d86d6e5220d54be0a667b1dec3798c53&c19d7fa425ac4abab40e155be5a0c6fd&3287ed6121304577a5cb04a662e411d3&e3c6499a38a64330ba64027d0407ad2a&ca614a81489a453eac5dbecb831a4e8d")
    await client.send_message("@chriszhuli_bot", "/pet MTEyNjkzMjAwMDAwMDAwMDQ5MzAzODU5&MTAxNzIxMDc1MTAwMDAwMDA1NTgwNTE2Nw==&MTEyNjkzMjAwMDAwMDAwMDQ5MjcxMDQ5&MTE1NDQ5OTIwMDAwMDAwNDM2NjQzNTE=&MTE1MzEzNjI2MDAwMDAwMDY2NjI4NzQ1")
    await client.send_message("@chriszhuli_bot", "/bean 4npkonnsy7xi3zaduph5l4na44kvgmniv2hqp2i&suqg5cye47cqnazzdrrymrzf3jsiwdvqke55kva&swycl32jzdcqbfjbxkoddgtoy4f22t6p66ti3ny&4npkonnsy7xi24qasuaz5d4k25s3flduwhmccji&ri72f67brtjywh5i6eg5xwpazq")
    await client.send_message("@chriszhuli_bot", "/jxfactory XkY6P2Ar0Sz3pMpqZNCvNg==&13-mRD8q87hMmLZMc0Yzpw==")
    await client.send_message("@chriszhuli_bot", "/sgmh T0225KkcRxsf9AHUI0z8l_9YfQCjVQmoaT5kRrbA&T0205KkcM0xwlTe_Q0-Py7FoCjVQmoaT5kRrbA&T022v_RxRhsf91HRPR73kP8NcQCjVQmoaT5kRrbA&T0225KkcRxYcoweBdR70kPECJQCjVQmoaT5kRrbA&T01296Q5GEddrAqACjVQmoaT5kRrbA")
    await client.send_message("@chriszhuli_bot", "/health T0225KkcRxsf9AHUI0z8l_9YfQCjVfnoaW5kRrbA&T0205KkcM0xwlTe_Q0-Py7FoCjVfnoaW5kRrbA&T022v_RxRhsf91HRPR73kP8NcQCjVfnoaW5kRrbA&T0225KkcRxYcoweBdR70kPECJQCjVfnoaW5kRrbA&T01296Q5GEddrAqACjVfnoaW5kRrbA")
    await client.send_read_acknowledge("@chriszhuli_bot")
with client:
    client.loop.run_until_complete(main())
