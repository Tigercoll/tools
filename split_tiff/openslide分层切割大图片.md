# openslide分层切割大图片

## 安装openslide

1. [Install OpenSlide](https://openslide.org/download/)
2. `pip install openslide-python`

下载完`openslide`后将其添加到环境变量.

## 简单使用

```python
# 导入模块
import  openslide
filename = 'filepath'
# 打开文件
slide = openslide.OpenSlide(filename)
# 原图分层缩放像素
print(slide.level_dimensions)
# 原图像素,宽高
print(slide.dimensions)
# 原图缩放倍数
print(slide.level_downsamples)
#原图分层数
print(slide.level_count)
# 所有属性
print(slide.properties)
# 关闭
slide.close()
```

## 分层切块DeepZoomGenerator

```python
# 导入模块
import  openslide
from openslide.deepzoom import DeepZoomGenerator
filename =r'C:\Users\Tiger\Desktop\123\Full_Image.tif'
# 打开文件
slide = openslide.OpenSlide(filename)

# slide 读取的 opslide 对象，将对其进行切图
# tile_size 设置切图尺寸
# overlap 两次切图之间的重叠尺寸
# limit_bounds  若最后剩余尺寸不足切图尺寸，False 表示舍弃，True 表示保留

data_gen = DeepZoomGenerator(slide,tile_size=256,overlap=0,limit_bounds=True)


print('生成的层数:', data_gen.level_count)
print('切分成的块数:', data_gen.tile_count)
print('每层尺寸大小:', data_gen.level_dimensions)
print('每层的块数:', data_gen.level_tiles)

slide.close()
```

获取切块

```python
# 将原图缩放到 level 层级对应的尺寸
# 按照前面指定的 tile_size 进取切片，并取 (i, j) 位置对应的 patch，作为返回值
data_devide.get_tile(level, (i,j))
# 需要注意的是 这都是从0开始的

out_dir = r'output_file'
# 获取每层块数
tiles = data_gen.level_tiles
for index, (row,col)  in enumerate(tiles):
    if not os.path.exists(out_dir+'\\'+str(index)):
        os.mkdir(out_dir+'\\'+str(index))
    for i in range(row):
        for j in range(col):
            data_gen.get_tile(index,(i,j)).save('%s/%s_%s.jpeg'%(out_dir+'\\'+str(index),i,j))
```

