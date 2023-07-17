# Brood Analysis Pipeline

An analysis pipeline to define the brood region in the videos to calculate time spent on the brood.
All scripts should be downloaded and run through the terminal, inside the brood_gui conda environment.

## Steps:

1. First run the extract_frames_brood.py script, and input the paths to the videos and to where the frames will be stored. A folder will be created to store the frames, called 'brood_frames'. If you have 1 video or if you have a directory of videos, it should all work the same :)
2. Next load the GUI by running the broodROI_selection_gui.py script. Load in the folder with the frames, and click 'brood area'. Another window should pop up with the frame. Define a region of interest (ROI) by click-dragging the mouse over the brood, and a blue rectangle should be drawn. Once you have let go of the ROI, press Enter on the keyboard to save the coordinates. Then close the window, move onto the next frame and repeat :)
3. **Once you have defined a ROI for each frame**, click export results. This will create a csv file in your directory with the results.
4. Close the gui, and now run post_process_brood_data.py in the terminal. This will ask you for paths to the csv file created, and to the h5 files you wish to analyse from DeepLabCut.

