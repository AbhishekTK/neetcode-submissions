class TimeMap:

    def __init__(self):
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [[value,timestamp]]
        else:
            self.d[key].append([value,timestamp]) 

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        else:
            l = 0
            r = ""
            for e in self.d[key]:
                if l <=e[1] and e[1]<= timestamp:
                    l = e[1]
                    r = e[0]
            return r
