class solution:
    def IntToRoman(self,num: int)-> str:
        symList = [["I",1]],[["II",2]],[["III",3]],[["IV",4]],[["V",5]],[["VII",6]],[["VII",7]]
        res+""
        for sym, val in reversed(symList):
            if num // val:
                count = num // val
                res +=(sym* count)
                num = num % val
                return res