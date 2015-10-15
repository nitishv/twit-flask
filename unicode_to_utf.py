import sys

infile = sys.argv[1]
outfile = infile + '.utf'
with open(infile) as fin:
	with open(outfile, 'wb') as fout:
		for line in fin.readlines():
			fout.write(str(line.encode('utf-8')))
			
	
