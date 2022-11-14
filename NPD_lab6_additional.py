from Bio import Phylo, SeqIO, SeqUtils


def read_tree(file, treetype = "newick"):
    """
    Function to read the tree file
    
    :param file: file with tree
    :param treetype: the type of the tree (default: newick)
    """
    
    tree = Phylo.read(file, treetype)
    return tree

def print_tree(treefile):
    """
    Function to print the tree and get the number of leaves
    
    :param treefile: file with tree
    """
    
    tree = read_tree(treefile)
    # draw the tree
    Phylo.draw_ascii(tree)
    # how many leaves in the tree
    leaves = tree.count_terminals()
    print("Number of leaves: {}".format(leaves))


def read_sequences(file, filetype = "fasta"):
    """
    Function to read a file with sequences
    
    :param file: file with sequences
    :param filetype: the type of the file (default: fasta)
    """
    # ids and sequences of sequences in the file
    sequences = []
    
    for seq_record in SeqIO.parse(file, filetype):
        sequences.append([seq_record.id, seq_record.seq.upper()])
    
    return sequences


def calculate_gc(sequencesfile):
    """
    Function to calculate GC content in a sequence
    
    :param sequencesfile: file with sequences
    """
    
    sequences = read_sequences(sequencesfile)
    
    for i in range(len(sequences)):
        seq_id = sequences[i][0]
        seq_seq = sequences[i][1]
        gc = SeqUtils.GC(seq_seq)
        print("In sequence {} GC content is: {}".format(seq_id, gc))



def main():
    print_tree("./lab6/g.txt")
    print("\n")
    calculate_gc("./lab6/f.fasta")

if __name__ == "__main__":
    main()


