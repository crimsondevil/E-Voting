import pickle, sys
from merkletools import MerkleTools


if __name__ == "__main__":
    leaf_index = int(sys.argv[1])
    mt = pickle.load(open('merkle', 'rb'))
    leaf_proof = mt.get_proof(leaf_index)
    leaf = mt.get_leaf(leaf_index)
    print(mt.validate_proof(leaf_proof, leaf, mt.get_merkle_root()))
