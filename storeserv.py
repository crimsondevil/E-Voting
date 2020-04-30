pollFile = open("poll.data", 'r')
bID, ev, eb = pollFile.read().split(',')
pollFile.close()

bvFile = open("ballots.list", 'r')
Bid = bvFile.read()
bvFile.close()

if bID == Bid:
    votesFile = open("votes.data", 'w')
    votesFile.write('%s, %s' % (ev, eb))
    votesFile.close()
