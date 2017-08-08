from evennia.commands.default.muxcommand import MuxCommand


class CmdPeek(MuxCommand):
    """
       +Peek - Look at what another character is holding.
    
       Usage: 
         +peek <character>
       Peek at another characters inventory.
    
    """   
    key = "+peek"
    locks = "cmd:all()"

    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        char =  self.caller.search(self.args)
        self.caller.msg("You peek into what %s is carrying: " % char)
        for item in char.contents:
            self.caller.msg(item) 

