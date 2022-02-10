from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont
import os


main_window = Tk()

# ------ CONSTANTS
# --- COLORS
BACKGROUND_COLOR = "#FCF8E8"
COLOR_2 = "#D4E2D4"
COLOR_3 = "#ECB390"
COLOR_4 = "#DF7861"
# --- FONTS
FONT_NAME = "Quicksand"
# --- FONT SIZES
TITLE_FONT_SIZE = 35
BUTTON_FONT_SIZE = 15
DEFAULT_WATERMARK_SIZE = StringVar(main_window)
DEFAULT_WATERMARK_SIZE.set("30")
WATERMARK_OPACITY_OPTIONS = ["25%", "50%", "75%", "100%"]
# --- WINDOW SIZE
MAIN_WINDOW_HEIGHT = 430
MAIN_WINDOW_WIDTH = 600
# --- MODIFIED FILE PATH
FILE_PATH = str()


def preview_image(save=False):
    global FILE_PATH
    # get watermark size from user input
    font_size = int(watermark_font_size.get())
    # set watermark font (default font type)
    watermark_font = ImageFont.truetype("Quicksand-Medium.ttf", font_size)
    # get watermark text from user input
    watermark = watermark_text.get()
    opacity = int((int(opacity_level.get()[:-1]) * 255) / 100)
    # open image file user selected
    try:
        with Image.open(FILE_PATH).convert("RGBA") as image:
            # add watermark to image
            watermark_image = Image.new("RGBA", image.size, (255, 255, 255, 0))
            write_watermark = ImageDraw.Draw(watermark_image)
            # get watermark dimensions including font type and size
            watermark_text_width, watermark_text_height = write_watermark.textsize(watermark, watermark_font)
            # get user loaded image size
            image_width, image_height = image.size
            # get watermark placement from radio buttons
            radio_button_choice = watermark_position_radio_buttons.get()
            # set default watermark placement (middle of the picture), if user won't choose any radio button
            watermark_placement = ((image_width / 2) - (watermark_text_width / 2),
                                   (image_height / 2) - (watermark_text_height / 2))
            # top left
            if radio_button_choice == 1:
                watermark_placement = (10, 10)
            # top right
            elif radio_button_choice == 2:
                watermark_placement = (image_width - watermark_text_width - 10, 10)
            # bottom left
            elif radio_button_choice == 3:
                watermark_placement = (10, image_height - watermark_text_height)
            # bottom right
            elif radio_button_choice == 4:
                watermark_placement = (image_width - watermark_text_width - 10, image_height - watermark_text_height)
            write_watermark.text(watermark_placement, text=watermark, font=watermark_font,
                                 fill=(255, 255, 255, opacity))
            final_image = Image.alpha_composite(image, watermark_image)
            # if user click on "Preview Image" only show image in viewer,
            # but if user chooses to save, save with "_watermark" suffix to name and show prompt
            if save is not True:
                final_image.show()
            if save is True:
                # split original path from file extension
                path, extension = os.path.splitext(FILE_PATH)
                # extract only file name
                original_file_name = path.split("/")[-1]
                # add "_watermark" suffix to original file name
                new_file_name = original_file_name + "_watermark.png"
                # prepare full save path
                save_path = path.replace(original_file_name, new_file_name)
                final_image.save(save_path)
                # show prompt
                messagebox.showinfo("Save Complete", "File saved successfully!")
    # if file is not chosen throw an error
    except AttributeError:
        messagebox.showinfo("Error", "Please choose file first!")


def choose_image():
    global FILE_PATH
    # possible file extensions to open
    file_types = [("Image files", ("*.jpg", "*.jpeg", "*.png"), ), ('All files', '*')]
    # show file explorer
    file_selection = filedialog.Open(initialdir="/home/mg/Downloads", filetypes=file_types)
    FILE_PATH = file_selection.show()


# ------ MAIN WINDOW LAYOUT
main_window.title("Watermarking App")
main_window.config(padx=0, pady=0, bg=BACKGROUND_COLOR)
main_window.minsize(width=MAIN_WINDOW_WIDTH, height=MAIN_WINDOW_HEIGHT)
# --- MIDDLE
main_canvas = Canvas(main_window, width=600, height=100, bg=BACKGROUND_COLOR, highlightthickness=0)
main_canvas.create_text(300, 50, text="Watermarking App", fill=COLOR_4, font=(FONT_NAME, TITLE_FONT_SIZE, "bold"))
# --- LEFT
# TEXT
watermark_text_label = Label(main_window, text="Watermark text", bg=BACKGROUND_COLOR, fg=COLOR_4,
                             font=(FONT_NAME, BUTTON_FONT_SIZE, "bold"))
watermark_text = Entry(main_window, bg=COLOR_3, fg=BACKGROUND_COLOR, font=(FONT_NAME, BUTTON_FONT_SIZE,),
                       highlightcolor=COLOR_4)
# POSITION
watermark_position_label = Label(main_window, text="Watermark position", bg=BACKGROUND_COLOR, fg=COLOR_4,
                                 font=(FONT_NAME, BUTTON_FONT_SIZE, "bold"))
watermark_position_radio_buttons = IntVar()
radio_button_1 = Radiobutton(text="Top left", value=1, variable=watermark_position_radio_buttons, bg=BACKGROUND_COLOR,
                             fg=COLOR_4, font=(FONT_NAME, 12,), highlightthickness=0, activebackground=BACKGROUND_COLOR)
radio_button_2 = Radiobutton(text="Top right", value=2, variable=watermark_position_radio_buttons, bg=BACKGROUND_COLOR,
                             fg=COLOR_4, font=(FONT_NAME, 12,), highlightthickness=0, activebackground=BACKGROUND_COLOR)
radio_button_3 = Radiobutton(text="Bottom left", value=3, variable=watermark_position_radio_buttons,
                             bg=BACKGROUND_COLOR, fg=COLOR_4, font=(FONT_NAME, 12,), highlightthickness=0,
                             activebackground=BACKGROUND_COLOR)
radio_button_4 = Radiobutton(text="Bottom right", value=4, variable=watermark_position_radio_buttons,
                             bg=BACKGROUND_COLOR, fg=COLOR_4, font=(FONT_NAME, 12,), highlightthickness=0,
                             activebackground=BACKGROUND_COLOR)
# SIZE
watermark_font_size_label = Label(main_window, text="Watermark size", bg=BACKGROUND_COLOR, fg=COLOR_4,
                                  font=(FONT_NAME, BUTTON_FONT_SIZE, "bold"))
watermark_text.insert(END, "Sample watermark")
watermark_font_size = Spinbox(main_window, from_=1, to=100, width=3, bg=COLOR_3, fg=BACKGROUND_COLOR,
                              font=(FONT_NAME, BUTTON_FONT_SIZE,), highlightcolor=COLOR_4,
                              textvariable=DEFAULT_WATERMARK_SIZE)
# OPACITY
watermark_opacity_level_label = Label(main_window, text="Opacity level", bg=BACKGROUND_COLOR, fg=COLOR_4,
                                      font=(FONT_NAME, BUTTON_FONT_SIZE, "bold"))
opacity_level = StringVar()
opacity_level.set("100%")
watermark_opacity_level_menu = OptionMenu(main_window, opacity_level, *WATERMARK_OPACITY_OPTIONS)
watermark_opacity_level_menu.config(bg=COLOR_3, fg=BACKGROUND_COLOR, font=(FONT_NAME, BUTTON_FONT_SIZE,),
                                    highlightthickness=0, activebackground=BACKGROUND_COLOR)

# --- RIGHT
open_file_button = Button(main_window, text="Choose file", bg=COLOR_3, fg=BACKGROUND_COLOR, command=choose_image,
                          font=(FONT_NAME, BUTTON_FONT_SIZE, ""))
preview_image_button = Button(main_window, text="Preview Image", bg=COLOR_3, fg=BACKGROUND_COLOR,
                              command=preview_image, font=(FONT_NAME, BUTTON_FONT_SIZE, ""))
save_image_button = Button(main_window, text="Save Image", bg=COLOR_3, fg=BACKGROUND_COLOR,
                           command=lambda: preview_image(save=True), font=(FONT_NAME, BUTTON_FONT_SIZE, ""))

# ------ POSITIONS
# --- LEFT SIDE
main_canvas.place(x=10, y=0)
watermark_text_label.place(x=10, y=100)
watermark_text.place(x=10, y=130)
watermark_position_label.place(x=10, y=170)
radio_button_1.place(x=10, y=200)
radio_button_2.place(x=10, y=220)
radio_button_3.place(x=10, y=240)
radio_button_4.place(x=10, y=260)
watermark_font_size_label.place(x=10, y=290)
watermark_font_size.place(x=10, y=320)
watermark_opacity_level_label.place(x=10, y=360)
watermark_opacity_level_menu.place(x=10, y=390)

# --- RIGHT SIDE
open_file_button.place(x=MAIN_WINDOW_WIDTH - 138, y=125)
preview_image_button.place(x=MAIN_WINDOW_WIDTH - 173, y=175)
save_image_button.place(x=MAIN_WINDOW_WIDTH - 146, y=225)

main_window.mainloop()
