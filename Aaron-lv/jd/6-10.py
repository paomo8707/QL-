#调度配置 21 13 * * 1 python3 /ql/jd/6-10.py
from telethon import TelegramClient
import os
current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)
client = TelegramClient("bot6-10", "14730052", "7fffd96b7e366d09ea2fe3f07deb82fc", connection_retries=None).start()
async def main():
    await client.send_message("@chriszhuli_bot", "/farm c8329e724d3440f19ae364f1cf2cd4ec&0f1abf96a115492a80770edf53c8afc0&cbb7a8a72d48481391b510a692845e9d&5805f97ea7cd42a0b6aa31c98655c20a&422f8c7718ec4b7fb165d2817fe29ffd")
    await client.send_message("@chriszhuli_bot", "/pet MTAxNzIxMDc1MTAwMDAwMDA2NDQ5MDk5Mw==&MTEzMzI1MTE4NDAwMDAwMDA2ODMzNTAxOQ==&MTE1MzEzNjI2MDAwMDAwMDU1ODIwNjg1&MTEyNDExNjE0OTAwMDAwMDA0OTMwMzgwMw==&MTEzMzI1MTE4NDAwMDAwMDA1NTk5MjQwNQ==")
    await client.send_message("@chriszhuli_bot", "/bean e7lhibzb3zek3e23gjedptp6ejpnu4bvrzkl7lq&mlrdw3aw26j3wv25nbxubvhekvv5vcdm7sy6uoy&zaliiiainqveaxpq6vpb6o62xa&4hvf44mzmxrsgkydtagrqh27ky&olmijoxgmjuty3yhg47yedrpijkvfzcdr2sgf2i")
    await client.send_message("@chriszhuli_bot", "/jxfactory Bqw1NSaHLmXAMX0Ib4uLfw==")
    await client.send_message("@chriszhuli_bot", "/sgmh T0225KkcREse9VfSdU_2kaQPcgCjVQmoaT5kRrbA&T0225KkcRRhP_VzQdE7ynfUCdgCjVQmoaT5kRrbA&T012_KwzFVdGsFDTCjVQmoaT5kRrbA&T015_KIgG0ZGqAHWIhkCjVQmoaT5kRrbA&T0225KkcRkxP8AaCchj2lqQPJQCjVQmoaT5kRrbA")
    await client.send_message("@chriszhuli_bot", "/health T0225KkcREse9VfSdU_2kaQPcgCjVfnoaW5kRrbA&T0225KkcRRhP_VzQdE7ynfUCdgCjVfnoaW5kRrbA&T012_KwzFVdGsFDTCjVfnoaW5kRrbA&T015_KIgG0ZGqAHWIhkCjVfnoaW5kRrbA&T0225KkcRkxP8AaCchj2lqQPJQCjVfnoaW5kRrbA")
    await client.send_read_acknowledge("@chriszhuli_bot")
with client:
    client.loop.run_until_complete(main())
