# -*- coding: utf-8 -*-
import random
from time import sleep
from tqdm import tqdm


def random_ten():
    try:
        jdt = False
        with open("../docs/fes.data", "r", encoding="utf-8") as fp_fes:
            fp_fes_list = fp_fes.readlines()

        my_list = []
        have_color = False

        for _ in range(10):
            if _ == 9:
                if not have_color:
                    num = random.random()
                    if num < 0.05:
                        my_list.append(random.choice(fp_fes_list).strip())
                    else:
                        my_list.append("金")
                    break

            num = random.random()
            if num < 0.05:
                my_list.append(random.choice(fp_fes_list).strip())
                have_color = True
            elif num < 0.205:
                my_list.append("金")
            else:
                my_list.append("银")

        my_list_1 = set(my_list)
        with open("../docs/ihave.data", "r", encoding="utf-8") as fp_fes:
            fp_fes_list = {line.strip() for line in fp_fes.readlines()}

        if not my_list_1 <= fp_fes_list:
            jdt = True
            unique_elements = my_list_1 - set(fp_fes_list)
            elements_to_write = "\n".join(unique_elements)
            with open("../docs/ihave.data", "a", encoding="utf-8") as fp_ihave:
                fp_ihave.write(elements_to_write + "\n")

        return my_list, jdt  # 返回抽取的结果列表

    except Exception as e:
        print(f"发生错误: {e}")
        return []
