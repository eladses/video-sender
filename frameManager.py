import cv2

class FrameManager():

    def __init__(self, video):
        self.cap = cv2.VideoCapture(video)
        self.frame = None
        self.frame_namber = -1
    
    def __del__(self):
        self.cap.release()
        cv2.destroyAllWindows()

    def next_frame(self):
        if(self.cap.isOpened()):
            ret, self.frame = self.cap.read()
            if ret:
                self.resize_frame(factor=0.125)

                self.frame_namber+=1
            return ret
        else:
            return 0

    def get_frame(self):
        return self.frame
    
    def get_frame_number(self):
        return self.frame_namber
    
    def resize_frame(self, factor = 0.25, interpolation = cv2.INTER_CUBIC):
        if factor > 0:
            self.frame = cv2.resize(self.frame, (0,0), fx = factor, fy = factor, interpolation = interpolation) 

if __name__=="__main__":
    fm = FrameManager("../data/street.mp4")

    # Loop until the end of the video
    while (fm.next_frame()):
        fm.resize_frame(0.25)
        
        # Display the resulting frame
        print(fm.get_frame_number())
        cv2.imshow('Frame', fm.get_frame())
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    del(fm)
