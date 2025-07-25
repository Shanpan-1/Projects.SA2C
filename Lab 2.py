Set1 =  ["Document1", "Document2", "Document3"]
class UndoRedoStack:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []
# This functionn adds an action to the undo stack and clars the redo stack.
    def do_action(self, action):
        self.undo_stack.append(action)
        self.redo_stack.clear()
        print(f"{action} has been performed")
# This funtion pop an element of the undo stach and adds it to the redo stack
    def undo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            self.redo_stack.append(action)
            print(f"Undo action: {action}")
        else:
            print("There is nothing to undo")
# This funtion pop an element of the redo stach and adds it to the undo stack
    def redo(self):
        if self.redo_stack:
            action = self.redo_stack.pop()
            self.undo_stack.append(action)
            print(f"Redo action: {action}")
        else:
            print("There is nothing to redo")
    def clear(self):
        self.undo_stack.clear()
        self.redo_stack.clear()
        print("Undo and Redo stacks cleared")

print("This was the first set created:", Set1)

a = UndoRedoStack()
a.do_action("type apple")
a.do_action("type pear")
a.undo()
a.redo()

Set1.append("Documetation")     # Added the word 'Documentstation' to the set


Set1.undo()

Set1.redo()

Set1.append("Superficial documents")# Added Superfical Documents to the set

Set1.undo()

Set1.redo()

Set1.append("Important_info2")     # Added the word 'Important_info2' to the set


Set1.clear()

print("Final Set1:", Set1)

'''
Should I add 
a.do_action(list(Set1))   Create a new object after the change 
as I have no idea what else to do
'''
