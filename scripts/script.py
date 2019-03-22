"""Using tkinter in this code is to open up a file dialogue for the user to choose a file.
This is external code found on https://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python
and https://pythonspot.com/tk-file-dialogs/.

The code for opening, reading, and saving a file is external code,
found on https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python.

The code for making a directory and getting the current working directory (cwd) is external code,
found on https://thispointer.com/how-to-create-a-directory-in-python/ and
https://automatetheboringstuff.com/chapter9/.
"""

#Opens file dialogue for user to pick a file
import tkinter
from tkinter import filedialog

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

import os

from modules.classes_and_functions import remove_blanks, RNA_pol, Ribosome

root = tkinter.Tk()
root.withdraw()

print("Please remove header from .fasta files before using this tool!")
print("Please select .fasta file to transcribe, translate, or transcribe&translate.")

file_path = filedialog.askopenfilename()
fasta_seq = open(file_path)
fasta_seq_read = fasta_seq.read()

# Asks user what they want to do with the .fasta file, then performs the algorithm
#  and writes result to a new .fasta file and saves it in a new folder
option = input("Do you wish to 'transcribe', 'translate', or 'transcribe&translate'?")

if option == 'transcribe':
    
    RNA_seq = RNA_pol.transcribe(fasta_seq_read)
    
    RNA_name = input("What do you want to name the RNA fasta file? " + \
                     "Please DON'T include any of the following characters : \ / : * ? < > |")
    
    try:
        os.mkdir('RNA sequences')
        os.chdir('RNA sequences')
        file = open(RNA_name + '.fasta', 'w')
        file.write(RNA_seq)
        print("File saved as " + RNA_name + ".fasta in location of " + os.getcwd() + \
              ". Thanks for using DNA transcriber 1.0!")
    
    except FileExistsError:
        os.chdir('RNA sequences')
        file = open(RNA_name + '.fasta', 'w')
        file.write(RNA_seq)
        print("File saved as " + RNA_name + ".fasta in location of " + os.getcwd() + \
              ". Thanks for using DNA transcriber 1.0!")

elif option == 'translate':
   
    protein_seq = Ribosome.translate(fasta_seq_read)
    
    protein_name = input("What do you want to name the protein fasta file? " + \
                         "Please DON'T include any of the following characters : \ / : * ? < > |")
    
    try:
        os.mkdir('Protein sequences')
        os.chdir('Protein sequences')
        file = open(protein_name + '.fasta', 'w')
        file.write(protein_seq)
        print("File saved as " + protein_name + ".fasta in location of " + os.getcwd() + \
              ". Thanks for using RNA translator 1.0!")
    
    except FileExistsError:
        os.chdir('Protein sequences')
        file = open(protein_name + '.fasta', 'w')
        file.write(protein_seq)
        print("File saved as " + protein_name + ".fasta in location of " + os.getcwd() + \
              ". Thanks for using RNA translator 1.0!")

elif option == 'transcribe&translate':
    
    protein_seq = Ribosome.translate(RNA_pol.transcribe(fasta_seq_read))
    
    protein_name = input("What do you want to name the protein fasta file? " + \
                         "Please DON'T include any of the following characters : \ / : * ? < > |")
    
    try:
        os.mkdir('Protein sequences')
        os.chdir('Protein sequences')
        file = open(protein_name + '.fasta', 'w')
        file.write(protein_seq)
        print("File saved as " + protein_name + ".fasta in location of " + os.getcwd() + \
              ". Thanks for using DNA transcriber&translator 1.0!")
    
    except FileExistsError:
        os.chdir('Protein sequences')
        file = open(protein_name + '.fasta', 'w')
        file.write(protein_seq)
        print("File saved as " + protein_name + ".fasta in location of " + os.getcwd() + \
              ". Thanks for using DNA transcriber&translator 1.0!")

else:
    
    raise Exception("Please enter only 'transcribe', 'translate', or 'transcribe&translate'!")
