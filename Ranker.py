import itertools as itr


def main():
    pairs = list()
    file = open("data.txt", "r")
    docs = file.read().splitlines()
    file.close()
    pairs = list()
    ranked = {}
    vocab = list()
    for i in range(0, len(docs)):
        d = docs[i].split()
        pairs.append(list(itr.combinations(d, 2)))
    for pair in pairs:
        for j in range(0, len(pair)):
            element = pair[j]
            if element not in ranked:
                ranked[element] = 0
            else:
                ranked[element] = ranked[element] + 1
    print("The top ten ranked pairs: ")
    count = 1
    for k in sorted(ranked, key=ranked.get, reverse = True):
            print(count, end = ". ")
            print(k, end=" ")
            print(ranked[k])
            count += 1
            if (count == 11):
                break
    return 0

main()



