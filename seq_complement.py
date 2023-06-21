import Bio
from Bio.Seq import Seq 
print(Bio.__version__)
my_seq = Seq('ATGGGTCACAGCA')
print(my_seq)
my_comp = my_seq.complement()
print(my_comp)