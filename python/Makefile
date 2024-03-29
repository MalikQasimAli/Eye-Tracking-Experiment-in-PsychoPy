UNAME           = $(shell uname)

ifeq ($(UNAME),Linux)
#PYTHON = /opt/modules/python/3.7/bin/python3.7
# PYTHON = /usr/bin/python3
# PYTHON = /opt/local/bin/python3.8
endif

ifeq ($(UNAME),Darwin)
PYTHON = /opt/local/bin/python
R = /usr/local/bin/R
endif

# use Butterworth?
SMOOTH = False

WIDTH = 1920
HEIGHT = 1080
#HERTZ = 60
HERTZ = 60
DIST = 21.65 # 55 cm
#SCREEN = 19
SCREEN = 17

DFWIDTH = 5
DFDEGREE = 3

BASELINE_T = 2.0
END_T = 180.0
# what I had for testing but we reverted back to 100.0
#VT = 5.0  # more fixations
#VT = 10.0
#VT = 20.0
VT = 44.0
#VT = 80.0
#VT = 100.0
#VT = 200.0
#VT = 240.0 # fewer fixations -- good results here

XTILES = 8
YTILES = 4

INDIR = trial_data/
AOIDIR = trial_aoi/
IMGDIR = trial_stimuli/

PLTDIR = ./plots/
OUTDIR = ./data/
RAWDIR = ./data/raw/

#all: dirs raw
all: dirs raw process collate stats

dirs:
	mkdir -p data/raw
	mkdir -p figs
	mkdir -p plots
	mkdir -p graphs

raw:
	$(PYTHON) ./hdf52csv.py --indir=$(INDIR) --outdir=$(RAWDIR) --width=$(WIDTH) --height=$(HEIGHT) --dist=$(DIST)
#	$(PYTHON) ./hdf52raw.py --indir=$(INDIR) --outdir=$(RAWDIR) --width=$(WIDTH) --height=$(HEIGHT) --dist=$(DIST)

process:
	$(PYTHON) ./filter.py --smooth=$(SMOOTH) --indir=$(RAWDIR) --imgdir=$(IMGDIR) --dist=$(DIST) --screen=$(SCREEN) --width=$(WIDTH) --height=$(HEIGHT) --hertz=$(HERTZ) --dfdegree=$(DFDEGREE) --dfwidth=$(DFWIDTH) --xtiles=$(XTILES) --ytiles=$(YTILES) --baselineT=$(BASELINE_T) --endT=$(END_T) --vt=$(VT) --aoidir=$(AOIDIR) --outdir=$(OUTDIR)

graph:
	$(PYTHON) ./graph.py --smooth=$(SMOOTH) --indir=$(RAWDIR) --imgdir=$(IMGDIR) --dist=$(DIST) --screen=$(SCREEN) --width=$(WIDTH) --height=$(HEIGHT) --hertz=$(HERTZ) --dfdegree=$(DFDEGREE) --dfwidth=$(DFWIDTH) --xtiles=$(XTILES) --ytiles=$(YTILES) --baselineT=$(BASELINE_T) --endT=$(END_T) --vt=$(VT) --aoidir=$(AOIDIR) --outdir=$(OUTDIR) --pltdir=$(PLTDIR)

collate:
	$(PYTHON) ./collate-amfo.py
	$(PYTHON) ./collate-fxtn.py
	$(PYTHON) ./collate-fxtn-aois.py
	$(PYTHON) ./collate-pICALH.py

stats:
	R --vanilla < wm.R > wm.out

clean:
	rm -rf __pycache__
	rm -f *.pyc
	rm -rf figs
	rm -rf plots
	rm -rf data
	rm -rf graphs
	rm -f *.Rout
	rm -f *.RData
	rm -f .RData
	rm -f .Rapp.history
