import os
import cv2
import numpy as np
import random





### PATH TO PLACE THE EXTRACTED FRAMES 
path_to_frame_folder = input("Path to frame folder? \n")
path_to_videos = input("Path to videos? \n")

#path_to_frame_folder = '/home/rb17990/Documents'
#path_to_videos = '/home/rb17990/Documents/TEST VIDS'


#create frame folder to store extracted frames
if not os.path.exists("brood_frames"):
	os.mkdir(os.path.join(path_to_frame_folder, "brood_frames"))


## SINGLE VIDEO PROVIDED

if path_to_videos.endswith(".mp4"):
	print("only one video given, easy peasy ;)")
	
	#rename file
	vidname = os.path.basename(path_to_videos)
	form = '.png'
	
	full_vidname = vidname.strip('.mp4') + form
	
	#directory to brood frame folder
	path_to_folder = os.path.join(path_to_frame_folder, 'brood_frames')
	
	#extract frame
	vidcap = cv2.VideoCapture(path_to_videos)
	success, image = vidcap.read()
	
	totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
	randomFrameNumber = random.randint(0, totalFrames)
	vidcap.set(cv2.CAP_PROP_POS_FRAMES, randomFrameNumber)
	success , image = vidcap.read()
	if success:
		cv2.imwrite(os.path.join(path_to_folder, full_vidname), image)
		print("frame extracted :)")
	

## FOLDER OF VIDEOS PROVIDED
else:
	print("folder of videos provided (what a big job!)")
	
	for filename in os.listdir(path_to_videos):
		if filename.endswith(".mp4"):
			print(filename)
			
			#rename the files
			form='.png'
			full_vidname = filename.strip('.mp4') + form
			
			#directory to brood frame folder
			path_to_folder = os.path.join(path_to_frame_folder, 'brood_frames')
			
			filename_path = os.path.join(path_to_videos, filename)
			
			#extract the frame
			vidcap = cv2.VideoCapture(filename_path)
			success, image = vidcap.read()
			
			totalFrames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
			randomFrameNumber = random.randint(0, totalFrames)
			vidcap.set(cv2.CAP_PROP_POS_FRAMES, randomFrameNumber)
			success , image = vidcap.read()
			if success:
				cv2.imwrite(os.path.join(path_to_folder, full_vidname), image)
				print("frame extracted :)")
			
	
	
	


