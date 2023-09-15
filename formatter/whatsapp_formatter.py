
class FormatCommand:
    def __init__(self, text) -> None:
        self.text = text
    
    def execute(self):
        raise Exception("Pls implement this method.")
    
class BoldCommand(FormatCommand):
    '''TODO Implement'''
    pass

class CursiveCommand(FormatCommand):
    '''TODO Implement'''
    pass

class MonospaceCommand(FormatCommand):
    '''TODO Implement'''
    pass

