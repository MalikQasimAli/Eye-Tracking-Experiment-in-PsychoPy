set PYTHON=python

# use Butterworth?
set SMOOTH=False

set WIDTH=1920
set HEIGHT=1080
set HERTZ=60
set DIST=60
set SCREEN=17

set DFWIDTH=5
set DFDEGREE=3

set BASELINE_T=2.0
set END_T=180.0
REM what I had for testing but we reverted back to 100.0
REM VT=5.0  # more fixations
REM set VT=10.0
REM VT=10.0
set VT=44.0
REM VT=80.0
REM VT=100.0
REM VT=200.0
REM VT=240.0 # fewer fixations -- good results here

SET XTILES=8
SET YTILES=4

set INDIR=trial_data/
set AOIDIR=trial_aoi/
set IMGDIR=trial_stimuli/

set PLTDIR=./plots/
set OUTDIR=./data/
set RAWDIR=./data/raw/

REM process

%PYTHON% ./filter.py --smooth=%SMOOTH% --indir=%RAWDIR% --imgdir=%IMGDIR% --dist=%DIST% --screen=%SCREEN% --width=%WIDTH% --height=%HEIGHT% --hertz=%HERTZ% --dfdegree=%DFDEGREE% --dfwidth=%DFWIDTH% --xtiles=%XTILES% --ytiles=%YTILES% --baselineT=%BASELINE_T% --endT=%END_T% --vt=%VT% --aoidir=%AOIDIR% --outdir=%OUTDIR%
