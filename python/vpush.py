import PySimpleGUI as sg

susunan = [[sg.VPush(),
            sg.Text("UNISKA MAB" ,font=("Helvetica",24)),
            sg.Push()],
            [sg.Push(),
             sg.Text("BANJARMASIN", font=("Courier",18)),
             sg.VPush()]
            ]
window = sg.Window(title="Element Text",
                   layout=susunan,
                   size=(430,200))
window. read()
window. close()