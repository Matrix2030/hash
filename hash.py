import re
import hashlib


class convert_hash:

    def __init__(self):
        print("Welcom to program convert character to the hash rate  :)")

    def converting_hash(self, vorodi):
        self.todelist = []
        self.inp = vorodi
        self.todelist.append(self.inp)
        ls = []
        st_file = ''
        self.character_entekhabi = self.todelist
        try:
            for char in self.character_entekhabi:
                for c in char:
                    res = ord(c)
                    ls.append(res)
                listToStr = ' '.join(map(str, ls))
                tocinver = re.sub('\s', '', listToStr)
                m = hashlib.sha256()
                m.update(tocinver.encode('utf-8'))
                hex = m.hexdigest()
                print("Your hash((  {s} )) = -----".format(s=vorodi), hex, "-----")
        except TypeError:
            print("'ooops'\nYou cannot enter a list as input")
            print("مقدار ورودی صحیح نمیباشد لطفا دوباره تلاش کنید  :(")
