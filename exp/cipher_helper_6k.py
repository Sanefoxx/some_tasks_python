class keyword_cipher(object):
    def __init__(self, abc, keyword):
        self.abc = abc
        self.keyword = ''.join(sorted(set(keyword), key=keyword.index))
    def encode(self, str):
        lx = self.abc
        for item in self.keyword:
            lx = lx.replace(item, "")
        lx = self.keyword + lx
        x = ""
        for i, value in enumerate(str):
            for j, value in enumerate(self.abc):
                if self.abc.find(str[i]) == -1:
                    x += str[i]
                    break
                if self.abc[j] == str[i]:
                    x += lx[j]
        return x
    def decode(self, str):
        lx = self.abc
        for item in self.keyword:
            lx = lx.replace(item, "")
        lx = self.keyword + lx
        x_x = ""
        for i, value in enumerate(str):
            for j, value in enumerate(lx):
                if lx.find(str[i]) == -1:
                    x_x += str[i]
                    break
                if lx[j] == str[i]:
                    x_x += self.abc[j]
        return x_x


abc = "abcdefghijklmnopqrstuvwxyz"
key = "keyword"
cipher = keyword_cipher(abc, key)

