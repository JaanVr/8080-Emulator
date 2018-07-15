import binascii
with open("invaders.rom", 'rb') as f:
    rom = binascii.hexlify(f.read())
n = 2
rom = [int(rom[i:i+n], 16) for i in range(0, len(rom), n)]

PC = 0
while(PC < len(rom)):
    if (rom[PC] == 0x00):
        print("NOP")
        PC+=1
    elif(rom[PC] == 0xC3):
        print("JMP", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0xF5):
        print("PUSH PSW")
        PC+=1
    elif(rom[PC] == 0xC5):
        print("PUSH B")
        PC+=1
    elif(rom[PC] == 0xD5):
        print("PUSH D")
        PC+=1
    elif(rom[PC] == 0xE5):
        print("PUSH H")
        PC+=1
    elif(rom[PC] == 0x3E):
        print("MVI A,", hex(rom[PC+1]))
        PC+=2
    elif(rom[PC] == 0x32):
        print("STA,", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0x21):
        print("LXI H,", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0x35):
        print("DCR M")
        PC+=1
    elif(rom[PC] == 0xCD):
        print("CALL", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0xDB):
        print("IN,", hex(rom[PC+1]))
        PC+=2
    elif(rom[PC] == 0x0F):
        print("RRC")
        PC+=1
    elif(rom[PC] == 0xDA):
        print("JC,", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0x3A):
        print("LDA,", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0xA7):
        print("ANA A")
        PC+=1
    elif(rom[PC] == 0xCA):
        print("JZ,", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0xFE):
        print("CPI,", hex(rom[PC+1]))
        PC+=2
    elif(rom[PC] == 0xC6):
        print("ADI,", hex(rom[PC+1]))
        PC+=2
    elif(rom[PC] == 0x27):
        print("DAA")
        PC+=1
    elif(rom[PC] == 0xAF):
        print("XRA A")
        PC+=1
    elif(rom[PC] == 0xC2):
        print("JNZ,", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0xE1):
        print("POP H")
        PC+=1
    elif(rom[PC] == 0xD1):
        print("POP D")
        PC+=1
    elif(rom[PC] == 0xC1):
        print("POP B")
        PC+=1
    elif(rom[PC] == 0xF1):
        print("POP PSW")
        PC+=1
    elif(rom[PC] == 0xFB):
        print("EI")
        PC+=1
    elif(rom[PC] == 0xC9):
        print("RET")
        PC+=1
    elif(rom[PC] == 0xD2):
        print("JNC", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0x7E):
        print("MOV A,M")
        PC+=1
    elif(rom[PC] == 0x23):
        print("INX H")
        PC+=1
    elif(rom[PC] == 0x66):
        print("MOV H,M")
        PC+=1
    elif(rom[PC] == 0x6F):
        print("MOV L,A")
        PC+=1
    elif(rom[PC] == 0x22):
        print("SHLD,", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0x2B):
        print("DCX H")
        PC+=1
    elif(rom[PC] == 0x3D):
        print("DCR A")
        PC+=1
    elif(rom[PC] == 0x3C):
        print("INR A")
        PC+=1
    elif(rom[PC] == 0x67):
        print("MOV H,A")
        PC+=1
    elif(rom[PC] == 0x46):
        print("MOV B,M")
        PC+=1
    elif(rom[PC] == 0xE6):
        print("ANI,", hex(rom[PC+1]))
        PC+=2
    elif(rom[PC] == 0x07):
        print("RLC")
        PC+=1
    elif(rom[PC] == 0x5F):
        print("MOV E,A")
        PC+=1
    elif(rom[PC] == 0x16):
        print("MVI D,", hex(rom[PC+1]))
        PC+=2
    elif(rom[PC] == 0x19):
        print("DAD D")
        PC+=1
    elif(rom[PC] == 0xEB):
        print("XCHG")
        PC+=1
    elif(rom[PC] == 0x78):
        print("MOV A,B")
        PC+=1
    elif(rom[PC] == 0xC4):
        print("CNZ,", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0x2A):
        print("LHLD,", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0x06):
        print("MVI B,", hex(rom[PC+1]))
        PC+=2
    elif(rom[PC] == 0xC8):
        print("RZ")
        PC+=1
    elif(rom[PC] == 0xC0):
        print("RNZ")
        PC+=1
    elif(rom[PC] == 0xCC):
        print("CZ,", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0x05):
        print("DCR B")
        PC+=1
    elif(rom[PC] == 0x61):
        print("MOV H,C")
        PC+=1
    elif(rom[PC] == 0x7D):
        print("MOV A,L")
        PC+=1
    elif(rom[PC] == 0x7A):
        print("MOV A,D")
        PC+=1
    elif(rom[PC] == 0x4E):
        print("MOV C,M")
        PC+=1
    elif(rom[PC] == 0xFA):
        print("JM,", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0xDE):
        print("SBI,", hex(rom[PC+1]))
        PC+=2
    elif(rom[PC] == 0x47):
        print("MOV B,A")
        PC+=1
    elif(rom[PC] == 0x7B):
        print("MOV A,E")
        PC+=1
    elif(rom[PC] == 0x14):
        print("INR D")
        PC+=1
    elif(rom[PC] == 0x68):
        print("MOV L,B")
        PC+=1
    elif(rom[PC] == 0x79):
        print("MOV A,C")
        PC+=1
    elif(rom[PC] == 0x4F):
        print("MOV C,A")
        PC+=1
    elif(rom[PC] == 0x15):
        print("DCR D")
        PC+=1
    elif(rom[PC] == 0x36):
        print("MVI M,", hex(rom[PC+1]))
        PC+=2
    elif(rom[PC] == 0x77):
        print("MOV M,A")
        PC+=1
    elif(rom[PC] == 0x86):
        print("ADD M")
        PC+=1
    elif(rom[PC] == 0x11):
        print("LXI D,", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0x0E):
        print("MVI C,", hex(rom[PC+1]))
        PC+=2
    elif(rom[PC] == 0x0D):
        print("DCR C")
        PC+=1
    elif(rom[PC] == 0x01):
        print("LXI B,", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0xB0):
        print("ORA B")
        PC+=1
    elif(rom[PC] == 0x56):
        print("MOV D,M")
        PC+=1
    elif(rom[PC] == 0x5E):
        print("MOV E,M")
        PC+=1
    elif(rom[PC] == 0xE3):
        print("XTHL")
        PC+=1
    elif(rom[PC] == 0xE9):
        print("PCHL")
        PC+=1
    elif(rom[PC] == 0x04):
        print("INR B")
        PC+=1
    elif(rom[PC] == 0x70):
        print("MOV M,B")
        PC+=1
    elif(rom[PC] == 0x31):
        print("LXI SP,", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0x73):
        print("MOV M,E")
        PC+=1
    elif(rom[PC] == 0x72):
        print("MOV M,D")
        PC+=1
    elif(rom[PC] == 0xD3):
        print("OUT,", hex(rom[PC+1]))
        PC+=2
    elif(rom[PC] == 0x85):
        print("ADD L")
        PC+=1
    elif(rom[PC] == 0xD0):
        print("RNC")
        PC+=1
    elif(rom[PC] == 0x34):
        print("INR M")
        PC+=1
    elif(rom[PC] == 0x2C):
        print("INR L")
        PC+=1
    elif(rom[PC] == 0x2E):
        print("MVI L,", hex(rom[PC+1]))
        PC+=2
    elif(rom[PC] == 0x71):
        print("MOV M,C")
        PC+=1
    elif(rom[PC] == 0xB4):
        print("ORA H")
        PC+=1
    elif(rom[PC] == 0xB8):
        print("CMP B")
        PC+=1
    elif(rom[PC] == 0xD6):
        print("SUI,", hex(rom[PC+1]))
        PC+=2
    elif(rom[PC] == 0xF6):
        print("ORI,", hex(rom[PC+1]))
        PC+=2
    elif(rom[PC] == 0xBE):
        print("CMP M")
        PC+=1
    elif(rom[PC] == 0x80):
        print("ADD B")
        PC+=1
    elif(rom[PC] == 0x97):
        print("SUB A")
        PC+=1
    elif(rom[PC] == 0x69):
        print("MOV L,C")
        PC+=1
    elif(rom[PC] == 0x37):
        print("STC")
        PC+=1
    elif(rom[PC] == 0xA0):
        print("ANA B")
        PC+=1
    elif(rom[PC] == 0x1A):
        print("LDAX D")
        PC+=1
    elif(rom[PC] == 0x13):
        print("INX D")
        PC+=1
    elif(rom[PC] == 0x26):
        print("MVI H,", hex(rom[PC+1]))
        PC+=2
    elif(rom[PC] == 0x29):
        print("DAD H")
        PC+=1
    elif(rom[PC] == 0x7C):
        print("MOV A,H")
        PC+=1
    elif(rom[PC] == 0xD4):
        print("CNC, ", hex(rom[PC+1]), hex(rom[PC+2]))
        PC+=3
    elif(rom[PC] == 0xD8):
        print("RC")
        PC+=1
    elif(rom[PC] == 0x24):
        print("INR H")
        PC+=1
    elif(rom[PC] == 0x83):
        print("ADD E")
        PC+=1
    elif(rom[PC] == 0x8A):
        print("ADC D")
        PC+=1
    elif(rom[PC] == 0x57):
        print("MOV D,A")
        PC+=1
    elif(rom[PC] == 0x48):
        print("MOV C,B")
        PC+=1
    elif(rom[PC] == 0x41):
        print("MOV B,C")
        PC+=1
    elif(rom[PC] == 0x08):
        print("UNSUPPORTED NOP")
        PC+=1
    elif(rom[PC] == 0x02):
        print("STAX B")
        PC+=1
    elif(rom[PC] == 0xB6):
        print("ORA M")
        PC+=1
    elif(rom[PC] == 0x09):
        print("DAD B")
        PC+=1
    elif(rom[PC] == 0x2F):
        print("CMA")
        PC+=1
    elif(rom[PC] == 0xA6):
        print("ANA M")
        PC+=1
    elif(rom[PC] == 0x12):
        print("STAX D")
        PC+=1
    elif(rom[PC] == 0xBC):
        print("CMP H")
        PC+=1
    elif(rom[PC] == 0x0C):
        print("INR C")
        PC+=1
    elif(rom[PC] == 0x65):
        print("MOV H,L")
        PC+=1
    elif(rom[PC] == 0x81):
        print("ADD C")
        PC+=1
    elif(rom[PC] == 0x1B):
        print("DCX D")
        PC+=1
    elif(rom[PC] == 0x25):
        print("DCR H")
        PC+=1
    elif(rom[PC] == 0x0A):
        print("LDAX B")
        PC+=1
    elif(rom[PC] == 0x03):
        print("INX B")
        PC+=1
    elif(rom[PC] == 0x8B):
        print("ADC E")
        PC+=1
    elif(rom[PC] == 0x28):
        print("UNSUPPORTED NOP")
        PC+=1
    elif(rom[PC] == 0xA8):
        print("XRA B")
        PC+=1
    elif(rom[PC] == 0x1C):
        print("INR E")
        PC+=1
    elif(rom[PC] == 0x10):
        print("UNSUPPORTED NOP")
        PC+=1
    elif(rom[PC] == 0x0B):
        print("DCX B")
        PC+=1
    elif(rom[PC] == 0xFF):
        print("RST 7")
        PC+=1
    elif(rom[PC] == 0x1F):
        print("RAR")
        PC+=1
    else:
        print(hex(rom[PC]))
        PC+=1
