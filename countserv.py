import pickle, hashlib, sys
from mymerkle import MerkleTools


def get_hash(n):
    return hashlib.md5(str(n).encode()).digest().hex()

if __name__ == "__main__":
    # candidate = int(sys.argv[1])
    # candidate = get_hash(candidate)

    mt = pickle.load(open('merkle', 'rb'))

    laeves = mt.get_leaf_count()
    vote_map = {}
    for i in range(laeves):
        leaf = mt.get_leaf(i)
        if not vote_map.get(leaf, None):
            vote_map[leaf] = 0
        vote_map[leaf] += 1

    print(vote_map)