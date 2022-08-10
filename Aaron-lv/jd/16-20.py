#调度配置 21 13 * * 1 python3 /ql/jd/16-20.py
from telethon import TelegramClient
import os
current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)
client = TelegramClient("bot16-20", "18447760", "903253249f217e18b5bd656cb865b91f", connection_retries=None).start()
async def main():
    await client.send_message("@chriszhuli_bot", "/farm d2d528b637b048b38fc78a263b2c5a84&915c7e0c74a842aa99fab767c779f60d&bc26bfb704eb4c7bb5e94dffcfb78f9a&aa2a60d26bfa49289e44bdfd2d1a569d&0f3ed2cc9fcb428b8a08782e005b3d3e")
    await client.send_message("@chriszhuli_bot", "/pet MTAxNzIxMDc1MTAwMDAwMDA3MjczOTcwNw==&MTE1NDY3NTMwMDAwMDAwNjQ1OTk5Mzk=&MTEyNjkzMjAwMDAwMDAwMDY4NDYwNzMx&MTEzMzI1MTE4NTAwMDAwMDA3MTY2NzgxNw==&MTExMjUxMTM0MDAwMDAwMDcyNzMzMDMz")
    await client.send_message("@chriszhuli_bot", "/bean 4npkonnsy7xi2vvulsfi7jg2qbztrr2oap4v6ga&e7lhibzb3zek3eqet4z23uiwr2fxjxzwweod6ca&4y4xgqshhr6agkzdgmpgcxwiia&7ivox3fgpcw7vll232upayqxguakk7n7w35ivjy")
    await client.send_message("@chriszhuli_bot", "")
    await client.send_message("@chriszhuli_bot", "/sgmh T0205KkcCUV9sCOgZkyg6J9oCjVQmoaT5kRrbA&T0225KkcRxZI81PeJEvznPRYJwCjVQmoaT5kRrbA&T0225KkcRBYe8ADXcx6gx_dfcgCjVQmoaT5kRrbA&T015vfx1RxYe91DTT0cCjVQmoaT5kRrbA&T019tvlxQxYe8kneIhr2kPQCjVQmoaT5kRrbA")
    await client.send_message("@chriszhuli_bot", "/health T0205KkcCUV9sCOgZkyg6J9oCjVfnoaW5kRrbA&T0225KkcRxZI81PeJEvznPRYJwCjVfnoaW5kRrbA&T0225KkcRBYe8ADXcx6gx_dfcgCjVfnoaW5kRrbA&T015vfx1RxYe91DTT0cCjVfnoaW5kRrbA&T019tvlxQxYe8kneIhr2kPQCjVfnoaW5kRrbA")
    await client.send_read_acknowledge("@chriszhuli_bot")
with client:
    client.loop.run_until_complete(main())
