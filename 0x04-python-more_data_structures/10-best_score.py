#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary is not None:
        items_ = list(a_dictionary.items())
        scores = sorted([i[-1] for i in items_], reverse=True)
        best_sorted = scores[0]
        for i in items_:
            if i[-1] == best_sorted:
                return i[0]
    else:
        return None
