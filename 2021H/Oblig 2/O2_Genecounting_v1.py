def genomecount(genome):

    genome_length = len(genome)
    genome_beginning = 0
    genome_end = 0
    gene_string = []

    for i in range(genome_end, genome_length):
        if (genome[i] == "A") and (genome[i + 1] == "T") and (genome[i + 2] == "G"):
            genome_beginning = i + 3
            for z in range(genome_beginning, genome_length):
                if not ("ATG" or "TAG" or "TAA" or "TGA") in genome[genome_beginning, genome_end]:
                    # genome_end = genome_length
                    break
                if (genome[z] == "A" and genome[z + 1] == "T" and genome[z + 2]) == "G":
                    genome_end = z
                    break
                elif (genome[z] == "T" and genome[z + 1] == "A" and genome[z + 2]) == "G":
                    genome_end = z
                    break
                elif (genome[z] == "T" and genome[z + 1] == "A" and genome[z + 2]) == "A":
                    genome_end = z
                    break
                elif (genome[z] == "T" and genome[z + 1] == "G" and genome[z + 2]) == "A":
                    genome_end = z
                    break

            if len(genome[genome_beginning:genome_end]) % 3 == 0:
                gene_string.append(genome[genome_beginning:genome_end])

    for elem in gene_string:
        print(elem)


def main():
    genomecount(input("Enter a genome string: "))


if __name__ == "__main__":
    main()
