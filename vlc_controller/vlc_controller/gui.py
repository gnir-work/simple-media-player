import PySimpleGUI as sg


def popup_message(message: str, timeout: int):
    """
    A small GUI popup message.
    @param message: The message string
    @param timeout: The timeout before the message disappears in seconds.
    """
    layout = [[sg.Text(message)]]
    window = sg.Window(
        "Popup",
        layout,
        no_titlebar=True,
        keep_on_top=True,
        font=("Arial", 35, "italic"),
    )

    while True:
        _, _ = window.read(timeout=1000 * timeout)
        break

    window.close()
