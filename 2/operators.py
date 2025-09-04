from functools import partial
import logging

class Infix(object):
    def __init__(self, func):
        self.func = func

    def __or__(self, other):
        return self.func(other)

    def __ror__(self, other):
        return Infix(partial(self.func, other))

    def __call__(self, v1, v2):
        return self.func(v1, v2)

@Infix
def implies(p, q):
    # p->q = not p or q
    r1 = eval("not p")
    r2 = eval("r1 or q")
    return r2

@Infix
def iff(p, q):
    r1 = eval("p |implies| q")
    r2 = eval("q |implies| p")
    return eval("r1 and r2")

@Infix
def xor(p, q):
    r1 = eval("not p and q")
    r2 = eval("not q and p")
    return eval("r1 or r2")

@Infix
def eq(p, q):
    return eval("p |iff| q")


