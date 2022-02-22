import PySimpleGUI as sg


def popup_message(message: str, timeout: int):
    layout = [[sg.Text(message)]]
    window = sg.Window("Demo", layout, no_titlebar=True, keep_on_top=True, font=('Arial', 35, "italic"))

    while True:
        _, _ = window.read(timeout=1000 * timeout)
        break

    window.close()


if __name__ == '__main__':
    popup_message("вы просматриваете эпизод 10", 5)
