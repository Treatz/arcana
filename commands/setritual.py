from evennia.commands.default.muxcommand import MuxCommand
from typeclasses.characters import Character
from evennia.contrib.dice import roll_dice

class CmdSetRitual(MuxCommand):

    """
       @SetRitual - Used to set the description of the ritual.
    
       Usage: 
          @setritual me/room = description
   
       Sets either your personal messge and the message for the room.
    
    """   

    auto_help = False
   
    key = "@setritual"
    locks = "cmd:all()"

    def func(self):
        if not self.lhs:
            self.caller.msg("You must suply either 'me' or 'room'.")
            return
        if not self.rhs:
             self.caller.msg("You must suply descriptions for your ritual.")
             return
        Wiz = Character.objects.get(id=1)
        if(self.lhs == "me"):
            self.caller.db.meritual = self.rhs
            self.caller.msg("You set your personal ritual message to %s." % self.rhs)
            Wiz.msg("%s sets his personal ritual to: %s" % (self.caller, self.rhs))
        if(self.lhs == "room"):
            self.caller.db.roomritual = self.rhs
            self.caller.msg("You set your room ritual message to %s." % self.rhs)
            Wiz.msg("%s sets his ritual room message to: %s" % (self.caller, self.rhs))
