'''
Author: Kai San Chan
Starting Date: 2023/02/21
Last Edit Date:
Log: Slice the 8-bit (852,1556,3) shape video frame into 6 sections and save
'''

#Installing dependencies#
import os
import cv2 as cv
Home = os.getcwd()

#Read in the exported file#
for folders in os.listdir(Home):
    if '.py' not in folders: #ignore this python file itself
        folder_path = Home+'/%s'%folders
        print(folder_path)
        #operating each folder's image data
        frame_number = 0
        for image in os.listdir(folder_path):
            image_frame = cv.imread(folder_path+'/%s'%image) #read in the image frames in terms of numpy array
            
            '''Slice each image frame (852,1156,3) into six sections of (512,512,3), horizontal-slide-window = 0 and vertical-slide-window = 300'''
            section1 = image_frame[:512,:512,:]
            section2 = image_frame[:512,512:512*2,:]
            section3 = image_frame[:512,512*2:512*3,:]
            #print(section2.shape,section3.shape)
            section4 = image_frame[300:812,:512,:]
            section5 = image_frame[300:812,512:512*2,:]
            section6 = image_frame[300:812,512*2:512*3,:]
            #print(section4.shape,section5.shape,section6.shape)
            
            '''Store each section into their corresponding new_folder'''
            sections = [section1,section2,section3,section4,section5,section6]
            for id in range(len(sections)):
                subpath = folder_path+'/section%s'%(id+1)
                if not os.path.exists(subpath):
                    os.makedirs(subpath)
                else:
                    path_frame = subpath+'/sec%s_%s.png'%(id+1,frame_number)
                    cv.imwrite(path_frame,sections[id])
            frame_number += 1
            print('The %sth image of %s was sliced!'%(frame_number,folders))