import Bio
from Bio.Seq import Seq
coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print(coding_dna)
template_dna = coding_dna.reverse_complement()
print(template_dna)
messenger_rna = coding_dna.transcribe()
print(template_dna)
#to get dna from rna 
messenger_rna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
print(messenger_rna)
print('converting this rna to dna ')
dna=messenger_rna.back_transcribe()
print(dna)