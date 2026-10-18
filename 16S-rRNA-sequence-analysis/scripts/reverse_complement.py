# reverse_complement.py
# Makes the reverse complement of a DNA sequence from a FASTA file

filename = "data/p_aeruginosa_16S.fasta"

sequence = ""

with open(filename) as file:
    for line in file:
        line = line.strip()
        if not line.startswith(">"):
            sequence = sequence + line

sequence = sequence.upper()

complement = {"A": "T", "T": "A", "G": "C", "C": "G"}

reverse_comp = ""
for base in sequence:
    reverse_comp = complement[base] + reverse_comp

print("Original first 30:   ", sequence[:30])
print("Rev. comp. first 30: ", reverse_comp[:30])
print("Same length:", len(sequence) == len(reverse_comp))
double = ""
for base in reverse_comp:
    double = complement[base] + double

print("Round trip works:", double == sequence)