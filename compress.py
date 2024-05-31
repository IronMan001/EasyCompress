from tkinter import Tk, Label, Button, Entry, filedialog,messagebox
import cv2
import os
import random,platform
from PIL import Image

def upload_image():
    # file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.webp")])
    file_path = filedialog.askopenfilename()
    if file_path:
        global image_path
        image_path = file_path

        messagebox.showinfo("提示", "上传完成！")

def compress_image():
    # messagebox.showinfo("提示", "333")
    if 'image_path' in globals():
        # messagebox.showinfo("提示", "222")

        imageType = os.path.splitext(image_path)[1][1:]

        image = cv2.imread(image_path,cv2.IMREAD_UNCHANGED)
        # 在这里进行压缩操作，可以根据需要调整大小和其他参数
        # 示例：缩小一半
        # new_image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))
        new_image = image

        if imageType == "jpg":
            quality = 10 #0-100 值越小,图片损失越大
            # 设置压缩参数
            params = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        elif imageType == "png":
            quality = 9 #0-9,值越大,图片损失越大
            # 设置压缩参数
            params = [int(cv2.IMWRITE_PNG_COMPRESSION), quality]
        # messagebox.showinfo("tttt", 'wancheng')


        if platform.system() == "Darwin":  # 判断是否为 Mac 系统
            download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
            saveImagePath = download_dir + os.sep + "image3"
        else:
            saveImagePath = "image2"
        messagebox.showinfo("提示", saveImagePath)
        if not os.path.exists(saveImagePath):
            try:
                os.mkdir(saveImagePath)
            except Exception as e:
                messagebox.showinfo("tishi",e)
                root.destroy()

        # messagebox.showinfo("提示", "5555")

        name = saveImagePath + os.sep + str(random.randint(0, 1000)) + "." + imageType

        messagebox.showinfo("提示", name)
        '''
        if new_image.shape[2] == 4:
            # 创建一个与原图像大小相同但只有 3 个颜色通道的新图像
            new_image = cv2.cvtColor(new_image[:, :, :3], cv2.COLOR_BGR2RGB)
        '''

        cv2.imwrite(name, new_image,params)
        messagebox.showinfo("提示", "压缩完成！")
        root.destroy()


def remove_alpha_cv2(image_path):
    # 读取包含透明度的图片
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    # 如果有透明度通道（4 通道）
    if image.shape[2] == 4:
        # 创建一个与原图像大小相同但只有 3 个颜色通道的新图像
        new_image = cv2.cvtColor(image[:, :, :3], cv2.COLOR_BGR2RGB)
    else:
        new_image = image
    return new_image

def usePIL():
    if 'image_path' in globals():

        # 打开图像文件
        image = Image.open(image_path)
        # rgb_image = image.convert('RGB')
        # 更改图像质量为80（取值范围为1-95）
        image.save("1.png", quality=1)


# 示例用法
# result_image = remove_alpha_cv2('image_with_alpha.png')
root = Tk()
# root.geometry("400x300")
root.wm_title("压缩缩")
Label(root, text="图片压缩工具").grid(row=0, column=0, columnspan=2)

Button(root, text="上传图片", command=upload_image).grid(row=1, column=0)

Button(root, text="压缩图片", command=compress_image).grid(row=1, column=1)
# Button(root, text="压缩图片", command=usePIL).grid(row=1, column=1)

root.mainloop()