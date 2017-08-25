import os
from PIL import Image
import shutil

# This script has four part, first to delete the destination folder useful for schduled script,
# second part to copy the files from spotlight folder, third to delete the unwanted photos and files
# last part is to rename it to keep it user friendly,
# you will need to change the username "NAME" in "src_dir" and "dest_dir" into your own username make sure you check the folders, 
# just in case if your windows version is different and can't find
# spotlight photos, you may search the web for the proper location of spotlight folder depending on your version as per my windows v
# vrsion 10, this location where i found the photos also you may need to change the destination folder to one you wish, 
# I created a folder inside picture with the name wall-papers.

src_dir = r"C:\Users\NAME\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets"
# Change "NAME" after C:\Users\ with the one of your computer, and make sure to go to the folder to see teh content

dest_dir = r"C:\Users\Soran\Pictures\wall-papers"
# similarly change "NAME" after C:\NAME\ with the one you have on your pace

J_index = 0

# ----------------------------------------------------------------
#                              Disclaimer
# this software is given as is there are no guarantees that it will
# work properly or it cause to deletion of your files; try to use
# the script with caution, I won't be responsible for any damage or
# loss that may happen when using this script.
#
#------------------------------------------------------------------



#=========[Part: one (Warning)]================
# Make sure the destination folder is empty this part will delete any photos inside
# thus if you like to keep any of your liked photos try to copy them somewhere else
# enjoy...

for files in os.listdir(dest_dir):
    fileName0 = os.path.join(dest_dir, files)
    os.remove(fileName0)


#===========[Part: two]======================
# copying the files from spotlight, note these files are without proper naming i.e. doestn
# end with .jpg; this is why i am deleting the files less than 50Kb as you won't find an HD photo
# with such file size also if you don't delete at this stage it may casue a problem as these files
# may not be pictures and second part will fail.


for fileName in os.listdir(src_dir):
    NameAndPath = os.path.join(src_dir, fileName)
    shutil.copy2(NameAndPath, dest_dir)
    file_size = os.stat(NameAndPath).st_size
    if file_size < 50000:
        os.remove(NameAndPath)


#===========[Part: three]=========================
# in this part i am removing the portrait photos, the smaller than HD photos and the square photos
# just to be safe i added the x < y and x ==y

for fileName2 in os.listdir(dest_dir):
        pictures = os.path.join(dest_dir, fileName2)
        with Image.open(pictures) as im:
            x, y = im.size
        if (x < y) or (x == y) or (x < 1900):
                os.remove(pictures)

#==============[Part: four]=====================
# the last part is simply to rename files in the destination folder, just to keep it neat and user friendly.
# you may use task scheduler to schedule reading new files and get surprised
# if you like any of the photos

for fileName3 in os.listdir(dest_dir):
        pictures = os.path.join(dest_dir, fileName3)
        Name1 = os.path.join(dest_dir, fileName3)
        Name2 = dest_dir + "\\" + "Pic-" + str(J_index) + ".jpg"
        os.rename(Name1, Name2)
        J_index += 1
