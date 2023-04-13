import os
import hashlib
import shutil
from tqdm import tqdm

# A, B, C文件夹路径
dir_A = input("输入旧版本路径")
dir_B = input("输入新版本路径")
dir_C = input("输入补丁的路径")

# 获取A文件夹中所有文件的相对路径和MD5值
files_A = {}
for root, dirs, files in os.walk(dir_A):
    for filename in tqdm(files, desc=f"Processing files in {dir_A}"):
        filepath = os.path.join(root, filename)
        relpath = os.path.relpath(filepath, dir_A)
        with open(filepath, "rb") as f:
            hash_md5 = hashlib.md5(f.read()).hexdigest()
        files_A[relpath] = hash_md5

# 遍历B文件夹中所有文件，如果与A文件夹中相同的文件MD5值不同，则拷贝到C文件夹
for root, dirs, files in os.walk(dir_B):
    for filename in tqdm(files, desc=f"Comparing files in {dir_B}"):
        filepath = os.path.join(root, filename)
        relpath = os.path.relpath(filepath, dir_B)
        with open(filepath, "rb") as f:
            hash_md5 = hashlib.md5(f.read()).hexdigest()
        if relpath not in files_A or hash_md5 != files_A[relpath]:
            dstpath = os.path.join(dir_C, relpath)
            dstdir = os.path.dirname(dstpath)
            if not os.path.exists(dstdir):
                os.makedirs(dstdir)
            shutil.copy2(filepath, dstpath)

# 遍历B文件夹中所有文件，将A文件夹中没有的文件拷贝到C文件夹
for root, dirs, files in os.walk(dir_B):
    for filename in tqdm(files, desc=f"Copying new files to {dir_C}"):
        filepath = os.path.join(root, filename)
        relpath = os.path.relpath(filepath, dir_B)
        if relpath not in files_A:
            dstpath = os.path.join(dir_C, relpath)
            dstdir = os.path.dirname(dstpath)
            if not os.path.exists(dstdir):
                os.makedirs(dstdir)
            shutil.copy2(filepath, dstpath)
