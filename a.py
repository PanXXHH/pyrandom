import PySimpleGUI as sg
import random
import pyperclip
import datetime
from Steper_class import Steper
"""
    TODO 急需解决把按钮点击可回车
        bind_return_key
        https://github.com/PySimpleGUI/PySimpleGUI/issues/2176
    TODO 把文件导入导出功能做出来
"""

sg.theme('Topanga')   # Add a touch of color
# All the stuff inside your window.
Asteper = Steper()

randomText = sg.Text('0')
timeText = sg.Text('2022年5月27日 000000')
stepText = sg.Text('1')
treedata = sg.TreeData()
pathText = sg.Text(Asteper.getCurrentPath())
minInputText = sg.InputText("1")
maxInputText = sg.InputText("1")
layout = [[minInputText, sg.Button('生成', k="generate"), maxInputText],
          [randomText, sg.Button('复制', k="copy")],
          [pathText],
          [sg.Button('置步', k="restep"),sg.Button('__dict__', k="print_dict")],
          [timeText],
          [sg.Tree(data=treedata,
                   headings=[])
           ]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'generate':
        ramdomValue = random.randrange(int(values[0]), int(values[1]) + 1)
        randomText.Update(ramdomValue)
        timeText.Update(datetime.datetime.now())
        Asteper.fullAndRemove(int(values[1]) - int(values[0]) + 1)
        Asteper.into(ramdomValue - int(values[0]))
        pathText.Update(Asteper.getCurrentPath())
        if Asteper.length() > 0:
            maxInputText.Update(Asteper.length() - int(values[0]) + 1)
        # print(ramdomValue, Asteper.__dict__())
    elif event == 'copy':
        pyperclip.copy(randomText.get())
    elif event == 'restep':
        Asteper.restep()
        pathText.Update(Asteper.getCurrentPath())
        maxInputText.Update(Asteper.length() - int(values[0]) + 1)
    elif event == 'print_dict':
        print(Asteper.__dict__())
    elif event == sg.WIN_CLOSED or event == 'Cancel':
        break
    # print('You entered ', random.randrange(int(values[0]), int(values[1]) + 1))
    print(event, values)

window.close()
