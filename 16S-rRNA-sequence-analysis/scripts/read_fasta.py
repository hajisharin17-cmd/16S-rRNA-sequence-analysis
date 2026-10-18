# read_fasta.py
# Reads a FASTA file and reports basic information

filename = "data/p_aeruginosa_16S.fasta"

header = ""
sequence = ""

with open(filename) as file:
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            header = line
        else:
            sequence = sequence + line

print("Header:", header)
print("Sequence length:", len(sequence))
print("First 60 letters:", sequence[:60])