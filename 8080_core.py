import binascii
import time

def listToByte(bitList):
    byte = 0
    index = 7
    for bit in bitList:
        byte |= bit << index
        index -= 1
    return byte

class Core(object):
    def __init__(self):
        with open("invaders.rom", 'rb') as f:
            self.rom = binascii.hexlify(f.read())
        n = 2
        self.rom = [int(self.rom[i:i+n], 16) for i in range(0, len(self.rom), n)]

        n=0x2000
        while(n<0x4000):
            self.rom.append(0)
            n+=1

        self.A = 0 
        self.B = 0
        self.C = 0
        self.D = 0
        self.E = 0
        self.H = 0
        self.L = 0
        self.PC = 0
        self.SP = 0
        self.S = 0 	
        self.Z = 0	
        self.AC = 0	
        self.P = 0	
        self.CY = 0
        self.done = False
        self.INTE = 0
        self.enableInterrupts = False

        #this doesnt work
        self.F = [self.S, self.Z, 0, self.AC, 0, self.P, 1, self.CY] 

        self.S = 1
        print(hex(listToByte(self.F)))
        self.S = 0

    def RST(self, ISR):
        print("INTERRUPT")
        self.SP -= 1
        self.rom[self.SP] = self.PC >> 8
        self.SP -= 1
        self.rom[self.SP] = self.PC & 0xFF 
        print("INTERRUPT PC", hex(self.PC))
        self.PC = 0
        self.PC = ISR << 3

    def tick(self):
        if (self.rom[self.PC] == 0x00):
            print("NOP")
            self.PC+=1
        elif(self.rom[self.PC] == 0xC3):
            print("JMP", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            highByte = self.rom[self.PC+2]
            lowByte = self.rom[self.PC+1]
            self.PC = highByte
            self.PC <<= 8
            self.PC |= lowByte
            print("JMP to", hex(self.PC))
        elif(self.rom[self.PC] == 0xF5):
            print("PUSH PSW")
            self.SP -= 1
            self.rom[self.SP] = self.A
            self.SP -= 1
            self.rom[self.SP] = listToByte(self.F)
            self.PC+=1
        elif(self.rom[self.PC] == 0xC5):
            print("PUSH B")
            self.SP -= 1
            self.rom[self.SP] = self.B
            self.SP -= 1
            self.rom[self.SP] = self.C
            self.PC+=1
        elif(self.rom[self.PC] == 0xD5):
            print("PUSH D")
            self.SP -= 1
            self.rom[self.SP] = self.D
            self.SP -= 1
            self.rom[self.SP] = self.E
            self.PC+=1
        elif(self.rom[self.PC] == 0xE5):
            print("PUSH H")
            self.SP -= 1
            self.rom[self.SP] = self.H
            self.SP -= 1
            self.rom[self.SP] = self.L
            self.PC+=1
        elif(self.rom[self.PC] == 0x3E):
            print("MVI A,", hex(self.rom[self.PC+1]))
            self.A = self.rom[self.PC+1]
            self.PC+=2
        elif(self.rom[self.PC] == 0x32):
            print("STA,", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            address = self.rom[self.PC+2]
            address <<= 8
            address |= self.rom[self.PC+1]
            self.rom[address] = self.A
            print("STA to", address)
            self.PC+=3
        elif(self.rom[self.PC] == 0x21):
            print("LXI H,", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            self.H = self.rom[self.PC+2]
            self.L = self.rom[self.PC+1]
            self.PC+=3
        elif(self.rom[self.PC] == 0x35):
            print("DCR M")
            self.PC+=1
        elif(self.rom[self.PC] == 0xCD):
            print("CALL", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            highByte = self.rom[self.PC+2]
            lowByte = self.rom[self.PC+1]
            #push the next sequential instruction address to stack
            self.PC += 3
            self.SP -= 1
            self.rom[self.SP] = self.PC >> 8
            self.SP -= 1
            self.rom[self.SP] = self.PC & 0xFF 
            self.PC = highByte
            self.PC <<= 8
            self.PC |= lowByte
            print("CALL to", hex(self.PC))
        elif(self.rom[self.PC] == 0xDB):
            print("IN,", hex(self.rom[self.PC+1]))
            self.PC+=2
        elif(self.rom[self.PC] == 0x0F):
            print("RRC")
            self.PC+=1
        elif(self.rom[self.PC] == 0xDA):
            print("JC,", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            self.PC+=3
        elif(self.rom[self.PC] == 0x3A):
            print("LDA,", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            self.PC+=3
        elif(self.rom[self.PC] == 0xA7):
            print("ANA A")
            self.PC+=1
        elif(self.rom[self.PC] == 0xCA):
            print("JZ,", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            self.PC+=3
        elif(self.rom[self.PC] == 0xFE):
            print("CPI,", hex(self.rom[self.PC+1]))
            self.PC+=2
        elif(self.rom[self.PC] == 0xC6):
            print("ADI,", hex(self.rom[self.PC+1]))
            self.PC+=2
        elif(self.rom[self.PC] == 0x27):
            print("DAA")
            self.PC+=1
        elif(self.rom[self.PC] == 0xAF):
            print("XRA A")
            self.PC+=1
        elif(self.rom[self.PC] == 0xC2):
            print("JNZ,", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            self.PC+=3
        elif(self.rom[self.PC] == 0xE1):
            print("POP H")
            self.L = self.rom[self.SP]
            self.SP += 1
            self.H = self.rom[self.SP]
            self.SP += 1
            self.PC+=1
        elif(self.rom[self.PC] == 0xD1):
            print("POP D")
            self.E = self.rom[self.SP]
            self.SP += 1
            self.D = self.rom[self.SP]
            self.SP += 1
            self.PC+=1
        elif(self.rom[self.PC] == 0xC1):
            print("POP B")
            self.C = self.rom[self.SP]
            self.SP += 1
            self.B = self.rom[self.SP]
            self.SP += 1
            self.PC+=1
        elif(self.rom[self.PC] == 0xF1):
            print("POP PSW")
            self.PC+=1
        elif(self.rom[self.PC] == 0xFB):
            print("EI")
            core.enableInterrupts = True
            self.PC+=1
        elif(self.rom[self.PC] == 0xC9):
            print("RET")
            self.PC = self.rom[self.SP]
            self.SP += 1
            self.PC |= self.rom[self.SP] << 8
            self.SP += 1
            print("RET to", hex(self.PC))
        elif(self.rom[self.PC] == 0xD2):
            print("JNC", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            self.PC+=3
        elif(self.rom[self.PC] == 0x7E):
            print("MOV A,M")
            self.PC+=1
        elif(self.rom[self.PC] == 0x23):
            print("INX H")
            self.PC+=1
        elif(self.rom[self.PC] == 0x66):
            print("MOV H,M")
            self.PC+=1
        elif(self.rom[self.PC] == 0x6F):
            print("MOV L,A")
            self.L = self.A
            self.PC+=1
        elif(self.rom[self.PC] == 0x22):
            print("SHLD,", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            self.PC+=3
        elif(self.rom[self.PC] == 0x2B):
            print("DCX H")
            self.PC+=1
        elif(self.rom[self.PC] == 0x3D):
            print("DCR A")
            self.PC+=1
        elif(self.rom[self.PC] == 0x3C):
            print("INR A")
            self.PC+=1
        elif(self.rom[self.PC] == 0x67):
            print("MOV H,A")
            self.H = self.A
            self.PC+=1
        elif(self.rom[self.PC] == 0x46):
            print("MOV B,M")
            self.PC+=1
        elif(self.rom[self.PC] == 0xE6):
            print("ANI,", hex(self.rom[self.PC+1]))
            self.PC+=2
        elif(self.rom[self.PC] == 0x07):
            print("RLC")
            self.PC+=1
        elif(self.rom[self.PC] == 0x5F):
            print("MOV E,A")
            self.E = self.A
            self.PC+=1
        elif(self.rom[self.PC] == 0x16):
            print("MVI D,", hex(self.rom[self.PC+1]))
            self.D = self.rom[self.PC+1]
            self.PC+=2
        elif(self.rom[self.PC] == 0x19):
            print("DAD D")
            self.PC+=1
        elif(self.rom[self.PC] == 0xEB):
            print("XCHG")
            self.PC+=1
        elif(self.rom[self.PC] == 0x78):
            print("MOV A,B")
            self.A = self.B
            self.PC+=1
        elif(self.rom[self.PC] == 0xC4):
            print("CNZ,", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            self.PC+=3
        elif(self.rom[self.PC] == 0x2A):
            print("LHLD,", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            self.PC+=3
        elif(self.rom[self.PC] == 0x06):
            print("MVI B,", hex(self.rom[self.PC+1]))
            self.B = self.rom[self.PC+1]
            self.PC+=2
        elif(self.rom[self.PC] == 0xC8):
            print("RZ")
            self.PC+=1
        elif(self.rom[self.PC] == 0xC0):
            print("RNZ")
            self.PC+=1
        elif(self.rom[self.PC] == 0xCC):
            print("CZ,", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            self.PC+=3
        elif(self.rom[self.PC] == 0x05):
            print("DCR B")
            self.PC+=1
        elif(self.rom[self.PC] == 0x61):
            print("MOV H,C")
            self.H = self.C
            self.PC+=1
        elif(self.rom[self.PC] == 0x7D):
            print("MOV A,L")
            self.A = self.L
            self.PC+=1
        elif(self.rom[self.PC] == 0x7A):
            print("MOV A,D")
            self.A = self.D
            self.PC+=1
        elif(self.rom[self.PC] == 0x4E):
            print("MOV C,M")
            self.PC+=1
        elif(self.rom[self.PC] == 0xFA):
            print("JM,", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            self.PC+=3
        elif(self.rom[self.PC] == 0xDE):
            print("SBI,", hex(self.rom[self.PC+1]))
            self.PC+=2
        elif(self.rom[self.PC] == 0x47):
            print("MOV B,A")
            self.B = self.A
            self.PC+=1
        elif(self.rom[self.PC] == 0x7B):
            print("MOV A,E")
            self.A = self.E
            self.PC+=1
        elif(self.rom[self.PC] == 0x14):
            print("INR D")
            self.PC+=1
        elif(self.rom[self.PC] == 0x68):
            print("MOV L,B")
            self.L = self.B
            self.PC+=1
        elif(self.rom[self.PC] == 0x79):
            print("MOV A,C")
            self.A = self.C
            self.PC+=1
        elif(self.rom[self.PC] == 0x4F):
            print("MOV C,A")
            self.C = self.A
            self.PC+=1
        elif(self.rom[self.PC] == 0x15):
            print("DCR D")
            self.PC+=1
        elif(self.rom[self.PC] == 0x36):
            print("MVI M,", hex(self.rom[self.PC+1]))
            self.PC+=2
        elif(self.rom[self.PC] == 0x77):
            print("MOV M,A")
            self.PC+=1
        elif(self.rom[self.PC] == 0x86):
            print("ADD M")
            self.PC+=1
        elif(self.rom[self.PC] == 0x11):
            print("LXI D,", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            self.D = self.rom[self.PC+2]
            self.E = self.rom[self.PC+1]
            self.PC+=3
        elif(self.rom[self.PC] == 0x0E):
            print("MVI C,", hex(self.rom[self.PC+1]))
            self.C = self.rom[self.PC+1]
            self.PC+=2
        elif(self.rom[self.PC] == 0x0D):
            print("DCR C")
            self.PC+=1
        elif(self.rom[self.PC] == 0x01):
            print("LXI B,", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            self.B = self.rom[self.PC+2]
            self.C = self.rom[self.PC+1]
            self.PC+=3
        elif(self.rom[self.PC] == 0xB0):
            print("ORA B")
            self.PC+=1
        elif(self.rom[self.PC] == 0x56):
            print("MOV D,M")
            self.PC+=1
        elif(self.rom[self.PC] == 0x5E):
            print("MOV E,M")
            self.PC+=1
        elif(self.rom[self.PC] == 0xE3):
            print("XTHL")
            self.PC+=1
        elif(self.rom[self.PC] == 0xE9):
            print("PCHL")
            self.PC+=1
        elif(self.rom[self.PC] == 0x04):
            print("INR B")
            self.PC+=1
        elif(self.rom[self.PC] == 0x70):
            print("MOV M,B")
            self.PC+=1
        elif(self.rom[self.PC] == 0x31):
            print("LXI SP,", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            self.SP = self.rom[self.PC+2]
            self.SP <<= 8
            self.SP |= self.rom[self.PC+1]
            self.PC+=3
            print("SP initialized to", hex(self.SP))
        elif(self.rom[self.PC] == 0x73):
            print("MOV M,E")
            self.PC+=1
        elif(self.rom[self.PC] == 0x72):
            print("MOV M,D")
            self.PC+=1
        elif(self.rom[self.PC] == 0xD3):
            print("OUT,", hex(self.rom[self.PC+1]))
            self.PC+=2
        elif(self.rom[self.PC] == 0x85):
            print("ADD L")
            self.PC+=1
        elif(self.rom[self.PC] == 0xD0):
            print("RNC")
            self.PC+=1
        elif(self.rom[self.PC] == 0x34):
            print("INR M")
            self.PC+=1
        elif(self.rom[self.PC] == 0x2C):
            print("INR L")
            self.PC+=1
        elif(self.rom[self.PC] == 0x2E):
            print("MVI L,", hex(self.rom[self.PC+1]))
            self.L = self.rom[self.PC+1]
            self.PC+=2
        elif(self.rom[self.PC] == 0x71):
            print("MOV M,C")
            self.PC+=1
        elif(self.rom[self.PC] == 0xB4):
            print("ORA H")
            self.PC+=1
        elif(self.rom[self.PC] == 0xB8):
            print("CMP B")
            self.PC+=1
        elif(self.rom[self.PC] == 0xD6):
            print("SUI,", hex(self.rom[self.PC+1]))
            self.PC+=2
        elif(self.rom[self.PC] == 0xF6):
            print("ORI,", hex(self.rom[self.PC+1]))
            self.PC+=2
        elif(self.rom[self.PC] == 0xBE):
            print("CMP M")
            self.PC+=1
        elif(self.rom[self.PC] == 0x80):
            print("ADD B")
            self.PC+=1
        elif(self.rom[self.PC] == 0x97):
            print("SUB A")
            self.PC+=1
        elif(self.rom[self.PC] == 0x69):
            print("MOV L,C")
            self.L = self.C
            self.PC+=1
        elif(self.rom[self.PC] == 0x37):
            print("STC")
            self.PC+=1
        elif(self.rom[self.PC] == 0xA0):
            print("ANA B")
            self.PC+=1
        elif(self.rom[self.PC] == 0x1A):
            print("LDAX D")
            self.PC+=1
        elif(self.rom[self.PC] == 0x13):
            print("INX D")
            self.PC+=1
        elif(self.rom[self.PC] == 0x26):
            print("MVI H,", hex(self.rom[self.PC+1]))
            self.H = self.rom[self.PC+1]
            self.PC+=2
        elif(self.rom[self.PC] == 0x29):
            print("DAD H")
            self.PC+=1
        elif(self.rom[self.PC] == 0x7C):
            print("MOV A,H")
            self.A = self.H
            self.PC+=1
        elif(self.rom[self.PC] == 0xD4):
            print("CNC, ", hex(self.rom[self.PC+1]), hex(self.rom[self.PC+2]))
            self.PC+=3
        elif(self.rom[self.PC] == 0xD8):
            print("RC")
            self.PC+=1
        elif(self.rom[self.PC] == 0x24):
            print("INR H")
            self.PC+=1
        elif(self.rom[self.PC] == 0x83):
            print("ADD E")
            self.PC+=1
        elif(self.rom[self.PC] == 0x8A):
            print("ADC D")
            self.PC+=1
        elif(self.rom[self.PC] == 0x57):
            print("MOV D,A")
            self.D = self.A
            self.PC+=1
        elif(self.rom[self.PC] == 0x48):
            print("MOV C,B")
            self.C = self.B
            self.PC+=1
        elif(self.rom[self.PC] == 0x41):
            print("MOV B,C")
            self.B = self.C
            self.PC+=1
        elif(self.rom[self.PC] == 0x08):
            print("UNSUPPORTED NOP")
            self.PC+=1
        elif(self.rom[self.PC] == 0x02):
            print("STAX B")
            self.PC+=1
        elif(self.rom[self.PC] == 0xB6):
            print("ORA M")
            self.PC+=1
        elif(self.rom[self.PC] == 0x09):
            print("DAD B")
            self.PC+=1
        elif(self.rom[self.PC] == 0x2F):
            print("CMA")
            self.PC+=1
        elif(self.rom[self.PC] == 0xA6):
            print("ANA M")
            self.PC+=1
        elif(self.rom[self.PC] == 0x12):
            print("STAX D")
            self.PC+=1
        elif(self.rom[self.PC] == 0xBC):
            print("CMP H")
            self.PC+=1
        elif(self.rom[self.PC] == 0x0C):
            print("INR C")
            self.PC+=1
        elif(self.rom[self.PC] == 0x65):
            print("MOV H,L")
            self.H = self.L
            self.PC+=1
        elif(self.rom[self.PC] == 0x81):
            print("ADD C")
            self.PC+=1
        elif(self.rom[self.PC] == 0x1B):
            print("DCX D")
            self.PC+=1
        elif(self.rom[self.PC] == 0x25):
            print("DCR H")
            self.PC+=1
        elif(self.rom[self.PC] == 0x0A):
            print("LDAX B")
            self.PC+=1
        elif(self.rom[self.PC] == 0x03):
            print("INX B")
            self.PC+=1
        elif(self.rom[self.PC] == 0x8B):
            print("ADC E")
            self.PC+=1
        elif(self.rom[self.PC] == 0x28):
            print("UNSUPPORTED NOP")
            self.PC+=1
        elif(self.rom[self.PC] == 0xA8):
            print("XRA B")
            self.PC+=1
        elif(self.rom[self.PC] == 0x1C):
            print("INR E")
            self.PC+=1
        elif(self.rom[self.PC] == 0x10):
            print("UNSUPPORTED NOP")
            self.PC+=1
        elif(self.rom[self.PC] == 0x0B):
            print("DCX B")
            self.PC+=1
        elif(self.rom[self.PC] == 0xFF):
            print("RST 7")
            self.PC+=1
        elif(self.rom[self.PC] == 0x1F):
            print("RAR")
            self.PC+=1
        else:
            print(hex(self.rom[self.PC]))
            self.PC+=1

def drawHalfOfScreen():
    pass
def drawSecondHalfOfScreen():
    pass

core = Core()

lastInterrupt = time.perf_counter()

drawToEndOfScreen = False
while (core.done is not True):
    core.tick()
    #2 Mhz clock translates to 0.5 * 10^-6 seconds or half a microsecond per cycle
    if((time.perf_counter() - lastInterrupt) > (1/120)):
        if(core.INTE == 1):
            core.INTE == 0
            if(drawToEndOfScreen):
                drawSecondHalfOfScreen()
                core.RST(2)
                drawToEndOfScreen = False
            else:
                drawHalfOfScreen()
                core.RST(1)
                drawToEndOfScreen = True
            lastInterrupt = time.perf_counter()
    #delay enabling interrupts by one instruction to allow interrupt handler to return
    if(core.enableInterrupts):
        core.INTE = 1
        core.enableInterrupts = False
