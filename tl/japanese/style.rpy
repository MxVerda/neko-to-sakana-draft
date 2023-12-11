translate japanese python:
    gui.system_font = gui.main_font = gui.text_font = gui.name_text_font = gui.interface_text_font = gui.button_text_font = gui.choice_button_text_font = "SourceHanSansLite.ttf"

# To make the furigana in Ruby appear small and over kanji.

style ruby_style is default:
    size 25
    yoffset -40 

style say_dialogue:
    line_leading 12
    ruby_style style.ruby_style

style history_text:
    line_leading 12
    ruby_style style.ruby_style