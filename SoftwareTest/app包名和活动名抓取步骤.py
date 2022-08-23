1. 关掉模拟器（安卓手机）所有应用
2. 打开CMD命令，输入adb devices 保证可以显示设备
3. 输入 adb logcat -c 清空日志文件
4. 输入 adb logcat >d:\log.txt
5. 在模拟器（安卓手机）操作你需要测试的app，打开应用和关闭应用
6. 回CMD命令  键盘 Ctrl+C 停止抓取日志
7. 进到D盘找到log.txt文件打开，打开后 Ctrl+f 输入关键字：cmp 点击查找
8. cmp=com.ibox.calculators/.SplashActivity bnds=[76,315][226,499] (has extras)} from pid 2104
     包名：cmp=后面的，/前面的是包名 （com.ibox.calculators）
   活动名： /后空格前 （.SplashActivity）