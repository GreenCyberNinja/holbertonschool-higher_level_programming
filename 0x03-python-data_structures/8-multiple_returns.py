#!/usr/bin/python3
def multiple_returns(sentence):
    ans = [len(sentence), None]
    if sentence:
        ans[1] = sentence[0]
    return tuple(ans)
