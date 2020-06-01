# Buffer Overflows

## Table of Contents
* [Generic procedure (Windows or Linux)](#generic-procedure-windows-or-linux)
* [Buffer Overflow Tips](#buffer-overflow-tips)
* [pattern_create.rb](#pattern_createrb)
* [pattern_offset.rb](#pattern_offsetrb)
* [nasm_shell.rb](#nasm_shellrb)
* [Bad characters Python code](#bad-characters-python-code)
* [Windows Buffer Overflows](#windows-buffer-overflows)


## Generic procedure (Windows or Linux)
* Identify vulnerable input field and payload length that causes overflow (Fuzzing)
* Identify offsets
* Detect bad characters
* Identify jump instruction opcode and usable return address
* Generate shellcode
* Exploit!


## Buffer Overflow Tips
* 0x00 is usually a bad character, because it often serves as a string terminator in programming languages vulnerable to buffer overflows (C/C++).
* Return Addresses CANNOT contain bad characters (which is why the Return Address is identified after detecting bad characters).
* Confusing debugger errors encountered during bad character detection likely indicate a bad character.
* Shellcode will almost always be generated with the ```EXITFUNC=thread``` option.
* Some vulnerable programs/services will always crash from buffer overflow conditions, regardless of how much preparation/compensation is done during exploit development.


## pattern_create.rb
Provided by the Metasploit Framework. Create unique pattern payloads to detect register offsets.
```
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l [PAYLOAD_LENGTH]
```

## pattern_offset.rb
Provided by the Metasploit Framework. Identify exact offsets where unique patterns reside.
```
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q [VALUE] -l [PAYLOAD_LENGTH]
```

## nasm_shell.rb
Provided by the Metasploit Framework. Convert x86 Assembly Language instructions into corresponding hexadecimal opcodes.
```
/usr/share/metasploit-framework/tools/exploit/nasm_shell.rb
```


## Bad characters Python code
```
badchars = ("\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
		"\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
		"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
		"\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
		"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
		"\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
		"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
		"\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
		"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
		"\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
		"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
		"\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
		"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
		"\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
		"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
		"\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")
```


## Windows Buffer Overflows

### Set breakpoints in Immunity Debugger
* Goto memory address using ![](Go_to_address_button.png "Go to address in Disassembler") button
* Click displayed memory address
* Press F2
* If warning message is displayed, click Yes
* Breakpoint is set when memory address is highlighted in Blue.

### Search for module information in Immunity Debugger
```
!mona modules
```

### Search for opcode address within module in Immunity Debugger
```
!mona find -s "[OPCODE]" -m [MODULE]
```

### Convert string [STRING] to Little-Endian hexadecimal value (Python)
```
"[STRING]"[::-1].encode('hex').upper()
```
Can be useful for printing string-to-hexadecimal values in Windows buffer overflow exploits.

