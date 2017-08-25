# Wall_paper
If you ever wondered why the photos on your windows 10 machine lock screen looks so beautiful, but you don't have an option to have them on your desktop, well I had this idea of how to automate a script to do this using batch script but it didn't work since some of the files are too small, square or even not a photo file.

This script aim to automatically load the photos and have only the one with high resolution kept in a seperate folder where you can personalize your wall paper using the windows personalize desktop with a slide show made of the lock screen photos.

this script has four part, first to delete the destination folder useful for schduled script,second part to copy the files from spotlight folder, third to delete the unwanted photos and files last part is to rename it to keep it user friendly, you will need to change the username in "src_dir" and "dest_dir" into your own username (mine is Soran) make sure you check the folders, just in case if your windows version is different and can't find spotlight photos, you may search the web for the proper location of spotlight folder depending on your version as per my windows version 10, this location where i found the photos also you may need to change the destination folder to one you wish, i created a folder inside picture with the name wall-papers.


 ----------------------------------------------------------------
                              Disclaimer
 this software is given as is there are no guarantees that it will
 work properly or it cause to deletion of your files; try to use
 the script with caution, I won't be responsible for any damage or
 loss that may happen when using this script.

------------------------------------------------------------------
