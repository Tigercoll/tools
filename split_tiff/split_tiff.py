import os
import openslide
from openslide.deepzoom import DeepZoomGenerator
import traceback


def split_image(img_path,out_dir,tile_size):
    '''
    :param img_path: 图片路径
    :param out_dir: 输出路径
    :param tile_size: 分块大小
    :return: 长宽像素
    '''
    try:
        # 打开图片
        slide = openslide.open_slide(img_path)
        # 获取原图像素
        height,width = slide.dimensions
        # 根据title_size 分层
        data_gen = DeepZoomGenerator(slide, tile_size=tile_size, overlap=0, limit_bounds=False)
        # 获取每层块数
        tiles = data_gen.level_tiles
        for index, (row, col) in enumerate(tiles):
            out_Folder = out_dir + '\\' + str(index)
            if not os.path.exists(out_Folder):
                os.mkdir(out_Folder)
            for i in range(row):
                for j in range(col):
                    # 保存每层的块数
                    data_gen.get_tile(index, (i, j)).save('%s/%s_%s.jpeg' % (out_Folder, i, j))
                    print('%s/%s_%s.jpeg' % (out_Folder, i, j))
        slide.close()
        # 返回高,宽
        return height,width
    except Exception as e:

        print(traceback.format_exc())






print(split_image(r'C:\Users\Tiger\Desktop\123\Full_Image.tif',r'C:\Users\Tiger\Desktop\page1\outputgg_files',512))



