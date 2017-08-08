from evennia.commands.default.muxcommand import MuxCommand


class CmdEnchant(MuxCommand):

    """
       +enchant - blesses an object with luck.
    
       Usage: 
         +enchant <target>

       Lasts until the luck has all been exhausted.
   
    """   
   
    key = "+enchant"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.args:
            self.caller.msg("You must suply an object for the spell to work.")
            return
        hit =  self.caller.search(self.args)
        if not hit.db.enchant:
            self.caller.msg("%s has become enchanted." % hit)
            hit.db.enchant = 1
        else:
            self.caller.msg("%s has become more powerfu." % hit)
            hit.db.enchant = hit.db.enchant + 1
