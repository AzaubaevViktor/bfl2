class Token:
    def __init__(self, line: "Line", pos:int, text:str):
        self.line = line
        self.pos = pos
        self.text = text