from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage


a =  MonkeyRunner.loadImageFromFile("images/roark_01_01.png")
b =  MonkeyRunner.loadImageFromFile("images/olivia_01_01.png")

print(a.sameAs(b,0.75))