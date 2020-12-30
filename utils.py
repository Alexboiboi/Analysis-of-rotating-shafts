import h5py
import numpy as np
import pandas as pd

def save_plot_button(fig):
    filetitle = fig.layout.title.text.strip().replace("<br>", " ").replace(" ", "_").replace(",", "")
    f = go.FigureWidget(fig).update_layout(margin_t=20, title_text='')
    out=widgets.Output()
    @out.capture(clear_output=True)
    def on_b_click(b):
        plotfilename = os.path.join(cc.value, filetitle)
        pio.write_image(f, plotfilename + '.' + b.description)
    button_jpg = widgets.Button(icon='save', description = 'jpg', button_style='info', layout=dict(width='auto'))
    button_jpg.on_click(on_b_click)
    button_pdf = widgets.Button(icon='save', description = 'pdf', button_style='success', layout=dict(width='auto'))
    button_pdf.on_click(on_b_click)
    button_svg = widgets.Button(icon='save', description = 'svg', button_style='primary', layout=dict(width='auto'))
    button_svg.on_click(on_b_click)
    cc=widgets.Combobox(value=plotdest, options=[plotdest], layout=dict(width='750px'))
    display(widgets.VBox([widgets.HBox([button_pdf, button_jpg, button_svg, cc]),out]))