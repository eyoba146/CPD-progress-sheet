class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        t_pos=0
        for np in range(len(name)):
            for scan in range(t_pos, len(typed)+1):
                if scan==len(typed): return False
                if name[np] == typed[t_pos]:
                    t_pos+=1
                    break
                else:
                    for tp in range(t_pos, len(typed)):
                        if(np==0): return False
                        if name[np-1] != typed[tp]: break
                    if tp==t_pos: return False
                    t_pos=tp

        
        for pos in range(t_pos, len(typed)):
            if typed[pos] != name[-1]:
                return False
        return len(typed)>=len(name) and name[-1]==typed[-1]
