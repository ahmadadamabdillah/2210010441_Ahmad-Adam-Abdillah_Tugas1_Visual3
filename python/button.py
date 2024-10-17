import PySimpleGUI as sg 
sg.theme("DarkGreen4")
sg.theme_text_color("yellow")
window = sg.Window(title= "Contoh Button",
                   layout=[[sg.Text("Contoh Button")],
                           [sg.Button("Button simpan")],
                           [sg.Button("Button keluar")],
                           ],
                           size=(400,200),
                           font=("Times", 18))
kejadian, nilai = window. read()
print(kejadian, "=>" ,nilai)
window. close()