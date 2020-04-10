import numpy as np
import cv2





def get_ratio_of_different_pixels_between_different_arrays(first_array,second_array):
	size=first_array.size

	difference_array=second_array-first_array
	difference=np.count_nonzero(difference_array)
	difference_ratio=difference/size
	return difference_ratio



def get_ratio_of_equivalent_pixels_between_two_arrays(first_array,second_array):
	return (1-get_ratio_of_different_pixels_between_different_arrays(first_array,second_array))



cap = cv2.VideoCapture(r'C:\Users\Jose-Manuel Jimenez\Documents\projects\python\motion_tracking\test_videos\Dubai - 31956P.mp4')


queue=[]
pair_list=[]

difference_ratio_list=[]

while(cap.isOpened()):
    ret, frame = cap.read()
  

    try:
	    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	    queue.append(frame)

	    if len(queue)>=2:
	    	

	    	difference=get_ratio_of_different_pixels_between_different_arrays(queue[0],queue[1])
	    	difference_ratio_list.append(difference)
	    	
	    	queue.pop(0)


	    if cv2.waitKey(1) & 0xFF == ord('q'):
	        break
    except Exception as e:
    	print(e)
    	break



print(difference_ratio_list)
print(np.var(difference_ratio_list))
cap.release()
cv2.destroyAllWindows()
