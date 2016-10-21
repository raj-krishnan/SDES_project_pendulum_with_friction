TEX = pdflatex -shell-escape -interaction=nonstopmode -file-line-error
PRE =  $(TEX) -ini -job-name="preamble" "&pdflatex preamble.tex\dump"
BIB = bibtex

.PHONY: all view

all : report.pdf
	rm -f report.aux
	rm -f report.bbl
	rm -f report.blg
	rm -f report-blx.bib
	rm -f report.log
	rm -f report.run.xml
	rm -f report.out

clean:
	rm -f report.pdf

view :
	open report.pdf

report.pdf : report.tex report.bbl report.blg
	$(TEX) report.tex

report.bbl report.blg : report.bib report.aux
	$(BIB) report

report.aux : report.tex
	$(TEX) report.tex

report.bib : report.tex
	$(TEX) report.tex
