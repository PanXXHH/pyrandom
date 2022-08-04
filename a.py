from os import getcwd
import PySimpleGUI as sg
import random
import datetime
from Steper_class import Steper
"""
    DONE 加载时选中最大值文本
    TODO 把文件导入导出功能做出来
    TODO 优化界面
    TODO 代码优化
    TODO 复制按钮删掉，文本居中
    TODO 缩小放大时选中最大值文本
"""

sg.theme('Topanga')   # Add a touch of color
# All the stuff inside your window.
Asteper = Steper()
randomText = sg.Text('0', size=20, justification='center')
timeText = sg.Text('2022年5月27日 000000')
stepText = sg.Text('1')
treedata = sg.TreeData()
mapText = sg.Text(Asteper.getCurrentPath())
minInputText = sg.InputText("1", size=10)
maxInputText = sg.InputText("1", size=10, focus=True)
layout = [[minInputText, sg.Button('生成', size=5, k="generate", bind_return_key=True), sg.Button('置步', k="restep"), maxInputText],
          [randomText],
          [mapText],
          [sg.Button('__dict__', k="print_dict"), sg.FileBrowse('导入', file_types=(("JSON file", "*.json"), ('All file', '*.*')), initial_folder=getcwd(), k="import"),
           sg.FileSaveAs('导出', file_types=(("JSON file", "*.json"), ('All file', '*.*')), initial_folder=getcwd(), k="export", target="port_path")],
          [timeText]]

# Create the Window
window = sg.Window('Window Title', layout, finalize=True)
maxInputText.Widget.select_range(0, 1)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == 'generate':
        ramdomValue = random.randrange(int(values[0]), int(values[1]) + 1)
        randomText.Update(ramdomValue)
        timeText.Update(datetime.datetime.now())
        Asteper.fullAndRemove(int(values[1]) - int(values[0]) + 1)
        Asteper.into(ramdomValue - int(values[0]))
        mapText.Update(Asteper.getCurrentPath())
        if Asteper.length() > 0:
            maxInputText.Update(Asteper.length() - int(values[0]) + 1)
        maxInputText.SetFocus()
        maxInputText.Widget.select_range(0, len(values[1]))
    elif event == 'restep':
        Asteper.restep()
        mapText.Update(Asteper.getCurrentPath())
        maxInputText.Update(Asteper.length() - int(values[0]) + 1)
    elif event == 'print_dict':
        print(Asteper.__dict__())
    elif event == 'import':
        pass
    elif event == 'export':
        print("explorer")
    elif event == sg.WIN_CLOSED or event == 'Cancel':
        break

    print(event, values)

window.close()
