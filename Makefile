CD = cd source &&
TEX = pdflatex -shell-escape -interaction=nonstopmode -file-line-error
PRE =  $(TEX) -ini -job-name="preamble" "&pdflatex preamble.tex\dump"
BIB = bibtex

.PHONY: all view clean animations plots test

all : source/report.pdf
	mkdir -p output/resources
	rm -f source/report.aux
	rm -f source/report.bbl
	rm -f source/report.blg
	rm -f source/report-blx.bib
	rm -f source/report.log
	rm -f source/report.run.xml
	rm -f source/report.out
	mv source/report.pdf output/140010007.pdf
	mv source/build/* output/resources
	cp source/animation.html output/140010007.html
	rm -rf source/build/

clean:
	rm -rf output/

view:
	evince output/report.pdf

animations: source/time_animation.py source/coordinate_animation.py
	mkdir -p source/build/
	python source/coordinate_animation.py
	python source/time_animation.py
	mv coordinate_animation.mp4 source/build/
	mv time_animation.mp4 source/build/

plots: source/plot_theta_theta_dash.py source/plot_theta_time.py
	mkdir -p source/build/
	python source/plot_theta_theta_dash.py
	python source/plot_theta_time.py
	mv pendulum.png source/build/
	mv theta_vs_theta_dash.png source/build/

test:
	$(CD) nosetests

source/report.pdf : animations plots source/report.tex source/report.bbl source/report.blg
# source/report.pdf : source/report.tex source/report.bbl source/report.blg
	$(CD) $(TEX) report.tex

source/report.bbl source/report.blg : source/report.bib source/report.aux
	$(CD) $(BIB) report

source/report.aux : source/report.tex
	$(CD) $(TEX) report.tex

source/report.bib : source/report.tex
	$(CD) $(TEX) report.tex
