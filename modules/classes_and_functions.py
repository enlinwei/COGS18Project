import string

def remove_blanks(input_str):
    """Removes blanks and newline characters in input_str and returns
    a string with those removed.
    
    Parameters
    ----------
    input_str : string
        String from which blanks and newline characters are to be removed.
    
    Returns
    ----------
    temp_str : string
        String which has blanks and newline characters removed.	
    """
    
    temp_str = input_str.replace(' ', '')
    temp_str = temp_str.replace('\n', '')
    return temp_str


class RNA_pol():
    """Transcribes a DNA sequence into its corresponding RNA sequence."""
    
    # Class purpose
    purpose = 'transcribe DNA to RNA'
    
    def is_DNA(input_DNA):
        """Checks if input string is a DNA sequence.
        
        Parameters
        ----------
        input_DNA : string
            DNA sequence to be checked to see if it is a DNA sequence.
        
        Returns
        ----------
        condition : boolean
            Whether input is a DNA sequence.
        
        Notes
        ----------
        Note: A DNA sequence only contains upper- or lowercase
        A, T, G, C characters.
        """
        
        # Uses remove_blanks() method to remove any blanks and newline characters
        #  in the input_DNA string
        DNA = remove_blanks(input_DNA)
        
        condition = True
        DNA_bases = 'AGTCagtc'
        
        # If one character in the input string DNA is not found in DNA_bases,
        #   will set condition to False and return an Exception telling the user
        #   that the input sequence is not a DNA sequence.
        for base in DNA:
            if base not in DNA_bases:
                condition = False
                raise Exception("Not a DNA sequence! Please enter again!")
                break
            else:
                continue
        
        return condition
    
    def DNA_to_caps(DNA):
        """Turns the input DNA sequence into all caps.
        
        Parameters
        ----------
        DNA : string
            DNA sequence to be turned into all caps.
        
        Returns
        ----------
        DNA.upper(): string
            The DNA sequence converted to all caps.
        
        Notes
        -----
        Note: turning the DNA sequence into all caps makes it easier to work
        with later, as we won't have to deal with lowercase characters.
        """
        
        # First uses is_DNA() method to check if input sequence is DNA;
        #  this prevents proceeding on to use other methods (and wasting time
        #  & resources) when the input sequence is not a DNA sequence.
        if RNA_pol.is_DNA(DNA):
            return DNA.upper()
    
    def transcribe(DNA):
        """Transcribes DNA sequence into RNA sequence.
        
        Parameters
        ----------
        DNA : string
            DNA sequence to be transcribed.
        
        Returns
        ----------
        RNA : string
            RNA sequence produced from transcribing DNA sequence.        
        """
        
        # First uses DNA_to_caps() method to turn DNA string into all caps
        #  so it's easier to work with.
        DNA = RNA_pol.DNA_to_caps(DNA)
        RNA = ''
        
        # Since DNA and RNA share the same bases except for T in DNA
        #  (which is U in RNA), this loop will replace all instances
        #  of T in DNA with U.
        for base in DNA:
            if base == 'T':
                RNA = RNA + 'U'
            else:
                RNA = RNA + base
        
        return RNA


class Ribosome():
    """Does the job of translation, turning an RNA sequence into its
    corresponding protein."""
    
    # Class purpose
    purpose = 'translate RNA to protein'
    
    def is_RNA(input_RNA):
        """Checks if input string is an RNA sequence.
        
        Parameters
        ----------
        RNA : string
            RNA sequence to be checked to see if it is a RNA sequence.
        
        Returns
        ----------
        condition : boolean
            Whether input is a RNA sequence.
        
        Notes
        ----------
        Note: An RNA sequence only contains upper- or lowercase
        A, U, G, C characters.
        """
        
        # Uses remove_blanks() method to remove any blanks and newline characters
        #  in the input_RNA string
        RNA = remove_blanks(input_RNA)
        
        condition = True
        RNA_bases = 'AGUCaguc'
        
        # If one character in the input string RNA is not found in RNA_bases,
        #  will set condition to False and raise an Exception telling the user
        #  that the input sequence is not a RNA sequence.
        for base in RNA:
            if base not in RNA_bases:
                condition = False
                raise Exception("Not an RNA sequence! Please enter again!")
                break
            else:
                continue
        
        return condition
    
    def RNA_to_caps(RNA):
        """Turns the input RNA sequence into all caps.
        
        Parameters
        ----------
        RNA : string
            RNA sequence to be turned into all caps.
        
        Returns
        ----------
        RNA.upper() : string
            The RNA sequence converted to all caps.
            
        Notes
        ----------
        Note: turning the RNA sequence into all caps makes it easier to work
        with later, as we won't have to deal with lowercase characters.
        """
        
        # First uses is_RNA() method to check if input sequence is RNA;
        #  this prevents proceeding on to use other methods (and wasting time
        #  & resources) when the input sequence is not an RNA sequence.
        if Ribosome.is_RNA(RNA):
            return RNA.upper()
        
        return RNA.upper()
    
    def find_start_codon(RNA):
        """Finds the position of the start codon.
        
        Parameters
        ----------
        RNA : string
            RNA sequence in which the position of the start codon is to be found.
        
        Returns
        ----------
        RNA.find('AUG') : int
            Position of the 'A' of 'AUG' in the string of RNA sequence.
            
        Notes
        ----------
        Note: The start codon is the first 'AUG' in the RNA sequence.
        """
        
        # First uses RNA_to_caps() method to capitalize all chars in the RNA
        #  sequence so it's easier to work with.
        RNA = Ribosome.RNA_to_caps(RNA)
        
        # If RNA sequence does not contain 'AUG', will raise an Exception
        #  telling the user that a start codon was not found.
        if 'AUG' in RNA:
            return RNA.find('AUG')
        else:
            raise Exception("Start codon not found!")
    
    def translate(RNA_seq):
        """Translates an input RNA sequence to the corresponding protein.
        
        Parameters
        ----------
        RNA : string
            RNA sequence to be translated into the corresponding protein.
        
        Returns
        ----------
        protein: string
            The corresponding translated protein (a string of amino acid symbols).
            
        Notes
        ----------
        Note: A protein is a string of amino acid sequences.
        """
        
        RNA = remove_blanks(RNA_seq)
        
        # Uses find_start_codon() method to find codon from which
        #  translation will start
        counter = Ribosome.find_start_codon(RNA)
        codon = ''
        protein = ''
        
        # Assigns triplets of RNA sequence chars to 'codon' and concatenates the
        #  corresponding amino acid symbol to the growing chain of amino acids,
        #  then moves on to the next triplet, until reaching stop codon.
        while counter <= (len(RNA) - 3):
            codon = RNA[counter] + RNA[counter+1] + RNA[counter+2]
            
            #Start codon & Methionine(M)
            if codon == 'AUG':
                protein = protein + 'M'
            #Phenylalanine(F)
            elif codon == 'UUU' or codon == 'UUC':
                protein = protein + 'F'
            #Leucine(L)
            elif codon == 'UUA' or codon == 'UUG' or codon == 'CUU' \
            or codon == 'CUC' or codon == 'CUA' or codon == 'CUG':
                protein = protein + 'L'
            #Isoleucine(I)
            elif codon == 'AUU' or codon == 'AUC' or codon == 'AUA':
                protein = protein + 'I'
            #Valine(V)
            elif codon == 'GUU' or codon == 'GUC' or codon == 'GUA' \
            or codon == 'GUG':
                protein = protein + 'V'
            #Serine(S)
            elif codon == 'UCU' or codon == 'UCC' or codon == 'UCA' \
            or codon == 'UCG' or codon == 'AGU' or codon == 'AGC':
                protein = protein + 'S'
            #Proline(P)
            elif codon == 'CCU' or codon == 'CCC' or codon == 'CCA' \
            or codon == 'CCG':
                protein = protein + 'P'
            #Threonine(T)
            elif codon == 'ACU' or codon == 'ACC' or codon == 'ACA' \
            or codon == 'ACG':
                protein = protein + 'T'
            #Alaline(A)
            elif codon == 'GCU' or codon == 'GCC' or codon == 'GCA' \
            or codon == 'GCG':
                protein = protein + 'A'
            #Tyrosine(Y)
            elif codon == 'UAU' or codon == 'UAC':
                protein = protein + 'Y'
            #Histidine(H)
            elif codon == 'CAU' or codon == 'CAC':
                protein = protein + 'H'
            #Glutamine(Q)
            elif codon == 'CAA' or codon == 'CAG':
                protein = protein + 'Q'
            #Asparagine(N)
            elif codon == 'AAU' or codon == 'AAC':
                protein = protein + 'N'
            #Lysine(K)
            elif codon == 'AAA' or codon == 'AAG':
                protein = protein + 'K'
            #Aspartate(D)
            elif codon == 'GAU' or codon == 'GAC':
                protein = protein + 'D'
            #Glutamate(E)
            elif codon == 'GAA' or codon == 'GAG':
                protein = protein + 'E'
            #Cysteine(C)
            elif codon == 'UGU' or codon == 'UGC':
                protein = protein + 'C'
            #Tryptophan(W)
            elif codon == 'UGG':
                protein = protein + 'W'
            #Arginine(R)
            elif codon == 'CGU' or codon == 'CGC' or codon == 'CGA' \
            or codon == 'CGG' or codon == 'AGA' or codon == 'AGG':
                protein = protein + 'R'
            #Glycine(G)
            elif codon == 'GGU' or codon == 'GGC' or codon == 'GGA' \
            or codon == 'GGG':
                protein = protein + 'G'
            #Stop codons
            elif codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
                break
            #Exception for if codon is not found
            else: 
                raise Exception("No such codon found!")
            
            #Increments counter to move to next codon
            counter = counter + 3
        
        return protein
