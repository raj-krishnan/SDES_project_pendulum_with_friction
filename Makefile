CD = cd source &&
TEX = pdflatex -shell-escape -interaction=nonstopmode -file-line-error
PRE =  $(TEX) -ini -job-name="preamble" "&pdflatex preamble.tex\dump"
BIB = bibtex

.PHONY: all view clean animations plots

all : source/report.pdf
	rm -f source/report.aux
	rm -f source/report.bbl
	rm -f source/report.blg
	rm -f source/report-blx.bib
	rm -f source/report.log
	rm -f source/report.run.xml
	rm -f source/report.out
	mv source/report.pdf output/report.pdf

clean:
	rm -rf output/

view:
	open output/report.pdf

animations: source/time_animation.py source/coordinate_animation.py
	python source/coordinate_animation.py
	python source/time_animation.py

plots: source/plot_theta_theta_dash.py source/plot_theta_time.py
	python source/plot_theta_theta_dash.py
	python source/plot_theta_time.py

source/report.pdf : source/report.tex source/report.bbl source/report.blg
	$(CD) $(TEX) report.tex

source/report.bbl source/report.blg : source/report.bib source/report.aux
	$(CD) $(BIB) report

source/report.aux : source/report.tex
	$(CD) $(TEX) report.tex

source/report.bib : source/report.tex
	$(CD) $(TEX) report.tex
