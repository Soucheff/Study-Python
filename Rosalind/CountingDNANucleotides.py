dnaString = open("rosalind_dna.txt").readline()
nt = {
    'A':0,
    'T':0,
    'G':0,
    'C':0,
}
ntTrash = 0 
for s in dnaString:
    if (s not in nt.keys()):
        ntTrash+=1
        continue    
    nt[s]+=1

print("Nucleotides(A C G T): ",nt['A'],nt['C'],nt['G'],nt['T'])
print("Nucleotides Trash: ",ntTrash)