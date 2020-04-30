pollFile = open("poll.data", 'r')
bID, ev= pollFile.read().split(',')
pollFile.close()

bvtFile = open("ballots.list", 'r')
Bid = bvtFile.read()
bvtFile.close()

if bID == Bid:
    votesFile = open("votes.data", 'w')
    votesFile.write('%s, %s' % (bID, ev))
    votesFile.close()
