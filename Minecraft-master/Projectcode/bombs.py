from mcpi.minecraft import Minecraft
from mcpi import block    
from time import sleep
from random import randint

def init(): 
    mc = Minecraft.create("127.0.0.1", 4711)
    x, y, z = mc.player.getPos()  
    return mc

def make_poles(mc,x,y,z):
        m = 41
        for n in range(0,k):
                if n > (k -2):
                        m = 30
                mc.setBlock(x, y,z,m)

def main():
        mc = init()
        x, y, z = mc.player.getPos()  
        count = 0
        while count < 1000:
                x1 = randint(-100,100)
                z1 = randint(-100,100)
                h = randint(3,15)
                make_poles(mc,x1,0,z1,)
                count = count + 1

main()
