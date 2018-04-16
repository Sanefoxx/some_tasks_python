class Cipher(object):
    def __init__(self, map1, map2):
        self.map1 = map1
        self.map2 = map2
        pass

    def encode(self, string):
        x = ""
        for i, value in enumerate(string):
            for j, value in enumerate(self.map1):
                if self.map1.find(string[i]) == -1:
                    x += string[i]
                    break
                if self.map1[j] == string[i]:
                    x += self.map2[j]
        return x

    def decode(self, string):
        x_x = ""
        for i, value in enumerate(string):
            for j, value in enumerate(self.map2):
                if self.map2.find(string[i]) == -1:
                    x_x += string[i]
                    break
                if self.map2[j] == string[i]:
                    x_x += self.map1[j]
        return x_x