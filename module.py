def read_image():
    import cv2 as cv
    img=cv.imread('Photos/cat.jpg')
    cv.imshow('Photo',img)
    cv.waitKey(0)

def read_video():
    import cv2 as cv
    capture=cv.VideoCapture('Videos/dog.mp4')
    while True:
        isTrue,frame=capture.read()
        cv.imshow('Video',frame)
        if cv.waitKey(20)&0xFF==('d'):
          break
    capture.release()
    cv.destroyAllWindows()

def resize():
    import cv2 as cv
    img=cv.imread('Photos/cat.jpg')
    cv.imshow('Cat',img)
    def rescaleFrame(frame,scale=0.75):
        width=int(frame.shape[1]*scale)
        height=int(frame.shape[0]*scale)
        dimensions=(width,height)
        return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
    resized_image=rescaleFrame(img)
    cv.imshow('Resized Cat',resized_image)
    cv.waitKey(0)

def rescale():
    import cv2 as cv
    capture=cv.VideoCapture('Videos/dog.mp4')
    def rescaleFrame(frame,scale=0.75):
        width=int(frame.shape[1]*scale)
        height=int(frame.shape[0]*scale)
        dimensions=(width,height)
        return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

    while True:
       isTrue,frame=capture.read()
       cv.imshow('Dog',frame)
       frame_resized=rescaleFrame(frame)
       cv.imshow('Resized Dog',frame_resized)
       if cv.waitKey(20)&0xFF==('d'):
          break
    capture.release()
    cv.destroyAllWindows()

def blank():
    import cv2 as cv
    import numpy as np
    blank=np.zeros((500,500,3),dtype='uint8')
    cv.imshow('Blank',blank)
    cv.waitKey(0)

def paint():
    import cv2 as cv
    import numpy as np
    blank=np.zeros((500,500,3),dtype='uint8')
    blank[200:300,300:400]=255,0,0
    cv.imshow('Blue',blank)
    cv.waitKey(0)

def rect():
    import cv2 as cv
    import numpy as np
    blank=np.zeros((500,500,3),dtype='uint8')
    cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,0,0),thickness=3)
    cv.imshow('Rectangle',blank)
    cv.waitKey(0)

def circle():
    import cv2 as cv
    import numpy as np
    blank=np.zeros((500,500,3),dtype='uint8')
    cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,255,0),thickness=-1)
    cv.imshow('Circle',blank)
    cv.waitKey(0)

def line():
    import cv2 as cv
    import numpy as np
    blank=np.zeros((500,500,3),dtype='uint8')
    cv.line(blank,(0,0),(300,400),(255,255,255),thickness=3)
    cv.imshow('Line',blank)
    cv.waitKey(0)

def text():
    import cv2 as cv
    import numpy as np
    blank=np.zeros((500,500,3),dtype='uint8')
    cv.putText(blank,'hello',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=3)
    cv.imshow('Text',blank)
    cv.waitKey(0) 


def imagetranslation():
    import numpy as np
    import cv2 as cv
    img = cv.imread('Photos/cat.jpg', 0)
    rows, cols = img.shape
    M = np.float32([[1, 0, 100], [0, 1, 50]])
    dst = cv.warpAffine(img, M, (cols, rows))
    cv.imshow('img', dst)
    cv.waitKey(0)

def imagerotation():
    import numpy as np
    import cv2 as cv
    img = cv.imread('Photos/cat.jpg', 0)
    rows, cols = img.shape
    M = np.float32([[1, 0, 0], [0, -1, rows], [0, 0, 1]])
    img_rotation = cv.warpAffine(img,
	cv.getRotationMatrix2D((cols/2, rows/2),
	30, 0.6),
	(cols, rows))
    cv.imshow('img', img_rotation)
    cv.imwrite('rotation_out.jpg', img_rotation)
    cv.waitKey(0)
    cv.destroyAllWindows()


def image_reflection():
   import numpy as np
   import cv2 as cv
   img = cv.imread('Photos/cat.jpg', 0)
   rows, cols = img.shape
   M = np.float32([[1, 0, 0],
				[0, -1, rows],
				[0, 0, 1]])
   reflected_img = cv.warpPerspective(img, M,
								(int(cols),
									int(rows)))
   cv.imshow('img', reflected_img)
   cv.imwrite('reflection_out.jpg', reflected_img)
   cv.waitKey(0)
   cv.destroyAllWindows()

def image_scaling():
    import numpy as np
    import cv2 as cv
    img = cv.imread('Photos/cat.jpg', 0)
    rows, cols = img.shape
    img_shrinked = cv.resize(img, (250, 200),
						interpolation=cv.INTER_AREA)
    cv.imshow('img', img_shrinked)
    img_enlarged = cv.resize(img_shrinked, None,
						fx=1.5, fy=1.5,
						interpolation=cv.INTER_CUBIC)
    cv.imshow('img_enlarged', img_enlarged)
    cv.waitKey(0)
    cv.destroyAllWindows()
def img_cropping():
    import numpy as np
    import cv2 as cv
    img = cv.imread('Photos/park.jpg', 0)
    cropped_img = img[100:300, 100:300]
    cv.imwrite('cropped_out.jpg', cropped_img)
    cv.imshow('cropped_out.jpg', cropped_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def img_shearing_in_X_axis():
    import numpy as np
    import cv2 as cv
    img = cv.imread('Photos/cat.jpg', 0)
    rows, cols = img.shape
    M = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
    sheared_img = cv.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))
    cv.imshow('img', sheared_img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def img_shearing_yaxis():
  import numpy as np
  import cv2 as cv
  img = cv.imread('Photos/cat.jpg', 0)
  rows, cols = img.shape
  M = np.float32([[1, 0, 0], [0.5, 1, 0], [0, 0, 1]])
  sheared_img = cv.warpPerspective(img, M, (int(cols*1.5), int(rows*1.5)))
  cv.imshow('sheared_y-axis_out.jpg', sheared_img)
  cv.waitKey(0)
  cv.destroyAllWindows()

#Smoothing and blurring
def kernel_blur():
 import cv2
 import numpy as np
 image = cv2.imread('Photos/cat.jpg')
 kernel2 = np.ones((5, 5), np.float32)/25
 img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel2)
 cv2.imshow('Original', image)
 cv2.imshow('Kernel Blur', img)
 cv2.waitKey()
 cv2.destroyAllWindows()

def avg_blur():
 import cv2
 import numpy as np
 image = cv2.imread('Photos/cat.jpg')
 averageBlur = cv2.blur(image, (5, 5))
 cv2.imshow('Original', image)
 cv2.imshow('Average blur', averageBlur)
 cv2.waitKey()
 cv2.destroyAllWindows()
    
def Gaussian_blur():
 import cv2
 import numpy as np
 image = cv2.imread('Photos/cat.jpg')
 gaussian = cv2.GaussianBlur(image, (3, 3), 0)
 cv2.imshow('Original', image)
 cv2.imshow('Gaussian blur', gaussian)
 cv2.waitKey()
 cv2.destroyAllWindows()

def median_blur():
 import cv2
 import numpy as np
 image = cv2.imread('Photos/cat.jpg')
 medianBlur = cv2.medianBlur(image, 9)
 cv2.imshow('Original', image)
 cv2.imshow('Median blur',
medianBlur)
 cv2.waitKey()
 cv2.destroyAllWindows()

def bilateral_blur():
 import cv2
 import numpy as np
 image = cv2.imread('Photos/cat.jpg')
 bilateral = cv2.bilateralFilter(image,
9, 75, 75)
 cv2.imshow('Original', image)
 cv2.imshow('Bilateral blur', bilateral)
 cv2.waitKey()
 cv2.destroyAllWindows()

def bitwise_and():
 import cv2
 import numpy as np
 img1 = cv2.imread('Photos/Input 1.png')
 img2 = cv2.imread('Photos/Input 2.png')
 dest_and = cv2.bitwise_and(img2, img1, mask = None)
 cv2.imshow('Bitwise And', dest_and)
 if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()

def bitwise_or():
 import cv2
 import numpy as np	
 img1 = cv2.imread('Photos/Input 1.png')
 img2 = cv2.imread('Photos/Input 2.png')
 dest_or = cv2.bitwise_or(img2, img1, mask = None)
 cv2.imshow('Bitwise OR', dest_or)
 if cv2.waitKey(0) & 0xff == 27:
  cv2.destroyAllWindows()
def bitwise_xor():
 import cv2 
 import numpy as np    
 img1 = cv2.imread('Photos/Input 1.png')  
 img2 = cv2.imread('Photos/Input 2.png')  
 dest_xor = cv2.bitwise_xor(img1, img2, mask = None)
 cv2.imshow('Bitwise XOR', dest_xor)   
 if cv2.waitKey(0) & 0xff == 27: 
    cv2.destroyAllWindows() 

def bitwise_not():
 import cv2
 import numpy as np	
 img1 = cv2.imread('Photos/Input 1.png')
 img2 = cv2.imread('Photos/Input 2.png')
 dest_not1 = cv2.bitwise_not(img1, mask = None)
 dest_not2 = cv2.bitwise_not(img2, mask = None)
 cv2.imshow('Bitwise NOT on image 1', dest_not1)
 cv2.imshow('Bitwise NOT on image 2', dest_not2)
 if cv2.waitKey(0) & 0xff == 27:
	 cv2.destroyAllWindows()
         
def masking():
 import cv2 as cv
 import numpy as np
 img = cv.imread('Photos/park.jpg')
 cv.imshow('Original image', img)
 blank = np.zeros(img.shape[:2], dtype='uint8')
 cv.imshow('Blank Image', blank)
 circle = cv.circle(blank,
 (img.shape[1]//2,img.shape[0]//2),200,255, -1)
 cv.imshow('Mask',circle)
 masked = cv.bitwise_and(img,img,mask=circle)
 cv.imshow('Masked Image', masked)
 cv.waitKey(0)

def alphablending():
 import cv2

 img1 = cv2.imread('Photos/cat.jpg')
 img2 = cv2.imread('Photos/park.jpg')
 img2 = cv2.resize(img2, img1.shape[1::-1])

 cv2.imshow("img 1", img1)
 cv2.waitKey(0)
 cv2.imshow("img 2", img2)
 cv2.waitKey(0)

 choice = 1
 while choice:
    alpha = float(input("Enter alpha value: "))
    dst = cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)
    cv2.imwrite('alpha_blend.png', dst)
    img3 = cv2.imread('alpha_blend.png')
    cv2.imshow("alpha blending", img3)
    cv2.waitKey(0)
    choice = int(input("Enter 1 to continue and 0 to exit: "))

def histogram_calc():
 import cv2
 from matplotlib import pyplot as plt
 img = cv2.imread('Photos/park.jpg',0)
 histr = cv2.calcHist([img],[0],None,[256],[0,256])
 plt.plot(histr)
 plt.show()














