# Followed this guide: https://stackoverflow.com/questions/45898233/interview-prep-optimizing-swaplexorder

def build_permitted_subs(pairs):
    perm = []

    for a, b in pairs:
        merged = False
        for ind, sub_perm in enumerate(perm):
            if a in sub_perm or b in sub_perm:
                sub_perm.add(a)
                sub_perm.add(b)
                merged = True
                break

        else:
            perm.append(set([a, b]))

        if merged:
            for merge_perm_ind in reversed(range(ind + 1, len(perm))):
                if perm[merge_perm_ind] & sub_perm:
                    sub_perm.update(perm[merge_perm_ind])
                    perm.pop(merge_perm_ind)

    return list(map(sorted, perm))

def solution(swap_str, _pairs):

    pairs = [[a - 1, b - 1] for a, b in _pairs]
    out = list(swap_str)

    perm = build_permitted_subs(pairs)

    for sub_perm in perm:
        sorted_subset = sorted(sub_perm, key=lambda ind: swap_str[ind], reverse=True)

        for sort, targ in zip(sorted_subset, sub_perm):
            out[targ] = swap_str[sort]

    return "".join(out)

print(solution("dznsxamwoj", [[1, 2], [3, 4], [6, 5], [8, 10]]))
print(solution("abdc", [[1, 4], [3, 4]]))
print(solution("acxrabdz",[[1,3], [6,8], [3,8], [2,7]]))