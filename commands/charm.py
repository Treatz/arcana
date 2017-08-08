from evennia.commands.default.muxcommand import MuxCommand


class CmdCharm(MuxCommand):

    """
       +charm - blesses an object with luck.
    
       Usage: 
         +charm <target>

       Lasts until the luck has all been exhausted.
   
    """   
   
    key = "+charm"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        if not self.args:
            self.caller.msg("You must suply an object for the spell to work.")
            return
        hit =  self.caller.search(self.args)
        if(hit.db.charm == 0):
            self.caller.msg("%s has become a lucky charm." % hit)
            hit.db.charm = hit.db.charm + 1
        else:
            self.caller.msg("%s has become more powerfu." % hit)
            hit.db.charm = hit.db.charm + 1
