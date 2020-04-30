import os, pyaes, sys

def generateBallot(vid):
    bId = os.urandom(16)

    bFile = open("ballots.list", 'w')
    bFile.write('%s' % (str(bId)))
    bFile.close()
#maybe this is reqd
    vbFile = open("voterballots.list", 'w')
    vbFile.write('%s, %s' % (vid, str(bId)))
    vbFile.close()

    return bId

def encVote(vt, bid, vid):
    v, n, d = open("voters.prv", 'r').read().split(',')
    if v == vid:
        vt, d, n = int(vt), int(d), int(n)
        evt = pow(vt, d, n)
        evt = bytes(str(evt).encode())
    #
    # return encB
    #
    # evt = pyaes.AESModeOfOperationCTR(bid).encrypt(vt)
    # ebid = RSAbID(bid, vid)

    encFile = open("poll.data", 'w')
    encFile.write('%s, %s' % (bid, evt))
    encFile.close()

# def RSAbID(bID, vID):
#     v, n, d = open("voters.prv", 'r').read().split(',')
#     if v == vID:
#         p = int.from_bytes(bID, sys.byteorder)
#         d, n = int(d), int(n)
#         encB = pow(p, d, n)
#         encB = bytes(str(encB).encode())
#
#     return encB

if __name__ == '__main__':
    voterID = sys.argv[1]
    vote = sys.argv[2]

    voterFile = open("voters.list", 'r')
    fileVoterID = voterFile.read()
    voterFile.close()

    if fileVoterID == voterID:
        ballotID = generateBallot(voterID)
        encVote(vote, ballotID, voterID)
    else:
        print("Voter not found. Register!")
