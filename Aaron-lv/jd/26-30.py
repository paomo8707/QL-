#调度配置 21 13 * * 1 python3 /ql/jd/26-30.py
from telethon import TelegramClient
import os
current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)
client = TelegramClient("bot26-30", "11671238", "2d49e00dae8628c5e1ad91c94d99558a", connection_retries=None).start()
async def main():
    await client.send_message("@chriszhuli_bot", "/farm c7ef37b9ff644d4288274b0a68fcbb93&49cde5b2545247dbbe0678208720c409&0d49ec6cf43d467ca92cef8ed099711c&d3b8ea00f09b44c2a37c9f4d5ee40bfb")
    await client.send_message("@chriszhuli_bot", "/pet MTE0MDQ3MzEwMDAwMDAwNDkzMjA2NTk=&MTE1NDAxNzgwMDAwMDAwNDQ3MjM0NDk=&MTAxODc2NTEzNDAwMDAwMDAwNTUyNTE3MQ==&MTE5MzEwNTEzODAwMDAwMDA4MzU3NzE5NQ==&MTE5MzEwNTEzODAwMDAwMDA4NjM0MDQyOQ==")
    await client.send_message("@chriszhuli_bot", "/bean mlrdw3aw26j3xko52myawwst2ynjrgri6si2pja&e7lhibzb3zek272j74tzzeuqxjic3aunhnmhrpq&e7lhibzb3zek2xtcnai7rcq5tidqfz25mz45spy&mlrdw3aw26j3whxeq42ifhdp4wxothfmk53r7vy&olmijoxgmjuty2qlkczbsihas6b544hd23xfkjy")
    await client.send_message("@chriszhuli_bot", "")
    await client.send_message("@chriszhuli_bot", "/sgmh T0225KkcRRgf81Pechigl_VZJwCjVQmoaT5kRrbA&T0225KkcRBdPpFXVcxOhnKJfdwCjVQmoaT5kRrbA&T0225KkcRBcco1OFdhL8xfdccACjVQmoaT5kRrbA&T0225KkcRUtIpgeGJxjzl_8IdACjVQmoaT5kRrbA&T0225KkcRkoZ_VPfJUj2wvQDfACjVQmoaT5kRrbA")
    await client.send_message("@chriszhuli_bot", "/health T0225KkcRRgf81Pechigl_VZJwCjVfnoaW5kRrbA&T0225KkcRBdPpFXVcxOhnKJfdwCjVfnoaW5kRrbA&T0225KkcRBcco1OFdhL8xfdccACjVfnoaW5kRrbA&T0225KkcRUtIpgeGJxjzl_8IdACjVfnoaW5kRrbA&T0225KkcRkoZ_VPfJUj2wvQDfACjVfnoaW5kRrbA")
    await client.send_read_acknowledge("@chriszhuli_bot")
with client:
    client.loop.run_until_complete(main())
