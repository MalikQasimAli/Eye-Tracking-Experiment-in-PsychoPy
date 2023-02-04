#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on February 04, 2023, at 01:54
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, iohub, hardware
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'eth_ws_team_p04'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'gender': '',
    'profession': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='D:\\Work\\ETH Workshop\\workshop_work\\hands_workshop\\eth_ws_team_p04_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[1.0000, 1.0000, 1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup eyetracking
ioConfig['eyetracker.hw.tobii.EyeTracker'] = {
    'name': 'tracker',
    'model_name': 'Tobii Pro Fusion',
    'serial_number': 'TPFC1-010200149364',
    'runtime_settings': {
        'sampling_rate': 120.0,
    }
}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, experiment_code='eth_ws_team_p04', session_code=ioSession, datastore_name=filename, **ioConfig)
eyetracker = ioServer.getDevice('tracker')

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "calib_instr" ---
calb_img = visual.ImageStim(
    win=win,
    name='calb_img', 
    image='instructions/calib_i.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
cal_keyb = keyboard.Keyboard()

# --- Initialize components for Routine "valid_instr" ---
valid_img = visual.ImageStim(
    win=win,
    name='valid_img', 
    image='instructions/valid_i.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
valid_keybrd = keyboard.Keyboard()

# --- Initialize components for Routine "calib_count" ---
# Run 'Begin Experiment' code from ccode_calib_count
timeout = 10

from math import atan2, degrees

h = 19.7 # Monitor height in cm
d = 62 # Distance between monitor and participant in cm
r = 1080 # Vertical resolution of the monitor

# Calculate the number of degrees that correspond to a single pixel.
deg_per_px = degrees(atan2(.5*h, d)) / (.5*r)

# Calculate the number of degrees that correspond to a number in height units.
deg_per_hu = deg_per_px * r
calib_text = visual.TextStim(win=win, name='calib_text',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
calib_resp = keyboard.Keyboard()

# --- Initialize components for Routine "title" ---
txt_title = visual.TextStim(win=win, name='txt_title',
    text='::: Safety Inspecter :::',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
img_title = visual.ImageStim(
    win=win,
    name='img_title', 
    image='C:/Users/qasim/Downloads/WhatsApp Image 2023-01-12 at 9.21.17 AM.jpeg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(1, 0.7),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
txt_continue = visual.TextStim(win=win, name='txt_continue',
    text=':: Press space to start  ::',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
title_resp = keyboard.Keyboard()

# --- Initialize components for Routine "instructions" ---
inst_title = visual.TextStim(win=win, name='inst_title',
    text='::: Instructions :::',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text = visual.TextStim(win=win, name='text',
    text='You are our safety insepctor!\n\n\nA building safety inspector identifies conditions of the building construction that can be safety risks.\n \n\nPlease look at the images and help us to identify damages to the building fabric.\n\n:: Press Space to Start ::',
    font='Open Sans',
    pos=(0, -0.05), height=0.05, wrapWidth=None, ori=0.0, 
    color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "tr_fixation_mark" ---
img_fix = visual.ImageStim(
    win=win,
    name='img_fix', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "tr_questions" ---
# Run 'Begin Experiment' code from code_io_ques
ioServer.sendMessageEvent(text='%s' % win.units, category='units')
et_eye_recording = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
img_ques = visual.ImageStim(
    win=win,
    name='img_ques', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
key_resp_2 = keyboard.Keyboard()

# --- Initialize components for Routine "tr_answers" ---
etRec_trac = hardware.eyetracker.EyetrackerControl(
    tracker=eyetracker,
    actionType='Start and Stop'
)
answer = visual.ImageStim(
    win=win,
    name='answer', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
key_resp_ans = keyboard.Keyboard()

# --- Initialize components for Routine "nasa" ---
nasa_question = visual.TextStim(win=win, name='nasa_question',
    text='',
    font='Open Sans',
    pos=(0, .3), height=0.02, wrapWidth=1.0, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
nasa_tresec = visual.TextStim(win=win, name='nasa_tresec',
    text='',
    font='Open Sans',
    pos=(0, .2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
nasa_slider = visual.Slider(win=win, name='nasa_slider',
    startValue=None, size=(1.0, 0.02), pos=(0, 0), units=None,
    labels=["no","yes"], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20), granularity=1.0,
    style='radio', styleTweaks=(), opacity=None,
    labelColor='gray', markerColor='blue', lineColor='lightgray', colorSpace='rgb',
    font='Open Sans', labelHeight=0.03,
    flip=False, ori=0.0, depth=-2, readOnly=False)

# --- Initialize components for Routine "end" ---
end_img = visual.ImageStim(
    win=win,
    name='end_img', 
    image='stimuli/thankyou.jpg', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "calib_instr" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
cal_keyb.keys = []
cal_keyb.rt = []
_cal_keyb_allKeys = []
# keep track of which components have finished
calib_instrComponents = [calb_img, cal_keyb]
for thisComponent in calib_instrComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "calib_instr" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *calb_img* updates
    if calb_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        calb_img.frameNStart = frameN  # exact frame index
        calb_img.tStart = t  # local t and not account for scr refresh
        calb_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(calb_img, 'tStartRefresh')  # time at next scr refresh
        calb_img.setAutoDraw(True)
    
    # *cal_keyb* updates
    waitOnFlip = False
    if cal_keyb.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        cal_keyb.frameNStart = frameN  # exact frame index
        cal_keyb.tStart = t  # local t and not account for scr refresh
        cal_keyb.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(cal_keyb, 'tStartRefresh')  # time at next scr refresh
        cal_keyb.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(cal_keyb.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(cal_keyb.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if cal_keyb.status == STARTED and not waitOnFlip:
        theseKeys = cal_keyb.getKeys(keyList=['space'], waitRelease=False)
        _cal_keyb_allKeys.extend(theseKeys)
        if len(_cal_keyb_allKeys):
            cal_keyb.keys = _cal_keyb_allKeys[-1].name  # just the last key pressed
            cal_keyb.rt = _cal_keyb_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in calib_instrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "calib_instr" ---
for thisComponent in calib_instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "calib_instr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
calib_loop = data.TrialHandler(nReps=timeout, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='calib_loop')
thisExp.addLoop(calib_loop)  # add the loop to the experiment
thisCalib_loop = calib_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisCalib_loop.rgb)
if thisCalib_loop != None:
    for paramName in thisCalib_loop:
        exec('{} = thisCalib_loop[paramName]'.format(paramName))

for thisCalib_loop in calib_loop:
    currentLoop = calib_loop
    # abbreviate parameter names if possible (e.g. rgb = thisCalib_loop.rgb)
    if thisCalib_loop != None:
        for paramName in thisCalib_loop:
            exec('{} = thisCalib_loop[paramName]'.format(paramName))
    # define target for calibration
    calibrationTarget = visual.TargetStim(win, 
        name='calibrationTarget',
        radius=0.01, fillColor='white', borderColor='black', lineWidth=2.0,
        innerRadius=0.0035, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
        colorSpace='rgb', units=None
    )
    # define parameters for calibration
    calibration = hardware.eyetracker.EyetrackerCalibration(win, 
        eyetracker, calibrationTarget,
        units=None, colorSpace='rgb',
        progressMode='time', targetDur=1.5, expandScale=1.5,
        targetLayout='FIVE_POINTS', randomisePos=True, textColor='black',
        movementAnimation=True, targetDelay=1.0
    )
    # run calibration
    calibration.run()
    # clear any keypresses from during calibration so they don't interfere with the experiment
    defaultKeyboard.clearEvents()
    # the Routine "calibration" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "valid_instr" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    valid_keybrd.keys = []
    valid_keybrd.rt = []
    _valid_keybrd_allKeys = []
    # keep track of which components have finished
    valid_instrComponents = [valid_img, valid_keybrd]
    for thisComponent in valid_instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "valid_instr" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *valid_img* updates
        if valid_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            valid_img.frameNStart = frameN  # exact frame index
            valid_img.tStart = t  # local t and not account for scr refresh
            valid_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(valid_img, 'tStartRefresh')  # time at next scr refresh
            valid_img.setAutoDraw(True)
        
        # *valid_keybrd* updates
        waitOnFlip = False
        if valid_keybrd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            valid_keybrd.frameNStart = frameN  # exact frame index
            valid_keybrd.tStart = t  # local t and not account for scr refresh
            valid_keybrd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(valid_keybrd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'valid_keybrd.started')
            valid_keybrd.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(valid_keybrd.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(valid_keybrd.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if valid_keybrd.status == STARTED and not waitOnFlip:
            theseKeys = valid_keybrd.getKeys(keyList=['space'], waitRelease=False)
            _valid_keybrd_allKeys.extend(theseKeys)
            if len(_valid_keybrd_allKeys):
                valid_keybrd.keys = _valid_keybrd_allKeys[-1].name  # just the last key pressed
                valid_keybrd.rt = _valid_keybrd_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in valid_instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "valid_instr" ---
    for thisComponent in valid_instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "valid_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    # define target for validation
    validationTarget = visual.TargetStim(win, 
        name='validationTarget',
        radius=0.01, fillColor='white', borderColor='black', lineWidth=2.0,
        innerRadius=0.0035, innerFillColor='green', innerBorderColor='black', innerLineWidth=2.0,
        colorSpace='rgb', units=None
    )
    # define parameters for validation
    validation = iohub.ValidationProcedure(win,
        target=validationTarget,
        gaze_cursor='green', 
        positions='FIVE_POINTS', randomize_positions=True,
        expand_scale=1.5, target_duration=1.5,
        enable_position_animation=True, target_delay=1.0,
        progress_on_key=None, text_color='black',
        show_results_screen=True, save_results_screen=False,
        color_space='rgb', unit_type=None
    )
    # run validation
    validation.run()
    # clear any keypresses from during validation so they don't interfere with the experiment
    defaultKeyboard.clearEvents()
    # the Routine "validation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "calib_count" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from ccode_calib_count
    #present validation results
    results = validation.getValidationResults()
    valid_results = "Validation Results in height units\nMin: %.4f, Max: %.4f, Mean: %.4f (%s units)\n" % \
      (results['min_error'], results['max_error'], results['mean_error'], \
       results['reporting_unit_type'])
    
    valid_results_deg = "Validation Results in degree visual angle\nMin: %.4f, Max: %.4f, Mean: %.4f" % \
      (results['min_error']*deg_per_hu, results['max_error']*deg_per_hu, results['mean_error']*deg_per_hu)
    
    calib_query = "%s\n%s\n\nRecalibrate (y/n)?" % (valid_results,valid_results_deg)
    calib_text.setText(calib_query)
    calib_resp.keys = []
    calib_resp.rt = []
    _calib_resp_allKeys = []
    # keep track of which components have finished
    calib_countComponents = [calib_text, calib_resp]
    for thisComponent in calib_countComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "calib_count" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *calib_text* updates
        if calib_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            calib_text.frameNStart = frameN  # exact frame index
            calib_text.tStart = t  # local t and not account for scr refresh
            calib_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(calib_text, 'tStartRefresh')  # time at next scr refresh
            calib_text.setAutoDraw(True)
        
        # *calib_resp* updates
        waitOnFlip = False
        if calib_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            calib_resp.frameNStart = frameN  # exact frame index
            calib_resp.tStart = t  # local t and not account for scr refresh
            calib_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(calib_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'calib_resp.started')
            calib_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(calib_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(calib_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if calib_resp.status == STARTED and not waitOnFlip:
            theseKeys = calib_resp.getKeys(keyList=['y','n'], waitRelease=False)
            _calib_resp_allKeys.extend(theseKeys)
            if len(_calib_resp_allKeys):
                calib_resp.keys = [key.name for key in _calib_resp_allKeys]  # storing all keys
                calib_resp.rt = [key.rt for key in _calib_resp_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in calib_countComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "calib_count" ---
    for thisComponent in calib_countComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from ccode_calib_count
    #calib_resp Keyboard component must have set Store: all keys
    if calib_resp is not None and 'n' in calib_resp.keys:
        print (valid_results,valid_results_deg)
        calib_loop.finished = True
    # check responses
    if calib_resp.keys in ['', [], None]:  # No response was made
        calib_resp.keys = None
    calib_loop.addData('calib_resp.keys',calib_resp.keys)
    if calib_resp.keys != None:  # we had a response
        calib_loop.addData('calib_resp.rt', calib_resp.rt)
    # the Routine "calib_count" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed timeout repeats of 'calib_loop'


# --- Prepare to start Routine "title" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
title_resp.keys = []
title_resp.rt = []
_title_resp_allKeys = []
# keep track of which components have finished
titleComponents = [txt_title, img_title, txt_continue, title_resp]
for thisComponent in titleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "title" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *txt_title* updates
    if txt_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txt_title.frameNStart = frameN  # exact frame index
        txt_title.tStart = t  # local t and not account for scr refresh
        txt_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt_title, 'tStartRefresh')  # time at next scr refresh
        txt_title.setAutoDraw(True)
    
    # *img_title* updates
    if img_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        img_title.frameNStart = frameN  # exact frame index
        img_title.tStart = t  # local t and not account for scr refresh
        img_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(img_title, 'tStartRefresh')  # time at next scr refresh
        img_title.setAutoDraw(True)
    
    # *txt_continue* updates
    if txt_continue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        txt_continue.frameNStart = frameN  # exact frame index
        txt_continue.tStart = t  # local t and not account for scr refresh
        txt_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(txt_continue, 'tStartRefresh')  # time at next scr refresh
        txt_continue.setAutoDraw(True)
    
    # *title_resp* updates
    waitOnFlip = False
    if title_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        title_resp.frameNStart = frameN  # exact frame index
        title_resp.tStart = t  # local t and not account for scr refresh
        title_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(title_resp, 'tStartRefresh')  # time at next scr refresh
        title_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(title_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(title_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if title_resp.status == STARTED and not waitOnFlip:
        theseKeys = title_resp.getKeys(keyList=['space'], waitRelease=False)
        _title_resp_allKeys.extend(theseKeys)
        if len(_title_resp_allKeys):
            title_resp.keys = _title_resp_allKeys[-1].name  # just the last key pressed
            title_resp.rt = _title_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in titleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "title" ---
for thisComponent in titleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if title_resp.keys in ['', [], None]:  # No response was made
    title_resp.keys = None
thisExp.addData('title_resp.keys',title_resp.keys)
if title_resp.keys != None:  # we had a response
    thisExp.addData('title_resp.rt', title_resp.rt)
thisExp.nextEntry()
# the Routine "title" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
instructionsComponents = [inst_title, text, key_resp]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "instructions" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *inst_title* updates
    if inst_title.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        inst_title.frameNStart = frameN  # exact frame index
        inst_title.tStart = t  # local t and not account for scr refresh
        inst_title.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(inst_title, 'tStartRefresh')  # time at next scr refresh
        inst_title.setAutoDraw(True)
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text.started')
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions" ---
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trials_code.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "tr_fixation_mark" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    img_fix.setImage('stimuli/' + fix)
    # keep track of which components have finished
    tr_fixation_markComponents = [img_fix]
    for thisComponent in tr_fixation_markComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "tr_fixation_mark" ---
    while continueRoutine and routineTimer.getTime() < 0.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *img_fix* updates
        if img_fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            img_fix.frameNStart = frameN  # exact frame index
            img_fix.tStart = t  # local t and not account for scr refresh
            img_fix.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_fix, 'tStartRefresh')  # time at next scr refresh
            img_fix.setAutoDraw(True)
        if img_fix.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img_fix.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                img_fix.tStop = t  # not accounting for scr refresh
                img_fix.frameNStop = frameN  # exact frame index
                img_fix.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tr_fixation_markComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "tr_fixation_mark" ---
    for thisComponent in tr_fixation_markComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.500000)
    
    # --- Prepare to start Routine "tr_questions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_io_ques
    ioServer.sendMessageEvent(text='%s%s' % ('start:',trial_id), category = 'trial_question')
    img_ques.setImage('stimuli/' + ques)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    tr_questionsComponents = [et_eye_recording, img_ques, key_resp_2]
    for thisComponent in tr_questionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "tr_questions" ---
    while continueRoutine and routineTimer.getTime() < 60.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *et_eye_recording* updates
        if et_eye_recording.status == NOT_STARTED and t >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            et_eye_recording.frameNStart = frameN  # exact frame index
            et_eye_recording.tStart = t  # local t and not account for scr refresh
            et_eye_recording.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(et_eye_recording, 'tStartRefresh')  # time at next scr refresh
            et_eye_recording.status = STARTED
        if et_eye_recording.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > et_eye_recording.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                et_eye_recording.tStop = t  # not accounting for scr refresh
                et_eye_recording.frameNStop = frameN  # exact frame index
                et_eye_recording.status = FINISHED
        
        # *img_ques* updates
        if img_ques.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            img_ques.frameNStart = frameN  # exact frame index
            img_ques.tStart = t  # local t and not account for scr refresh
            img_ques.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(img_ques, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'img_ques.started')
            img_ques.setAutoDraw(True)
        if img_ques.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > img_ques.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                img_ques.tStop = t  # not accounting for scr refresh
                img_ques.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'img_ques.stopped')
                img_ques.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_2.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tr_questionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "tr_questions" ---
    for thisComponent in tr_questionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_io_ques
    ioServer.sendMessageEvent(text='%s%s' % ('end:',trial_id), category = 'trial_question')
    # make sure the eyetracker recording stops
    if et_eye_recording.status != FINISHED:
        et_eye_recording.status = FINISHED
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-60.500000)
    
    # --- Prepare to start Routine "tr_answers" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_io_answ
    ioServer.sendMessageEvent(text='%s%s' % ('start:',trial_id), category = 'trial_answer')
    answer.setImage('stimuli/' + answ)
    key_resp_ans.keys = []
    key_resp_ans.rt = []
    _key_resp_ans_allKeys = []
    # keep track of which components have finished
    tr_answersComponents = [etRec_trac, answer, key_resp_ans]
    for thisComponent in tr_answersComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "tr_answers" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *etRec_trac* updates
        if etRec_trac.status == NOT_STARTED and t >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            etRec_trac.frameNStart = frameN  # exact frame index
            etRec_trac.tStart = t  # local t and not account for scr refresh
            etRec_trac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(etRec_trac, 'tStartRefresh')  # time at next scr refresh
            etRec_trac.status = STARTED
        
        # *answer* updates
        if answer.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            answer.frameNStart = frameN  # exact frame index
            answer.tStart = t  # local t and not account for scr refresh
            answer.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(answer, 'tStartRefresh')  # time at next scr refresh
            answer.setAutoDraw(True)
        
        # *key_resp_ans* updates
        waitOnFlip = False
        if key_resp_ans.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            key_resp_ans.frameNStart = frameN  # exact frame index
            key_resp_ans.tStart = t  # local t and not account for scr refresh
            key_resp_ans.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_ans, 'tStartRefresh')  # time at next scr refresh
            key_resp_ans.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_ans.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_ans.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_ans.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_ans.getKeys(keyList=['a','b','c'], waitRelease=False)
            _key_resp_ans_allKeys.extend(theseKeys)
            if len(_key_resp_ans_allKeys):
                key_resp_ans.keys = _key_resp_ans_allKeys[-1].name  # just the last key pressed
                key_resp_ans.rt = _key_resp_ans_allKeys[-1].rt
                # was this correct?
                if (key_resp_ans.keys == str(cor)) or (key_resp_ans.keys == cor):
                    key_resp_ans.corr = 1
                else:
                    key_resp_ans.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in tr_answersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "tr_answers" ---
    for thisComponent in tr_answersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_io_answ
    ioServer.sendMessageEvent(text='%s%s' % ('end:',trial_id), category = 'trial_answer')
    # make sure the eyetracker recording stops
    if etRec_trac.status != FINISHED:
        etRec_trac.status = FINISHED
    # check responses
    if key_resp_ans.keys in ['', [], None]:  # No response was made
        key_resp_ans.keys = None
        # was no response the correct answer?!
        if str(cor).lower() == 'none':
           key_resp_ans.corr = 1;  # correct non-response
        else:
           key_resp_ans.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_ans.keys',key_resp_ans.keys)
    trials.addData('key_resp_ans.corr', key_resp_ans.corr)
    if key_resp_ans.keys != None:  # we had a response
        trials.addData('key_resp_ans.rt', key_resp_ans.rt)
    # the Routine "tr_answers" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
nasa_trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('nasa_tlx_eng.csv'),
    seed=None, name='nasa_trials')
thisExp.addLoop(nasa_trials)  # add the loop to the experiment
thisNasa_trial = nasa_trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisNasa_trial.rgb)
if thisNasa_trial != None:
    for paramName in thisNasa_trial:
        exec('{} = thisNasa_trial[paramName]'.format(paramName))

for thisNasa_trial in nasa_trials:
    currentLoop = nasa_trials
    # abbreviate parameter names if possible (e.g. rgb = thisNasa_trial.rgb)
    if thisNasa_trial != None:
        for paramName in thisNasa_trial:
            exec('{} = thisNasa_trial[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "nasa" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    nasa_question.setText(nasa_ques)
    nasa_tresec.setText(nasa_tre)
    nasa_slider.reset()
    # keep track of which components have finished
    nasaComponents = [nasa_question, nasa_tresec, nasa_slider]
    for thisComponent in nasaComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "nasa" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *nasa_question* updates
        if nasa_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nasa_question.frameNStart = frameN  # exact frame index
            nasa_question.tStart = t  # local t and not account for scr refresh
            nasa_question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nasa_question, 'tStartRefresh')  # time at next scr refresh
            nasa_question.setAutoDraw(True)
        
        # *nasa_tresec* updates
        if nasa_tresec.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nasa_tresec.frameNStart = frameN  # exact frame index
            nasa_tresec.tStart = t  # local t and not account for scr refresh
            nasa_tresec.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nasa_tresec, 'tStartRefresh')  # time at next scr refresh
            nasa_tresec.setAutoDraw(True)
        
        # *nasa_slider* updates
        if nasa_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nasa_slider.frameNStart = frameN  # exact frame index
            nasa_slider.tStart = t  # local t and not account for scr refresh
            nasa_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nasa_slider, 'tStartRefresh')  # time at next scr refresh
            nasa_slider.setAutoDraw(True)
        
        # Check nasa_slider for response to end routine
        if nasa_slider.getRating() is not None and nasa_slider.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in nasaComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "nasa" ---
    for thisComponent in nasaComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    nasa_trials.addData('nasa_slider.response', nasa_slider.getRating())
    # the Routine "nasa" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'nasa_trials'


# --- Prepare to start Routine "end" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
endComponents = [end_img, key_resp_3]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "end" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_img* updates
    if end_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_img.frameNStart = frameN  # exact frame index
        end_img.tStart = t  # local t and not account for scr refresh
        end_img.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_img, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'end_img.started')
        end_img.setAutoDraw(True)
    if end_img.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_img.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            end_img.tStop = t  # not accounting for scr refresh
            end_img.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_img.stopped')
            end_img.setAutoDraw(False)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3.started')
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "end" ---
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "end" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
