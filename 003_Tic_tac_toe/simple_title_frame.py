def simple_title_frame(text):
    """Creates simple frame around statement."""
    text_length = len(text)
    frame_symbol = "#"
    top_bar = ((2 * text_length) * frame_symbol) + "\n"
    middle_bar = frame_symbol + ((int(text_length / 2) - 1) * " ") + text + \
                 ((int(text_length / 2) - 1) * " ") + frame_symbol + "\n"
    bottom_bar = ((2 * text_length) * frame_symbol)
    frame = top_bar + middle_bar + bottom_bar
    return frame
