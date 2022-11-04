import random

from Fighter import Fighter

class PC(Fighter):
    pass

class NPC(Fighter):
    pass

def main():
    pc = PC(hp = 20, dmg = 20, heal = 20)
    npc = NPC(hp = 30, dmg = 30, heal = 0)

    while pc.hp > 0 and npc.hp > 0:
        pc_atk = random.randint(0, pc.dmg)
        npc_atk = random.randint(0, npc.dmg)
        pc.hp -= npc_atk
        npc.hp -= pc_atk
        
    print(f"PC: {pc.hp}\tNPC: {npc.hp}")

if __name__ == "__main__":
    main()