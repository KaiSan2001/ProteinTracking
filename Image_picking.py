'''
Author: Kai San Chan
Starting Date: 2023/02/21
Last Edit Date:
Log: Pick the image frames from sliced folder with an interval of 15 so that a more uniform dataset can be provided to help the model learn a broader landscape of the growing activity
'''

#Installing dependencies#
import os
import cv2 as cv
Home = os.getcwd()

picked_path = Home+'/PickedImages'
if not os.path.exists(picked_path):
    os.makedirs(picked_path)

#Picking the images#
Homedir = os.listdir(Home)
Homedir.remove('PickedImages') #ignore the empty file
for folders in Homedir:
    if '.py' not in folders: #ignore the python files
        for i in range(1,7):
            path_to_folders = Home+'/%s/section%s'%(folders,i)
            for id in range(1,len(os.listdir(path_to_folders)),15):
                image_name = path_to_folders+'/sec%s_%s.png'%(i,id)
                #print(image_name)
                picked_image = cv.imread(image_name)
                saved_path = picked_path+'/%s_sec%s_%s.png'%(folders,i,id)
                #print(saved_path)
                cv.imwrite(saved_path,picked_image)
                print('The %sth image of %s was picked and saved'%(id,folders))