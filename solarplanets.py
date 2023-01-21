import cv2

img=cv2.imread("solar-system.jpg")

cv2.putText(img,"sun",(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"MERCURY",(110,190),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"VENUS",(190,270),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"EARTH",(300,320),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"MARS",(400,270),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"JUPITER",(500,90),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"SATURN",(720,110),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"URANUS",(950,130),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"NEPTUNE",(1080,130),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))

cv2.imshow('output',img)
cv2.waitKey(0)
cv2.imwrite('solar-system',img)