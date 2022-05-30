class node():
    def __init__(self, stash=None, crash=None, erase=None):
        self.stash = stash
        self.crash = crash



class main():
    def __init__(self):
        self.a = node(stash=(0, 'b'), crash=(1, 'c'))
        self.b = node(stash=(2, 'c'))
        self.c = node(stash=(4, 'f'), crash=(3, 'd'))
        self.d = node(crash=(6, 'd'), stash=(5, 'e'))
        self.e = node(crash=(7, 'f'), stash=(8, 'b'))
        self.f = node()
        self.current = self.a

    def stash(self):
        if self.current.stash is None:
            raise KeyError
        ans = self.current.stash[0]
        exec(f'self.current = self.{self.current.stash[1]}')
        return ans

    def crash(self):
        if self.current.crash is None:
            raise KeyError
        ans = self.current.crash[0]
        exec(f'self.current = self.{self.current.crash[1]}')
        return ans



o = main()
example = ['stash', 'crash', 'stash']
for i in example:
    exec(f'print(o.{i}())')
