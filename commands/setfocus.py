from evennia.commands.default.muxcommand import MuxCommand
from evennia.contrib.dice import roll_dice

class CmdSetFocus(MuxCommand):

    """
       @SetFocus - Used to set the description of you magical focus.
    
       Usage: 
          @setfocus me/room = description
   
       Sets both your personal messge and the message for the room.
    
    """   

    auto_help = False
   
    key = "@setfocus"
    locks = "cmd:all()"

    def func(self):
        if not self.lhs:
            self.caller.msg("You must suply either 'me' or 'room'.")
            return
        if not self.rhs:
             self.caller.msg("You must suply a description for your focus.")
             return
        Wiz = Character.objects.get(id=1)
        if(self.lhs == "me"):
            self.caller.ndb.mefocus = self.rhs
            self.caller.msg("You set your personal message to %s." % self.rhs)
            Wiz.msg("%s sets his focus message to: %s" % (self.caller, self.rhs))
        if(self.lhs == "room"):
            self.caller.ndb.roomfocus = self.rhs
            self.caller.msg("You set your room message to %s." % self.rhs)
            Wiz.msg("%s sets his focus message to: %s" % (self.caller, self.rhs))
