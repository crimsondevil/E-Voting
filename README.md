# Secure E-Voting System

Secure E-Voting System is a python based project. It handles the security of data during the registration of the voters while polling on election day, and counting and auditing of the votes to ensure an unbiased voting environment. It also ensures that the voter is a registered and unique voter who is eligible to vote and its ballot for voting is personalized and secured.

The encryption schemes used are:-

    RSA Encryption 
    Merkle Tree Hashing
  
The key management is done using:-

    SHAKE_256 hash algorithm
    SHA-256 hash algorithm
    Private key and Public key using GCD and Modular Inverse
    Random key generator.  
    
The packages used are datetime, hashlib, helpers, json, mymerkle, os, pickle, random, and sys. The modules used are argv[], dumps(), encode(), hexdigest(), MerkleTools(), now(), pow(), randrange(), sha256(), shake_256(), and urandom().

# regserv.py
This file is the start of the system. In this, it takes 3 arguments from the command line; the name, the year of birth, and the SSN number of the voter. Using the year, it checks if the voter is eligible to vote or not. The default age assumed is 21 years. An SSN is used to verify that an individual is uniquely identified. If a voter accidentally tries to re-register, he is assigned his previously generated voter ID along with new public and private keys. Once this verification is complete, a new 10-digit voter ID is generated using the SHAKE_256 on the SSN. Along with this, a hashed data of all the data provided is also created. A unique public and private key is also generated for future purposes of encryption of votes. All these data for each voter is mapped in a JSON file called data/voters.json. Every new voter data appends the existing data in it.

input 1:

    py regserv.py alice 1988 23047

output 1:

    You are registered. Your voter ID is: 1af6e92d0d. Do not disclose it to any unknown sources and third-parties.

input 2:

    py regserv.py eva 2005 91475

output 2:

    Underage! You are not eligible to vote.

# pollserv.py
The polling process happens in this file. The voter enters the voter ID and the vote for his candidate by mentioning his candidate ID in the beginning in the command line. The voter ID is then used to verify if the voter is registered or not, by tallying it against voters.json file. If he is registered, then a unique ballot and ballot ID is generated for the voter to store the casted vote. The ballot ID along with its corresponding voter ID is stored in data/ballot.json file once the voting has been completed. After this, the vote is encrypted using the voter's private key for which data is loaded from voters.json . It is encrypted using the RSA Encryption Algorithm. The ballot ID and the encrypted vote is mapped in a data/polls.json file.

input 1:

    py pollserv.py 1af6e92d0d 10

output 1:

    A unique ballot has been created for voter ID: 1af6e92d0d
    Your vote has been casted successfully. Thank you!

input 2:

    py pollserv.py ff7tb78y9p 5

output 2:

    Voter not found. Register!

input 3:

    py pollserv.py 1af6e92d0d 10

output 3:

    You have already registered a vote. You cannot vote again.

# storeserv.py
It reads data from all the files used for mapping and storing generated data. It uses the ballot.json to verify the ballot ID against the ballot ID present in polls.json file. It is also used to figure out the corresponding voter ID to any given ballot ID. Using the voter ID, we access the voter's public key to decrypt the encrypted vote. The vote comprises of a candidate ID. The sequence of candidate IDs is shown as a result. The sequence follows the same structure as the votes were stored. This sequence of candidate IDs is then hashed using SHA-256 and used as a leaf node to form a merkle tree. This tree is then dumped using pickle, in a file called Merkle.

input:

    py storeserv.py

output:

    The sequence of votes stored:-
    ['5', '5', '6', '10', '10', '11', '10']

# countserv.py
This file reads data from the Merkle file and counts the total votes for each candidate by using a counter for each of them while reading it from the Merkle file. The file initially reads from the pickled 'merkle' file which consists of the MerkleTools object. This object has the whole merkle tree in an immutable, binary form to read and process the leaves. The leaves of the Merkle Tree consists of the individual vote received for the candidate. The merkle tree helps in protecting the vote data from any kind of tampering and preserves the state of the voting sequence.

input:

    py countserv.py

output:

    The count of votes for each candidate:-
    {'ef2d127de37b942baad06145e54b0c619a1f22327b2ebbcfbec78f5564afe39d': 2, 'e7f6c011776e8db7cd330b54174fd76f7d0216b612387a5ffcfb81e6f0919683': 1, '4a44dc15364204a80fe80e9039455cc1608281820fe2b24f1e5233ade6af1dd5': 3, '4fc82b26aecb47d2868c4efbe3581732a3e7cbcc6c2efb32062c08170a05eeb8': 1}
    The candidate ID has been hidden for security reasons.

# auditserv.py
This file is used to verify the state of the merkle tree which is pickled from the 'Merkle' file. In this, a new candidate is taken from the argument in the command line. It is then checked against the Merkle file to check if it is a valid leaf node or sister node. If not, it will have a different root than the actual root. This way we can verify if the votes have ever been tampered at any time. Validating the proof of the target node provided in the argument makes the audit a success. If the node exists as leaf, then the tree is valid. Whereas it gives a false response on reading the tampered tree thereby verifying the voting sequence.

input 1:

    py auditserv.py 6

output 1:
    
    True, candidate ID: 6 exists.

input 2:

    py auditserv.py 16

output 2:

    Candidate ID: 15 doesn't exist.

# helper.py
This file is mainly used for all the read and write data to and from a JSON file. It takes the name of the file, the data, and the type it is to be accessed. Then it dumps for writing and loads for reading a data from the .json file. It also checks if any duplicate voter is there and if someone is trying to tamper the votes, by always checking for a duplicity in the write data before appending the file.

# To view the JSON files of stored data from the system:-

The list of voter IDs, their hashed data, and the public and private keys for each one of them.

    type voters.json

The list of ballots formed for every registered voter who has casted a vote.

    type ballot.json

The RSA encrypted vote from every ballot used for voting.

    type polls.json
