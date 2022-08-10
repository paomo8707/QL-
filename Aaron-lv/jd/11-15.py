#调度配置 21 13 * * 1 python3 /ql/jd/11-15.py
from telethon import TelegramClient
import os
current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)
client = TelegramClient("bot11-15", "14800316", "8d074aa3695f7335dcc7cb45a0c82976", connection_retries=None).start()
async def main():
    await client.send_message("@chriszhuli_bot", "/farm c5c4a5b009904b62aa64166682481ac3&0c67936a7e314c27968bfca62bb5d04c&99e81a0e0f464eb69002c9a90559d0ae&0741f762e0664bdcaef977812b3905dd&971b9f4e428541afb1f1e4e168c3a2e9")
    await client.send_message("@chriszhuli_bot", "/pet MTAxNzIxMDc1MTAwMDAwMDA3MTAwNTc1MQ==&MTEzMzI1MTE4NTAwMDAwMDA1NTg5NDM3MQ==&MTAxNzIxMDc1MTAwMDAwMDA0OTQ3OTQ0OQ==&MTE0MDQ3MzEwMDAwMDAwNDkyNDcyMDM=&MTEyNzEzMjc0MDAwMDAwMDUwMDYzODM1")
    await client.send_message("@chriszhuli_bot", "/bean okj5ibnh3onz7yvgh33x73lwpmvj2tnzeal6kaq&4npkonnsy7xi2awzojgz4rliwbftopisiebdejy&wwvyldyl4sbhu2booo5jljyydu3h7wlwy7o5jii&igefhjvuw6xvsaww6o5d7nbxh2wnk2xahjkxo3i&mlrdw3aw26j3xbnpadpbgr5tfmdk6lq6gyc6q6a")
    await client.send_message("@chriszhuli_bot", "")
    await client.send_message("@chriszhuli_bot", "/sgmh T0205KkcAVd6gwa_e0Ss4axDCjVQmoaT5kRrbA&T0225KkcR0pN8lCFKEjwkvBcJwCjVQmoaT5kRrbA&T018v_h1QBsb8FfQJRub1ACjVQmoaT5kRrbA&T0205KkcAGdHqQqsSH6T8r5xCjVQmoaT5kRrbA&T0225KkcRR4ao12BKRj2kfEOJgCjVQmoaT5kRrbA")
    await client.send_message("@chriszhuli_bot", "/health T0205KkcAVd6gwa_e0Ss4axDCjVfnoaW5kRrbA&T0225KkcR0pN8lCFKEjwkvBcJwCjVfnoaW5kRrbA&T018v_h1QBsb8FfQJRub1ACjVfnoaW5kRrbA&T0205KkcAGdHqQqsSH6T8r5xCjVfnoaW5kRrbA&T0225KkcRR4ao12BKRj2kfEOJgCjVfnoaW5kRrbA")
    await client.send_read_acknowledge("@chriszhuli_bot")
with client:
    client.loop.run_until_complete(main())
