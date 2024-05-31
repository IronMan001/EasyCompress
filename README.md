# EasyCompress
v1.0 版本 ,压缩jpg和png。 png的压缩率目前不高。jpg的压缩率还不错

主要是用的是python3.8

# conda
```
opencv                    4.6.0            py38h9991a6c_5    defaults
pillow                    10.3.0                   pypi_0    pypi
python                    3.8.19               h5ee71fb_0    defaults
tk                        8.6.14               h4d00af3_0    defaults
```
# 使用清华源 和阿里源
自己搜一下，经常变

pillow用的是 阿里源。
```
pip -i 自定义阿里源 pillow
```
# 打包平台
pyinstaller

  ###  命令
```
pyinstaller compress.py 
```
打包后的文件，就在 dist目录下.

Mac平台打包出来的是Mac的程序，windows平台，打包的就是exe

重新打包的话，可以直接删除dist文件夹，或者 
```
pyinstaller -w compress.py 
```



