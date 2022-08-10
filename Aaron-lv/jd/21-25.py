#调度配置 21 13 * * 1 python3 /ql/jd/21-25.py
from telethon import TelegramClient
import os
current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)
client = TelegramClient("bot21-25", "13522180", "a69bf5e90e69fd116ba73939bc66b32d", connection_retries=None).start()
async def main():
    await client.send_message("@chriszhuli_bot", "/farm f4ab1d89f58849a68f17cc0e4d214873&899b99ab26ac407cad943bb7538a4052&c02b38e8b39643a0a0d2a7a36c7f6c62&ce471f2e6cb046d8ad75c223c1d11490&6da5b4c893bd4a4da948256a591b03d7")
    await client.send_message("@chriszhuli_bot", "/pet MTEyNzEzMjc0MDAwMDAwMDYzNzEzNzE3&MTExMjUxMTMzMDAwMDAwMDc1Mjg1MDYx&MTEzMzI1MTE4NDAwMDAwMDA3NzM2NzUxMw==&MTE1NDY3NTIwMDAwMDAwNTcwMTU0NTk=&MTAxODc2NTE0NzAwMDAwMDAyODkwOTg2OQ==")
    await client.send_message("@chriszhuli_bot", "/bean zaasc3rk7co6lqkct4jkjapuc4&tmhxvxgqd6m5ajlnwpg3u5vrau5ac3f4ijdgqji&olmijoxgmjutyf7i6qciy3bybbuoa3vkfrrkpgy&e7lhibzb3zek3cukrjs2a5bzknlrssgseopmjja&xadideawwcwbehlalmwooye4u3wwyubivh4rfli")
    await client.send_message("@chriszhuli_bot", "")
    await client.send_message("@chriszhuli_bot", "/sgmh T015_7xyRx8f8l3QIhgCjVQmoaT5kRrbA&T016Z2bblYeeIuxWJRj1CjVQmoaT5kRrbA&T0225KkcRk9P_F3fJhjwk_UNdgCjVQmoaT5kRrbA&T0225KkcRBtI8lyEcR-lk_5eIgCjVQmoaT5kRrbA&T020uvR7SB8b8VDKJhr2k_UDCjVQmoaT5kRrbA")
    await client.send_message("@chriszhuli_bot", "/health T015_7xyRx8f8l3QIhgCjVfnoaW5kRrbA&T016Z2bblYeeIuxWJRj1CjVfnoaW5kRrbA&T0225KkcRk9P_F3fJhjwk_UNdgCjVfnoaW5kRrbA&T0225KkcRBtI8lyEcR-lk_5eIgCjVfnoaW5kRrbA&T020uvR7SB8b8VDKJhr2k_UDCjVfnoaW5kRrbA")
    await client.send_read_acknowledge("@chriszhuli_bot")
with client:
    client.loop.run_until_complete(main())
