# dataVisualEditor
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


Cross-platform data visualization editing tool based on file manipulation
Zhao hangtian
Usage: generate(s) and sync(s) the data_file.npy and data_file folders in the same directory.
Command:
Python visualEditor. Py [data_file] g
Python visualEditor. Py [data_file] s
0. Priceless data, please do a good backup!
Generate: read data_file.npy and generate pictures in the data_file folder.Please do not change the name of the image in this directory.
2. Sync: according to the remaining images in the folder data_file as index, sync to data_file.npy.
3. Please generate before sync.


sample five.npy added. try it for fun!