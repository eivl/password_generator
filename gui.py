from pathlib import Path
from password_generator import generate_password
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def update_dummy() -> None:
    try:
        length = int(entry_1.get())
    except ValueError:
        length = 12
    password = generate_password(length)
    canvas.itemconfig(dummy, text=password)


window = Tk()

window.geometry("1152x700")
window.configure(bg="#0084FF")


canvas = Canvas(
    window,
    bg = "#0084FF",
    height = 700,
    width = 1152,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    576.0,
    0.0,
    1152.0,
    700.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    68.0,
    77.0,
    anchor="nw",
    text="Welcome to a password generator",
    fill="#FFFFFF",
    font=("Roboto Bold", 30 * -1)
)

canvas.create_text(
    83.0,
    173.0,
    anchor="nw",
    text="Please take care and generate a",
    fill="#FFFFFF",
    font=("Roboto", 26 * -1)
)

canvas.create_text(
    83.0,
    203.0,
    anchor="nw",
    text="password for your online stuff.",
    fill="#FFFFFF",
    font=("Roboto", 26 * -1)
)

canvas.create_text(
    83.0,
    233.0,
    anchor="nw",
    text="Default length is 12",
    fill="#FFFFFF",
    font=("Roboto", 26 * -1)
)


canvas.create_text(
    664.0,
    94.0,
    anchor="nw",
    text="Enter the details",
    fill="#000000",
    font=("Roboto Bold", 30 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    836.0,
    224.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#ECE8E8",
    highlightthickness=0
)
entry_1.place(
    x=672.0,
    y=189.0,
    width=328.0,
    height=69.0
)

canvas.create_text(
    665.0,
    165.0,
    anchor="nw",
    text="Password length",
    fill="#000000",
    font=("Roboto Bold", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))


button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: update_dummy(),
    relief="flat"
)
button_1.place(
    x=708.0,
    y=332.0,
    width=230.0,
    height=70.0
)

dummy = canvas.create_text(
    665.0,
    480.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Roboto Bold", 20 * -1),
    width=450,
)

window.resizable(False, False)
window.mainloop()
