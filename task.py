class task:
    def __init__(self,titile,status = "to-do"):
        self.titile = titile
        self.status = status

    def mark_done(self):
        self.status = "done"
