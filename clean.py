import sys
import os
import re
import argparse
from argparse import RawTextHelpFormatter
import gzip
import warnings

from ete3 import NCBITaxa
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

ncbi = NCBITaxa()

def is_valid_file(x):
        if not os.path.exists(x):
                raise argparse.ArgumentTypeError("{0} does not exist".format(x))
        return x

class SequenceRead:
	"""A single sequence read class"""
	head = ''
	data = ''
	def __repr__(self):
		return self.head + self.data
	def has_words(self, words_string):
		words_list = words_string.upper().split("|")
		return any(word in self.head.upper() for word in words_list)

def sequence_good(seq):
	match = uniprot_ox.search(seq.head)
	if match:
		try:
			ncbi_lineage = ncbi.get_lineage(match.group(1))
			ncbi_names = ncbi.get_taxid_translator(ncbi_lineage)
			ncbi_name = ncbi_names[ncbi_lineage[2]]
			# prokaryotic
			if ncbi_name in ('Bacteria', 'Archaea', 'Caudovirales', 'unclassified bacterial viruses', 'unclassified archaeal viruses'):
				return True
		except ValueError as e:
			warnings.warn(str(e))
			pass
	return False


usage = 'clean_database.py [-opt1, [-opt2, ...]] infile'
parser = argparse.ArgumentParser(description='A program to clean fasta formatted sequence databases', formatter_class=RawTextHelpFormatter, usage=usage)
parser.add_argument('infile', type=is_valid_file, help='input file in fasta format')
parser.add_argument('-i', '--include', action="store", default="", dest='good_terms', help='sequence read header must contain these strings (vertical pipe separated)')
parser.add_argument('-e', '--exclude', action="store", default="xxx", dest='bad_terms', help='sequence read header must NOT contain these strings (vertical pipe separated)')
args = parser.parse_args()

uniprot_ox = re.compile('OX=(\d+)')

seq = SequenceRead()
with gzip.open(args.infile) as f:
	for line in f:
		line = line.decode('utf-8')
		if line.startswith('>'):
			if seq.has_words(args.good_terms) and not seq.has_words(args.bad_terms) and sequence_good(seq):
				print(seq)
			seq.head = line
			seq.data = ''
		else:
			seq.data += line
			
