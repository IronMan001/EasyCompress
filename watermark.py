# -*- coding: utf-8 -*-
import cv2
import numpy as np

fn = "test1.jpg"
if __name__ == '__main__':
    print('loading... %s' % fn)
    print(u'正在处理中')
    img = cv2.imread(fn)
    w = img.shape[1]
    h = img.shape[0]

    cv2.putText(img, "Hello World", (2, 20), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 0), thickness=2)

    cv2.namedWindow('watermark')
    cv2.imshow('watermark', img)
    cv2.waitKey()
    cv2.destroyAllWindows()

