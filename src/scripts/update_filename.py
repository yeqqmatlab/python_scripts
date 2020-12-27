import os

"""
create by yqq 2019-12-27
python脚本修改文件名称
"""

def rename(dirname):
    filelist = os.listdir(dirname)
    for file in filelist:
        olddir = os.path.join(dirname, file)
        if os.path.isdir(olddir):
            continue
        file_name = os.path.splitext(file)[0]
        file_type = os.path.splitext(file)[1]
        newdir = os.path.join(dirname, file_name.replace(r"@www.java1234.com", "") + file_type)
        os.rename(olddir, newdir)

rename(r"G:\PDF\liunx")