# analyze_sequence.py
# Basic analysis of a DNA sequence from a FASTA file

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

sequence = sequence.upper()

count_a = sequence.count("A")
count_t = sequence.count("T")
count_g = sequence.count("G")
count_c = sequence.count("C")

other = len(sequence) - (count_a + count_t + count_g + count_c)

gc_content = (count_g + count_c) / len(sequence) * 100

print("Header:", header)
print("Length:", len(sequence))
print("A:", count_a, " T:", count_t, " G:", count_g, " C:", count_c)
print("Other letters:", other)
print("GC content: " + str(round(gc_content, 2)) + "%")