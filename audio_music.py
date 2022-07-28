import random
import os
music_dir_path= "C:\\Users\\kiran\\Music\\music folder"
songs=os.listdir(music_dir_path)#converting songs into list
d=random.choice(songs)#chooses random music
os.startfile(os.path.join(music_dir_path, d))#plays random music


music_dir="C:\\Users\\kiran\\Music\\music folder"
songs1=os.listdir(music_dir)
os.startfile(os.path.join(music_dir, songs1[5]))#plays song no 5 in music player