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
    auto_help=False
    def func(self):
        if not self.caller.db.magic:
            self.caller.msg("You can't use magic!")
            return

        from evennia.contrib.dice import roll_dice

        if not self.caller.db.correspondence:
            self.caller.msg("This spell requires knowledge of the correspondence sphere.")
            return
        wins = 0
        for x in range(0, self.caller.db.arete):
            roll = roll_dice(1,10)
            if(roll > 5):
                wins += 1
        wins = wins + self.caller.db.correspondence
        if wins < 7:
            self.caller.msg("Your spell fizzles out and fails.")
            return

        if not self.caller.db.quintessence:
            self.caller.msg("You don't have enough quintessence for that!")
            return
        else:
            self.caller.db.quintessence -= 1
        if(sel.caller.ndb.source):
            self.caller.msg("You have opened a portal to %s." % self.caller.ndb.source)
            self.caller.ndb.portA = create_object(DefaultExit, key="portal",aliases=["in", "enter"],location=self.caller.location,destination=self.caller.ndb.source)
            self.caller.ndb.portB = create_object(DefaultExit, key="portal",aliases=["in", "enter"],location=self.caller.ndb.source,destination=self.caller.location)
