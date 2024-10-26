# -*- coding: utf-8 -*-
import random
from time import sleep
from tqdm import tqdm

def random_one():
    # 读取文件的示例
    try:
        jdt = False
        with open("../docs/fes.data", "r", encoding="utf-8") as fp_fes:
            fp_fes_list = fp_fes.readlines()

        my_list = []

        num = random.random()
        if num < 0.025:  # 2.5%的概率输出“彩色”
            my_list.append(random.choice(fp_fes_list).strip())
        elif num < 0.205:  # 18%的概率输出“金色”
            my_list.append("金")
            have_color = True
        else:  # 79.5%的概率输出“银色”
            my_list.append("银")

        my_list_1 = set(my_list)
        with open("../docs/ihave.data", "r", encoding="utf-8") as fp_fes:
            fp_fes_list = {line.strip() for line in fp_fes.readlines()}

        if not my_list_1 <= fp_fes_list:
            unique_elements = my_list_1 - set(fp_fes_list)
            elements_to_write = "\n".join(unique_elements)
            with open("../docs/ihave.data", "a", encoding="utf-8") as fp_ihave:
                fp_ihave.write(elements_to_write + "\n")  # 添加换行符以分隔追加的内容
            jdt = True

        return my_list, jdt

    except Exception as e:
        print(f"发生错误: {e}")