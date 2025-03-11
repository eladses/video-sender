import frameManager, sender
import time
def main():
    frame_namager = frameManager.FrameManager("street.mp4")
    com_namager = sender.CommunicationManager()
    i=0
    t_start=time.time()
    while (frame_namager.next_frame()):
        print(f"frame: {i}, time {time.time()-t_start}")
        i+=1
        com_namager.send_frmae(frame_namager.get_frame())
        if (com_namager.listen()==0):
        # if (i==300):
            break
    print(f"fps: {i/(time.time()-t_start)}")


if __name__=="__main__":
    print("program start")
    main()
    print("program end")
