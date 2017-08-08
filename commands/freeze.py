from evennia.commands.default.muxcommand import MuxCommand


class CmdFreeze(MuxCommand):
    """
       +Freeze - Freezes time in a location.
    
       Usage: 
         +freeze   
       Stops time in a location.
    
    """   
    key = "+freeze"
    locks = "cmd:all()"
    auto_help=False
    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return
        current_room = self.caller.location
        current_room.db.freeze = 1 
        for item in current_room.contents:
            item.msg("Time comes to a stop.") 
        self.caller.ndb.present = 1
        self.caller.ndb.frozen_room = current_room      
