import cv2
import numpy as np
import ffpyplayer
#ffpyplayer for playing audio
from ffpyplayer.player import MediaPlayer
video_path="D:\Jarvis project\WELCOME BACK SIR - J.A.R.V.I.S 4K UHD _shorts(1080P_HD).mp4"
def welcomebacksir(video_path):
    video=cv2.VideoCapture(video_path)
    player = MediaPlayer(video_path)
    while True:
        grabbed, frame=video.read()
        audio_frame, val = player.get_frame()
        if not grabbed:
            print("End of video")
            break
        if cv2.waitKey(30) & 0xFF == ord("q"):#video duration speed ki idhi adjust according to video length
            break

            # 0xFF==ord("q") press q to quit from video

        cv2.imshow("Video", frame)
        if val != 'eof' and audio_frame is not None:
            #audio
            img, t = audio_frame
    video.release()
    cv2.destroyAllWindows()
#PlayVideo(video_path) calling function
#call the above code in face recogition with jarvis code