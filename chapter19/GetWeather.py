# -*- coding:utf-8 -*-

__author__ = 'hzliyong'
import tkinter
import json
import urllib.request

def getCityWeather_RealTime(cityID):
    url = "http://www.weather.com.cn/data/sk/" + str(cityID) + ".html"
    try:
        stdout = urllib.request.urlopen(url)
        weatherInformation = stdout.read().decode('utf-8')

        jsonDatas = json.loads(weatherInformation)

        city = jsonDatas["weatherinfo"]["city"]
        temp = jsonDatas["weatherinfo"]["temp"]
        fx = jsonDatas["weatherinfo"]["WD"]
        fl = jsonDatas["weatherinfo"]["WS"]
        sd = jsonDatas["weatherinfo"]["SD"]
        time = jsonDatas["weatherinfo"]["time"]

        content = "#" + city + "#" + " " + temp + "℃" + fx + fl + " " + "相对湿度" + sd + " " + "发布时间：" + time + '\n'
        twitter = {'image': '', 'message': content}
    except SyntaxError as err:
        print('SyntaxError:' + err.args)
    except:
        print("OtherError:")
    else:
        return twitter
    finally:
        None


def getCityWeatherDetail_AllDay(cityID):
    url = "http://www.weather.com.cn/data/cityinfo/" + str(cityID) + ".html"
    try:
        stdout = urllib.request.urlopen(url)
        weathInformation = stdout.read().decode('utf-8')
        jsonDatas = json.loads(weathInformation)

        city = jsonDatas["weatherinfo"]["city"]
        temp1 = jsonDatas["weatherinfo"]["temp1"]
        temp2 = jsonDatas["weatherinfo"]["temp2"]
        weather = jsonDatas["weatherinfo"]["weather"]
        img1 = jsonDatas["weatherinfo"]["img1"]
        img2 = jsonDatas["weatherinfo"]["img2"]
        ptime = jsonDatas["weatherinfo"]["ptime"]

        content = city + "," + " " + weather + ",最高气温：" + temp2 + " " + ",最低气温：" + temp1 + " " + ",发布时间：" + ptime + '\n\n'
        twitter = {'image': "icon\d" + img1, 'message': content}

    except SyntaxError as err:
        print('SyntaxError:' + err.args)
    except:
        print('OtherError:')
    else:
        return twitter
    finally:
        None


class Window:
    def __init__(self, root):
        self.citys = self.getCitys('city.txt')
        self.root = root
        self.label = tkinter.Label(root, text = '输入城市：')
        self.label.place(x = 5, y = 15)
        self.entryCity = tkinter.Entry(root)
        self.entryCity.place(x = 65, y = 15)
        self.get = tkinter.Button(root, text = '获取天气', command = self.Get)
        self.get.place(x = 230, y = 15)
        self.edit = tkinter.Text(root, width = 300, height = 350)
        self.edit.place(y = 50)

    def getCitys(self, file):
        file = open(file, encoding = 'utf-8')
        city = {}
        for c in file.read().split('|'):
            cn, cc = c.split(",")
            city.update({cn:cc})
        return city

    def Get(self):
        city = self.entryCity.get().encode('utf-8')
        for k in iter(self.citys.keys()):
            if k.endswith(city.decode()):
                CityCode = self.citys[k]
                break
        title_small = '[实时天气]\n'
        twitter = getCityWeather_RealTime(CityCode)
        self.edit.insert(tkinter.END,
                         title_small + twitter['message'] + '\n')
        title_small = '【今日天气】\n'
        twitter = getCityWeatherDetail_AllDay(CityCode)
        self.edit.insert(tkinter.END,
                         title_small + twitter['message'] + '\n')

if __name__ == '__main__':
    root = tkinter.Tk()
    window = Window(root)
    root.minsize(400,445)
    root.mainloop()










