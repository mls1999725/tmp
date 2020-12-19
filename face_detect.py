import os
import cv2 as cv

def face_detect_demo(image):
    # 将图片转换为灰度图
    # gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # 加载特征数据
    face_detector = cv.CascadeClassifier(os.path.join(cv.data.haarcascades, 'haarcascade_frontalface_default.xml'))
    faces = face_detector.detectMultiScale(image)
    for x, y, w, h in faces:
        cv.rectangle(image, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)

cap = cv.VideoCapture(0)
i = 0
while(True):
    # 读取图片，路径不能含有中文名，否则图片读取不出来
    # image = cv.imread('face.jpg')
    ret, frame = cap.read()
    face_detect_demo(frame)

    cv.imwrite('face_detect_{}.jpg'.format(i), frame)
    # 显示图片
    # cv.imshow('image', image)

    # 等待键盘输入，单位是毫秒，0表示无限等待
    # cv.waitKey(0)
    i = i + 1
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# 因为最终调用的是C++对象，所以使用完要释放内存
cv.destroyAllWindows()
