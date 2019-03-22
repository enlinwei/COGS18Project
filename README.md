# COGS18Project
Final project for UCSD course COGS18 "Introduction to Python", Fall quarter 2018.

## Project Description:
The purpose of this project is to create a tool that is useful for life sciences: it allows the user to quickly transcribe DNA sequences to RNA sequences, or translate RNA sequences to proteins (which are composed of amino acid sequences), or go from DNA straight to protein. These are very important steps in life sciences and this tool can hopefully help speed up data analysis in life science research.
The tool is created to work with .fasta files (basically simple text files), which is the predominant form of storing sequences of DNA, RNA, and proteins. The tool allows the user to select a .fasta file containing a DNA or RNA sequence from the computer file dialogue and will output the resulting sequence, either transcribed and/or translated into an RNA or protein sequence, in a .fasta file and save it in a new folder "RNA sequences" or "Protein sequences" in the script (or in the new folder if it already exists). The folder will be found in the same folder as the script.

## Biology Primer:
-RNA polymerase (RNA_pol)
In biology, DNA sequences need to be 'transcribed' into RNA sequences before they can be 'translated' into proteins. The RNA sequences are basically the same as DNA sequences, except all T's are replaced with U's. The class RNA_pol transcribes a DNA sequence into an RNA sequence (replaces all instances of 'T' or 't' with 'U').

-Ribosome
In biology, DNA sequences need to be 'transcribed' into RNA sequences before they can be 'translated' into proteins. Translation is done by things in cells called 'ribosomes'. To translate an RNA into protein, it is read in 'codons' of 3 RNA bases at a time; each codon codes for one amino acid, the building blocks of proteins. Thus, a protein is at the very basic level a string of amino acids. Some different codons code for the same amino acid. For example:
'UUU' and 'UUC' both code for the amino acid phenylalanine, represented by the symbol F. The Ribosome would add a phenylalanine to the amino acid sequence, and then move to the next codon.
Translation starts at the first 'AUG' in the RNA sequence; 'AUG' codes for the amino acid methionine (M). Three special codons, 'UAA', 'UAG', and 'UGA', are called "stop codons"; they don't code for anything, but when these codons are reached, translation is done and the protein is complete.

## Project Code:
This project uses tkinter to bring up a file dialogue for the user to select files, which does not work in Jupyter Notebook. Thus, the code for this project is to be run from the Anaconda Prompt or OS command prompt only, on the script.py file in the "scripts" folder.
The pytest for this project needs to import pytest, which does not work on the OS command prompt; thus it is to be run from the Anaconda Prompt or the Jupyter Notebook terminal only, on the tests.py file in the "modules" folder.
