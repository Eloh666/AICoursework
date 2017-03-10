import copy

class UndoRedoStack:
    def __init__(self):
        self.past = []
        self.future = []
        self.present = None

    def undo(self):
        if not self.past or not self.present:
            return
        if self.present:
            self.future.append(self.present)
        self.present = self.past.pop()
        self.reRender()
        return self.present, self.past != [], self.future != []

    def redo(self):
        if not self.future or not self.present:
            return
        if self.present:
            self.past.append(self.present)
        self.present = self.future.pop()
        self.reRender()
        return self.present, self.past != [], self.future != []

    def onChange(self, state):
        if self.present:
            self.past.append(self.present)
        self.present = copy.copy(state)
        self.reRender()
        return self.present, self.past != [], self.future != []

    def clearStack(self):
        self.past = []
        self.future = []
        self.present = None

    def reRender(self):
        if self.present.reRender:
            self.present.reRender()
