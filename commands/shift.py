from evennia.commands.default.muxcommand import MuxCommand


class CmdShift(MuxCommand):

    """
       +Shift - Changes you into an animal.
    
       Usage: 
         +shift <form>

       Changes your appearance but not your stats.
    
    """   
   
    key = "+shift"
    locks = "cmd:all()"

    def func(self):
        if not self.args:
            self.caller.msg("You must suply a form to change to.")
            return
        if self.args == "cat":
            self.caller.ndb.nameSave = self.caller.key
            self.caller.key = "A black cat"
            self.caller.ndb.descSave = self.caller.db.desc
            self.caller.db.desc = "A good kitty."
            self.caller.ndb.imageSave = self.caller.db.image
            self.caller.db.image = "http://www.germantownvet.com/wp-content/uploads/2016/11/Cat-Dandruff-300x223.jpg"
            self.caller.msg("You now appear as %s." % self.caller.key)
            self.caller.db.form = "cat"

        if self.args == "dog":
            self.caller.ndb.nameSave = self.caller.key
            self.caller.key = "A dog"
            self.caller.ndb.descSave = self.caller.db.desc
            self.caller.db.desc = "A good doggy."
            self.caller.ndb.imageSave = self.caller.db.image
            self.caller.db.image = "https://s-media-cache-ak0.pinimg.com/236x/ef/ed/c1/efedc1948b3902ace1a16b2127672cd7--white-photography-sled-dogs.jpg"
            self.caller.msg("You now appear as %s." % self.caller.key)
            self.caller.db.form = "dog"
