import cv2
import numpy as np
import pyautogui as pig


def record():
    cc = cv2.VideoWriter_fourcc(*"XVID")
    sz = pig.size()
    out = cv2.VideoWriter('output.avi', cc, 40.0, sz)

    while(True):
        img = pig.screenshot()
        frame = np.array(img)
        
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        out.write(frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    out.release()
    
record()
