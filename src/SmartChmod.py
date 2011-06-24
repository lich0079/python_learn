
# coding:utf-8
import os
import stat
path = "/Users/lich0079/Music"


def chmod1():
    for root, dirs, files in os.walk(path):
        for file in files:
            if(not file[0] == "."):
                fp = os.path.join(root, file)   #生成完整路径
                print fp
                # 在原来的权限基础上加上 g+r o+r
                os.chmod(fp, stat.S_IMODE(os.stat(fp)[stat.ST_MODE]) | stat.S_IRGRP | stat.S_IROTH)
        for dir in dirs:
            if(not dir[0] == "."):  # 这句话没有起作用  因为walk自己还是会遍历到.dir下面去
                dp = os.path.join(root, dir)
                print dp
                os.chmod(dp, stat.S_IMODE(os.stat(dp)[stat.ST_MODE]) | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
                # visit(os.path.join(root, dir))   walk方法自己会去递归遍历子目录 不要加这句

def visit(path):
    for file in os.listdir(path):
        fp = os.path.join(path, file)
        if os.path.isdir(fp):
            print 'dir  ' + fp
            removeor(fp);removeox(fp)
            visit(fp)
        elif os.path.isfile(fp):
            print 'file ' + fp
            removeor(fp)
        else:
            print '---- ' + fp

def removeox(path):
    os.system('chmod o-x "' + path + '"')

def removeor (path):
    os.system('chmod o-r "' + path + '"')

def chmod2(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if(file[0] == "."):
                fp = os.path.join(root, file)   #生成完整路径
                print fp
                removeor(fp)
        for dir in dirs:
            if(dir[0] == "."):  # 这句话没有起作用  因为walk自己还是会遍历到.dir下面去
                dp = os.path.join(root, dir)
                print dp
                removeor(dp);removeox(dp)
                visit(dp)
chmod2(path)
