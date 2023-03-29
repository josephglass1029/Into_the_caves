class Money:
    def __init__(self, pp=0, gp=0, sp=0, ep=0, cp=0):
        self.pp = pp
        self.gp = gp
        self.sp = sp
        self.ep = ep
        self.cp = cp
        
    def add_money(self, pp=0, gp=0, sp=0, ep=0, cp=0):
        self.pp += pp
        self.gp += gp
        self.sp += sp
        self.ep += ep
        self.cp += cp
    
    def current_money(self):
        print(f"You now have {self.pp} PP, {self.gp} GP, {self.ep} EP, {self.sp} SP, {self.cp} CP")