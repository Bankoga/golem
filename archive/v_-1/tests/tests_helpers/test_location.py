class Location:
    def __init__(self, loc, parent_location=None):
        # print(parent_location)
        # print(loc)
        # path is used for diving into the container objects
        self.path = [loc] if parent_location is None else parent_location.extend(loc)
        # print(self.path)
        # key is used for bucket sorting
        self.key = ':'.join(str(e) for e in self.path)
    
    def extend(self, key):
        return self.path + [key]