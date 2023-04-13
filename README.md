# FolderComparison
A/B文件夹对比并生成差异化的C文件夹


import os

import hashlib

import shutil

from tqdm import tqdm


获取A文件夹中所有文件的相对路径和MD5值
 
遍历B文件夹中所有文件，如果与A文件夹中相同的文件MD5值不同，则拷贝到C文件夹

遍历B文件夹中所有文件，将A文件夹中没有的文件拷贝到C文件夹
