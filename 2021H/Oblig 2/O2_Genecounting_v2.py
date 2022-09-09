def check_if_gene(genome_string):
    genome_beginning = 0
    genome_length = len(genome_string)

    if ("ATG") in genome_string:
        for i in range(0, len(genome_string)):
            if (genome_string[i] == "A") and (genome_string[i + 1] == "T") and (genome_string[i + 2] == "G"):
                genome_beginning = i + 3
                if "TAG" or "TAA" or "TGA" in genome_string[genome_beginning:genome_length]:
                    return True, genome_beginning

    else:
        return False


def seperate_gene_string(genome_string, genome_beginning):

    print("Found gene")


def main():  # input
    genome = input("Enter a genome string: ")
    geneinfo = check_if_gene(genome)
    if geneinfo[0]:
        seperate_gene_string(genome, geneinfo[1])
    else:
        print("no gene is found")


if __name__ == "__main__":
    main()
