pollFile = open("poll.data", 'r')
bID, ev= pollFile.read().split(',')
pollFile.close()

bvtFile = open("ballots.list", 'r')
Bid = bvtFile.read()
bvtFile.close()

def decrypt(m, e, n):
    # print (m,e,n)
    print (pow(int(m), int(e), int(n)))

if bID == Bid:
    # voter_ballot = open("voterballots.list", "r")
    # vid, ballot_id = voter_ballot.read().split(',')
    vid, n, e = open('voters.pub', 'r').read().split(',')
    decrypt(eb[3:-1], e, n)
    # votesFile = open("votes.data", 'w')
    # votesFile.write('%s, %s' % (ev, eb))
    # votesFile.close()
