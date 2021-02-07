import json, pickle
from mymerkle import MerkleTools


if __name__ == '__main__':
    polls_map = json.load(open('data/polls.json'))
    ballot_map = json.load(open('data/ballot.json'))
    voter_map = json.load(open('data/voters.json'))

    votes = []
    for ballot, enc_vote in polls_map.items():
        public_key = voter_map[ballot_map[ballot]]["pub"]
        n, e = public_key.split(',')
        enc_vote, n, e = int(enc_vote), int(n), int(e)

        votes.append(str(pow(enc_vote, e, n)))

    print ("The sequence of votes stored:-")
    print (votes)
    if votes:
        mt = MerkleTools(hash_type="sha256")
        mt.add_leaf(votes, True)
        mt.make_tree()

        with open('merkle','wb') as m_file:
            pickle.dump(mt, m_file)
