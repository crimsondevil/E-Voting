import pickle, sys, hashlib
from mymerkle import MerkleTools


def get_hash(n):
    return hashlib.md5(n.encode()).digest().hex()


if __name__ == "__main__":
    leaf_value = sys.argv[1]
    leaf_value = get_hash(leaf_value)

    mt = pickle.load(open('merkle', 'rb'))
    laeves = mt.get_leaf_count()
    votes = []
    for i in range(laeves):
        votes.append(mt.get_leaf(i))

    try:
        index = votes.index(leaf_value)
        leaf_proof = mt.get_proof(index)
        leaf = mt.get_leaf(index)
        print("Is Valid?", mt.validate_proof(leaf_proof, leaf, mt.get_merkle_root()))
    except:
        print ("Provided leaf doesn't exists")
