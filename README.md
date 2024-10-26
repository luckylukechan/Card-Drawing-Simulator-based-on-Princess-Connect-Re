# Card-Drawing-Simulator-based-on-Princess-Connect-Re
# 基于[公主连结]的抽卡模拟器
This system can be used to test the hand of card drawing, written in python, the project language is Chinese.

该系统可用于测试抽卡的手气，用 python 编写，项目语言为中文。


## **---关于文件说明---**

```plaintext
Card-Drawing-Simulator-based-on-Princess-Connect-Re
├── src                         # Python代码文件夹
│   └── main.py                 # 主程序，运行此文件可直接启动抽卡窗口
├── data                        # 项目相关图片资源
├── docs                        # 项目资源保存文件夹，可根据需要进行修改
│   ├── fes.data                # 存放卡池角色（三星）
│   ├── gemstone.data           # 存放钻石数量
│   ├── ihave.data              # 存放已抽取的角色数据
│   └── num.data                # 存放已抽取的数量
```

## **---关于按钮点击---***
```plaintext
可视化界面可操作按钮有四个，分别为单抽（150钻）、十连抽（1500钻）、钻石余量右边的“＋”按
钮可以购买宝石、显示已抽到的角色的按钮
```

## **---关于界面显示---***
```plaintext
单击抽取后，如果有未抽取的（三星）角色，下方的进度条会加载至满后再显示抽到的卡，否则直接显示。
当前抽取三星角色的概率为5%（3★概率加倍），十连抽有保底机制（前9抽为一星（银）时第10抽一定为二星（金）或二星以上（彩））
还有其他的就留给你们慢慢探索吧~~~
```
