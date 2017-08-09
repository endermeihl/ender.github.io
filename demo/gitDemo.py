
import os
import subprocess

os.system('git')


def get_branches(project_dir):
    try:
        os.chdir(project_dir)
    except Exception as e:
        print(e)
    branches_str = subprocess.check_output(["git", "branch"])
    # 终端运行“git branch”命令，并且将终端的输出str转存到branches_str里
    print(branches_str)
    branches = branches_str.split('\n')
    # 使用str的split方法将其按照'\n'分割
    branch_list = []
    for branch in branches[0:-1]:
        branch_list.append(branch.lstrip('* '))
        # 使用str的lstrip方法将字符串的前的空格和当前branch前的“*”标记去除
    print(branch_list)
    return branch_list

get_branches('C:/Users/ender/IdeaProjects/gitwebapp/jerryTrainManage')