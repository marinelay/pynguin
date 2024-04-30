class A:
    def __init__(self):
        self._x = None

    def set_x1(self):
        self.x = 0

    def set_x2_list(self):
        if isinstance(self.x, str):
            self.x = []

    def set_x2(self) :
        self.x = "0"

    def bar(self) -> int:
        x = self.x + 1
        y = x + 1
        return y

    def baz(self):
        if isinstance(self.x, int):
            return 1
        elif isinstance(self.x, str):
            return "2"
        elif isinstance(self.x, list):
            return 5
        
        return None
    
class B:
    def __init__(self):
        self._x = None

    def set_x1(self):
        self.x = 0

    def set_x2_list(self):
        if isinstance(self.x, str):
            self.x = []

    def set_x2(self) :
        self.x = "0"

    def bar(self) -> int:
        x = self.x + 1
        y = x + 1
        return y

    def baz(self):
        if isinstance(self.x, int):
            return 1
        elif isinstance(self.x, str):
            return "2"
        elif isinstance(self.x, list):
            return 5
        
        return None