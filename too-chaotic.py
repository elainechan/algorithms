def minimumBribes(q):
    bribes = 0
    for i in q:
        if q.index(i) < i - 3:
            return 'Too chaotic'
        elif q.index(i) < q.index(i) - 1:
            bribes += q.index(i) - (q.index(i)-1)
    return bribes
