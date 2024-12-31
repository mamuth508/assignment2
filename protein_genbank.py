from Bio import SeqIO

hemseq_file_path = "/home/gulerm/protein_seq/hemoglobinalpha.fasta"
hem_seq_handle = SeqIO.parse(hemseq_file_path, "fasta")

for seq_record in hem_seq_handle:
    ID_hem = seq_record.id
    Seq_hem = str(seq_record.seq)
    Len_hem = len(seq_record)
    Des_hem = seq_record.description

    print("ID:", ID)
    print("Sequence:", Seq_hem)
    print("Length:", Len_hem )
    print("Description:",Des_hem)
insseq_file_path = "/home/gulerm/protein_seq/insulin.fasta"
ins_seq_handle = SeqIO.parse(insseq_file_path, "fasta")

for seq_record in ins_seq_handle:
    ID_ins = seq_record.id
    Seq_ins = str(seq_record.seq)
    Len_ins = len(seq_record)
    Des_ins = seq_record.description

    print("ID:", ID_ins)
    print("Sequence:", Seq_ins)
    print("Length:", Len_ins)
    print("Description:", Des_ins)
p53seq_file_path = "/home/gulerm/protein_seq/p53.fasta"
p53_seq_handle = SeqIO.parse(p53seq_file_path, "fasta")

for seq_record in p53_seq_handle:
    ID_p53 = seq_record.id
    Seq_p53 = str(seq_record.seq)
    Len_p53 = len(seq_record)
    Des_p53 = seq_record.description

    print("ID:", ID_p53)
    print("Sequence:",  Seq_p53)
    print("Length:", Len_p53)
    print("Description:", Des_p53)   
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Seq import IUPAC
from Bio import SeqIO

hemoglobin = SeqRecord(Seq(Seq_hem), id = (ID_hem), 
             description = (des_hem) )
insulin = SeqRecord(Seq(Seq_ins), id = (ID_ins),
              description = (Des_ins))
p53 = SeqRecord(Seq(Seq_p53), id = (ID_p53),
              description = (Des_p53))
my_proteins = [hemoglobin, insulin, p53]
seq_file_path = "/home/gulerm/protein_seq/my_proteins.faa"
SeqIO.write(my_proteins, "my_proteins.faa", "fasta")
records = SeqIO.parse(seq_file_path, "fasta", alphabet= IUPAC.ambiguous_dna)
count = SeqIO.write(records, "my_proteins.genbank", "genbank")
print("Converted %i records" % count)

