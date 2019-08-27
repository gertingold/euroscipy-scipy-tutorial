.PHONY: all cleantex clean

texfile = presentation
imgdir = images
_imgdownload = phyphox_dark.png coordinate_system.jpg eso1907a.jpg \
	       whitedata_strain_SNR_qscan.jpg sln_cover-2019.pdf
imgfiles = $(patsubst %, $(imgdir)/%, $(_imgdownload))

all: presentation.pdf

presentation.pdf: presentation.tex $(imgfiles)
	pdflatex $(texfile).tex
	pdflatex $(texfile).tex

$(imgdir)/phyphox_dark.png:
	wget https://phyphox.org/wp-content/uploads/2019/06/phyphox_dark.png -O $@

$(imgdir)/coordinate_system.jpg:
	wget http://phyphox.org/wp-content/uploads/2016/04/coordinate_system.jpg -O $@

$(imgdir)/eso1907a.jpg:
	wget https://cdn.eso.org/images/screen/eso1907a.jpg -O $@

$(imgdir)/whitedata_strain_SNR_qscan.jpg:
	wget https://www.ligo.caltech.edu/system/avm_image_sqls/binaries/89/jpg_original/whitedata_strain_SNR_qscan_v11Vhigh.jpg?1506626321 -O $@

$(imgdir)/sln_cover-2019.pdf:
	wget https://github.com/scipy-lectures/scipy-lecture-notes/raw/master/images/cover-2019.pdf -O $@

cleantex:
	rm -f $(texfile).aux $(texfile).log $(texfile).nav \
	      $(texfile).out $(texfile).snm $(texfile).toc \
	      $(texfile).vrb $(texfile).pdf

clean: cleantex
	rm $(imgfiles)
