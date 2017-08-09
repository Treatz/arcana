from evennia.commands.default.muxcommand import MuxCommand


class CmdSource(MuxCommand):
    """
       +Source - locks a source location in place.
    
       Usage: 
         +source    
       Sets your current location as your source.
    
    """   
    key = "+source"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1
        current_room = self.caller.location
        self.caller.msg("%s is set as your source location." % self.caller.location.name)
        self.caller.ndb.source = current_room
