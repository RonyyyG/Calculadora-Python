from PySimpleGUI import PySimpleGUI as sg
sg.theme('DarkBlue3')
layout = [
    [sg.Text('', key='nA', font=('Helvetica', 20),
             justification='center', expand_x=True)],
    [sg.Button('1', size=(5, 2)), sg.Button(
        '2', size=(5, 2)), sg.Button('3', size=(5, 2))],
    [sg.Button('4', size=(5, 2)), sg.Button(
        '5', size=(5, 2)), sg.Button('6', size=(5, 2))],
    [sg.Button('7', size=(5, 2)), sg.Button(
        '8', size=(5, 2)), sg.Button('9', size=(5, 2))],
    [sg.Button('0', size=(5, 2)), sg.Button(
        '+', size=(5, 2)), sg.Button('-', size=(5, 2))],
    [sg.Button('*', size=(5, 2)), sg.Button('/', size=(5, 2)),
     sg.Button('C', size=(5, 2))],
    [sg.Text('', size=(5, 2)), sg.Button(
        '=', size=(5, 2)), sg.Text('', size=(5, 2))]
]
janela = sg.Window('Calculadora', layout, size=(200, 400))

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'C':
        janela['nA'].update('')
    elif eventos == '1':
        janela['nA'].update(f"{janela['nA'].get()}1")
    elif eventos == '2':
        janela['nA'].update(f"{janela['nA'].get()}2")
    elif eventos == '3':
        janela['nA'].update(f"{janela['nA'].get()}3")
    elif eventos == '4':
        janela['nA'].update(f"{janela['nA'].get()}4")
    elif eventos == '5':
        janela['nA'].update(f"{janela['nA'].get()}5")
    elif eventos == '6':
        janela['nA'].update(f"{janela['nA'].get()}6")
    elif eventos == '7':
        janela['nA'].update(f"{janela['nA'].get()}7")
    elif eventos == '8':
        janela['nA'].update(f"{janela['nA'].get()}8")
    elif eventos == '9':
        janela['nA'].update(f"{janela['nA'].get()}9")
    elif eventos == '0':
        janela['nA'].update(f"{janela['nA'].get()}0")
    elif eventos == '+':
        janela['nA'].update(f"{janela['nA'].get()}+")
    elif eventos == '-':
        janela['nA'].update(f"{janela['nA'].get()}-")
    elif eventos == '*':
        janela['nA'].update(f"{janela['nA'].get()}*")
    elif eventos == '/':
        janela['nA'].update(f"{janela['nA'].get()}/")
    elif eventos == '=':
        try:
            janela['nA'].update(eval(janela['nA'].get()))
        except:
            janela['nA'].update('Erro')
janela.close()
