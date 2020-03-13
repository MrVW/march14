import tkinter
import pygeoip
 
class FindLocation(object):
    def __init__(self):
        self.gi = pygeoip.GeoIP("./GeoLiteCity.dat")
        self.root = tkinter.Tk()  # 创建主窗口,用于容纳其它组件
 # 给主窗口设置标题内容
        self.root.title("全球定位ip位置(离线版)")
 # 创建一个输入框,并设置尺寸
        self.ip_input = tkinter.Entry(self.root,width=30)
 
 # 创建一个回显列表
        self.display_info = tkinter.Listbox(self.root, width=50)
 
 # 创建一个查询结果的按钮
        self.result_button = tkinter.Button(self.root, command = self.find_position, text = "查询")
 
 # 完成布局
    def gui_arrang(self):
        self.ip_input.pack()
        self.display_info.pack()
        self.result_button.pack()
 
 # 根据ip查找地理位置
    def find_position(self): # 获取输入信息
        self.ip_addr = self.ip_input.get()
        aim = self.gi.record_by_name(self.ip_addr) # 为了避免非法值,导致程序崩溃,有兴趣可以用正则写一下具体的规则,为了便于新手理解,减少代码量,就直接粗放的过滤了
        try:
            city = aim["city"]   # 获取目标城市
            country = aim["country_name"]# 获取目标国家
            region_code = aim["region_code"]  # 获取目标地区
            longitude = aim["longitude"]  # 获取目标经度
            latitude = aim["latitude"]   # 获取目标纬度
        except:
            pass
  
 # 创建临时列表
        the_ip_info = ["所在纬度:"+str(latitude),"所在经度:"+str(longitude),"地域代号:"+str(region_code),"所在城市:"+str(city), "所在国家或地区:"+str(country), "需要查询的ip:"+str(self.ip_addr)]
 #清空回显列表可见部分,类似clear命令
        for item in range(10):
            self.display_info.insert(0,"") # 为回显列表赋值
        for item in the_ip_info:
            self.display_info.insert(0,item)
        return the_ip_info  # 这里的返回值,没啥用,就是为了好看
 
 
def main():
    FL = FindLocation()  # 初始化对象
    FL.gui_arrang() # 进行布局
    tkinter.mainloop() # 主程序执行
    pass
 
 
if __name__ == "__main__":
    main()
