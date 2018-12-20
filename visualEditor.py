"""
基于文件操作的跨平台数据可视化编辑工具
作者：zhao hangtian
用法：把data_file.npy和data_file文件夹放在同一目录下，先generate(s)再sync(s)。
命令：
	python visualEditor.py [data_file] g
	python visualEditor.py [data_file] s
0.数据无价，请先做好备份！
1.generate：读取data_file.npy，在data_file文件夹生成图片。根据需要删除文件夹下的图片，请不要更改此目录下的图片文件名。
2.sync：根据文件夹data_file中剩下图片作为index，同步到data_file.npy中。
3.请先执行generate再执行sync。
4.不要连续执行sync，第二次执行sync前应该再generate一次。
"""
import numpy as np
import cv2
import sys
import os
import shutil

if len(sys.argv) != 3:
    print("参数错误！请使用 filename.npy func")
    exit(0)
para = sys.argv

foldName = 'jointsPics\\' + para[1]


def make_path(p):
    if not os.path.exists(p):  # 判断文件夹是否存在
        os.mkdir(p)
    else:
        shutil.rmtree(p)        # 删除文件夹
        os.mkdir(p)


def generate(foldname=foldName):
    load = np.load(foldname + '.npy')
    make_path(foldname)


    ### Modify there to draw your data!
    canvas = np.zeros((300, 300, 3), dtype="uint8")
    maxnum = len(load)
    r = 6
    red = (0, 0, 255)
    blue = (255, 0, 0)
    green = (0, 0, 255)
    yellow = (255, 255, 0)
    Magenta = (255, 0, 255)
    Cyan = (0, 255, 255)
    White = (255, 255, 255)
    for j in range(0, maxnum):
        image = load[j]
        canvas[:, :, :] = 0
        for i in range(0, 21):
            centerX = int(image[i, 1])
            centerY = int(image[i, 0])
            color = (0, 0, 0)
            if (i == 0):
                color = White
            elif (0 < i < 5):
                color = blue
            elif (4 < i < 9):
                color = green
            elif (8 < i < 13):
                color = Cyan
            elif (12 < i < 17):
                color = Magenta
            else:
                color = yellow
            cv2.circle(canvas, (centerX, centerY), r, color, -1)
            if i % 4:
                cv2.line(canvas, (int(image[i, 1]), int(image[i, 0])), (int(image[i + 1, 1]), int(image[i + 1, 0])), color, 2)
            if not ((i-1) % 4):
                cv2.line(canvas, (int(image[i, 1]), int(image[i, 0])), (int(image[0, 1]), int(image[0, 0])), color, 2)
        savefile = foldname + '\\' + str(j) + '.jpg'
        print(savefile)
        cv2.imwrite(savefile, canvas)
    print("成功生成可视化图片\n")

    ### if you want to see instantly.
        # cv2.imshow(str(j), canvas)
        # cv2.waitKey(0)
    # cv2.destroyAllWindows()


def sync(foldname=foldName):
    load = np.load(foldname + '.npy')
    filePath = sys.path[0] + '\\' + foldName + '\\'
    print(filePath)
    K = [k for _, _, k in os.walk(filePath)]
    imgI = [int(i[:-4]) for i in K[0]]
    if len(load) != len(imgI):
        imgI.sort(reverse=True)
        print(imgI)
        print("文件夹图片数量:" + str(len(imgI)))
        print("npy图片数量:" + str(len(load)))
        for i in range(len(load) - 1, -1, -1):
            if i not in imgI:
                print('del: ' + str(i))
                load = np.delete(load, i, 0)
        np.save(foldname + '.npy', load)
        print("成功更新" + foldname + ".npy文件")
    else:
        print("图片数没有更改，没有改动npy")
    print("文件夹图片数量:" + str(len(imgI)))
    print("npy图片数量:" + str(len(load)))


if para[2] == 'generate' or para[2] == 'g':
    generate(foldname=foldName)
elif para[2] == 'sync' or para[2] == 's':
    sync(foldname=foldName)
