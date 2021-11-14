#libraries to import

import os
import pytube as pt
import moviepy.editor as mp

# download
url = str (input("Insert your video URL: "))

stream = pt.YouTube(url = url).streams.get_audio_only()
stream.download("mp4")

title = str((stream.title))

# conversion
clip = mp.AudioFileClip("mp4\\" + title + ".mp4")
clip.write_audiofile("mp3\\" + title + ".mp3")

delete = str (input("Delete .mp4 (YES/NO): " ))


# delete .mp4
if delete in "YesYESyes": 
     os.remove("mp4\\" + title + ".mp4")
     print(".mp4 was deleted!")
     
else:
     print(".mp4 was not deleted")
     
     
# Download mp3 format!
