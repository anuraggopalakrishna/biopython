from Bio import SeqIO
for sequence in SeqIO.parse("ls_orchid.fasta", "fasta"):
    print(sequence.id)
    print(repr(sequence.seq))
    print(len(sequence))