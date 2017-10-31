#!/usr/bin/env python

from operator import attrgetter
from typing import List, NamedTuple


class Interval(NamedTuple):
    'An interval is a product of a start and a finish-time.'
    start: int
    finish: int


def schedule(intervals: List[Interval]) -> List[Interval]:
    'Returns the greates subset of non-overlapping intervals.'

    i: List[Interval] = sorted(intervals, key=attrgetter('finish'))
    o: List[Interval] = []

    while i:
        sel: Interval = i[0]

        o.append(sel)
        for tmp in list(i):
            if sel.start <= tmp.start <= sel.finish or tmp.start <= sel.start <= tmp.finish:
                i.remove(tmp)

    return o


if __name__ == '__main__':
    intervals: List[Interval] = [
      Interval(2, 4), Interval(1, 5), Interval(3, 3), Interval(4, 6)]

    print(schedule(intervals))
