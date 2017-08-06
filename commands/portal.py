from evennia.commands.default.muxcommand import MuxCommand
from evennia import DefaultRoom, DefaultExit, DefaultObject
from evennia.utils.create import create_object

class CmdPortal(MuxCommand):
    """
       +Portal - Creates a portal that anyone can pass through.
    
       Usage: 
         +portal    
       Opens a gateway between two locations.
    
    """   
    key = "+portal"
    locks = "cmd:all()"

    def func(self):
        if(sel.caller.ndb.source):
            self.caller.msg("You have opened a portal to %s." % self.caller.ndb.source)
            self.caller.ndb.portA = create_object(DefaultExit, key="portal",aliases=["in", "enter"],location=self.caller.location,destination=self.caller.ndb.source)
            self.caller.ndb.portB = create_object(DefaultExit, key="portal",aliases=["in", "enter"],location=self.caller.ndb.source,destination=self.caller.location)
