dna_map = {
    "A" : "T",
    "T" : "A",
    "C" : "G",
    "G" : "C"
}
def DNA_strand(dna:str):
    return "".join([dna_map.get(char) for char in dna])

print(DNA_strand("AAAA"))