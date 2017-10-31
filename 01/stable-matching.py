#!/usr/bin/env python

from typing import List, Tuple


''' The propose_and_reject-function implements a version of the Stable
    Matching-algorithm by Gale and Shapely. It works on a group of women and
    one of men (each instances of Person) where each one have preferences 
    for the other group. This algorithm tries to create a good list of pairs.'''


class Person():
    '''A person is one of a women or a men where the gender just represents two
       groups. Each Person has a name and a preference_list of Person of the
       other gender and has no partner in the beginning (is free). The
       propose_list will be filled later and contains each person to whom this
       person hasn't proposed yet.'''

    def __init__(self, name: str, preference_list: List['Person'] = []):
        self.name: str = name
        self.preference_list: List['Person'] = preference_list
        self.free: bool = True
        self.propose_list: List['Person'] = []

    def __repr__(self):
        return self.name

Pair = Tuple[Person, Person]


def propose_and_reject(men: List[Person], women: List[Person]) -> List[Pair]:
    '''This function tries to create good pairs based on Gale and Shapley's
       Stable Matching algorithm from the two given groups of the same size.'''

    assert (len(men) == len(women)), 'We need an equal amount of women and men'

    for p in men + women:
        p.free = True
    for p in men:
        p.propose_list = women

    pairs: List[Pair] = []

    while True:
        ms: List[Person] = [m for m in men if m.free and m.propose_list]
        if not ms:
            break

        m: Person = ms[0]
        w: Person = [w for w in m.preference_list if w in m.propose_list][0]

        if w.free:
            pairs.append((m, w))
            m.free = False
            w.free = False
        else:
            m_old: Person = [mx for (mx, wx) in pairs if wx == w][0]
            m_old_index: int = w.preference_list.index(m_old)
            m_index: int = w.preference_list.index(m)
            if m_index > m_old_index:
                pairs.remove((m_old, w))
                pairs.append((m, w))
                m.free = False
                m_old.free = True

        m.propose_list.remove(w)

    return pairs


if __name__ == '__main__':
    x: Person = Person('X')
    y: Person = Person('Y')
    z: Person = Person('Z')

    a: Person = Person('A', [y, x, z])
    b: Person = Person('B', [x, y, z])
    c: Person = Person('C', [x, y, z])

    x.preference_list = [a, b, c]
    y.preference_list = [b, a, c]
    z.preference_list = [a, b, c]

    pairs: List[Pair] = propose_and_reject([x, y, z], [a, b, c])
    print(pairs)
