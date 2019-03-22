"""Some of these tests are designed to fail (passes if assert fails, and fails if assert passes), which is made
using the "raises" function in pytest on the Exception raised by the code.
The code for passing pytest if the assert fails is external code found on
https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest.
"""

import pytest

from classes_and_functions import remove_blanks, RNA_pol, Ribosome

def test_is_DNA_seq():
    assert RNA_pol.is_DNA('ACCGCAGTCTTA')

def test_not_DNA_seq():
    with pytest.raises(Exception) as e_info:
        RNA_pol.is_DNA('ACCGTAVCGTT')

def test_is_RNA_seq():
    assert Ribosome.is_RNA('ACCGUAUUCGA')

def test_not_RNA_seq():
    with pytest.raises(Exception) as e_info:
        Ribosome.is_RNA('ACUGTATBCGA')

def test_transcribe():
    assert RNA_pol.transcribe('AATGCGAGCTTAA') == 'AAUGCGAGCUUAA'

def test_translate():
    assert Ribosome.translate("CCAUCAUGUUUUUCUUAUUGCUUCUCCUACUGAUUAUCAUAGUUGUCGUAGUGUCUUCCUCAUCGCCUCCCCCACCGACUACCACAACGGCUGCCGCAGCGUAUUACCAUCACCAACAGAAUAACAAAAAGGAUGACGAAGAGUGUUGCUGGCGUCGCCGACGGAGAAGGAGUAGCGGUGGCGGAGGGUAACAGU") == "MFFLLLLLLIIIVVVVSSSSPPPPTTTTAAAAYYHHQQNNKKDDEECCWRRRRRRSSGGGG"

def test_DNA_to_caps():
    assert RNA_pol.DNA_to_caps('aacgtac') == 'AACGTAC'

def test_RNA_to_caps():
    assert Ribosome.RNA_to_caps('aacguac') == 'AACGUAC'

def test_find_start_codon():
    assert Ribosome.find_start_codon('aagaugccagucuu') == 3

def test_not_find_start_codon():
    with pytest.raises(Exception) as e_info:
        Ribosome.find_start_codon('aagauaccagucuu')

def test_stop_codon_UAA():
	assert Ribosome.translate("ACAUGAUGUGGUAACCU") == "MMW"

def test_stop_codon_UAG():
	assert Ribosome.translate("ACAUGAUGUGGUAGCCU") == "MMW"

def test_stop_codon_UGA():
	assert Ribosome.translate("ACAUGAUGUGGUGACCU") == "MMW"
