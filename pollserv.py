import os, json, sys
from helpers import update_file

def generateBallot(voter_id):
    ballotID = os.urandom(16).hex()

    def transform(ballot_map):
        if voter_id in ballot_map.values():
            raise Exception("You have already registered a vote. You cannot vote again.")
        else:
            ballot_map[ballotID] = voter_id
            print ("A unique ballot has been created for voter ID:", voter_id)
        return ballot_map

    status = update_file('data/ballot.json', transform)

    return ballotID if status else None


def encVote(vote, ballot_id, voter_id, voter_data):
    n, d = voter_data['prv'].split(',')
    vote, d, n = int(vote), int(d), int(n)
    enc_vote = pow(vote, d, n)

    def transform(polls_map):
        polls_map[ballot_id] = str(enc_vote)
        return polls_map
    update_file('data/polls.json', transform)
    print ("Your vote has been casted successfully. Thank you!")

if __name__ == '__main__':
    voterID = sys.argv[1]
    vote = sys.argv[2]

    with open('data/voters.json', 'r') as voter_file:
        voter_map = json.load(voter_file)

        if voter_map.get(voterID, None):
            ballotID = generateBallot(voterID)
            voter_data = voter_map[voterID]
            if ballotID:
                encVote(vote, ballotID, voterID, voter_data)
        else:
            print("Voter not found. Register!")
