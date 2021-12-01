# IPython Interactions
import ipywidgets as wg
from IPython.display import display
from glob import glob
import os

import ana
from ana.functions import timing

global meas

search_str = lambda m_type: os.sep.join(['%s', '%s', '%s*', '*']) if m_type in ['MFN'] else \
                            os.sep.join(['%s', '%s', '*'])

def get_meas_numbers(datadir, m_type):
    """
    Args:
        datadir:
        m_type:
    """
    meas_numbers = [folder.split('/')[-1].split('_')[0] for folder in glob(
                                        '%s/%s/m[0-9.]*' % (
                                            datadir,
                                            m_type))]
    meas_numbers.sort()
    return meas_numbers

def get_new_meastypes(*args):
    """
    Args:
        *args:
    """
    meas_types = [folder.split('/')[2] for folder in glob('%s/*/' % choose_datadir.value)]
    if not len(meas_types):
        display_filename.value = 'Error: Data Dir does not exist!'
        return
    choose_type.options=meas_types
    get_new_numbers(choose_type.value)

def get_new_numbers(*args):
    """
    Args:
        *args:
    """
    meas_numbers = get_meas_numbers(choose_datadir.value, choose_type.value)
    choose_number.options=meas_numbers
    if choose_type.value == 'MFN':
        choose_meas_class.value = 'DAQ'
    elif choose_type.value == 'Hloop':
        choose_meas_class.value = 'HLoop'
    elif choose_type.value == 'SR785':
        choose_meas_class.value = 'Signal Analyzer'

def update_filename(*args):
    """
    Args:
        *args:
    """
    m_type = choose_type.value
    filename = [fn.split('/')[-1] for fn in glob(search_str(m_type) % (choose_datadir.value, 
                                                               m_type,
                                                               choose_number.value))]
    if filename:
        update_info(filename[0])
        display_filename.value = filename[0]

@timing
def load_file(*args):
    """
    Args:
        *args:
    """
    button_widget.button_style = 'warning'

    m_type = choose_type.value
    m_no = choose_number.value
    meas = None
    filename = search_str(m_type) % (choose_datadir.value, 
                                                    m_type,
                                                    m_no)
    lof_files = glob(filename)
    meas_class = choose_meas_class.value
    if meas_class == 'DAQ':
        meas = ana.MFN(lof_files)
    elif meas_class == 'RAW':
        meas = ana.RAW(lof_files)
    elif meas_class == 'Signal Analyzer':
        meas = ana.SA(lof_files)
    elif meas_class == 'HLoop':
        meas = ana.Hloop(lof_files)

    if not meas:
        display_filename.value = 'Error: Can not load measurement!'
        button_widget.button_style = 'danger'
    else:
        button_widget.button_style = 'success'
        button_show.disabled = False

right_widgets = wg.VBox([])
def update_info(filename):
    """
    Args:
        filename:
    """
    meas_info = ana.measurement.MeasurementClass().get_info_from_name(filename)
    right_widgets.children = tuple()
    right_widgets.children += (wg.HTML("<h2>Measurement Info</h2>"),)
    for key, val in meas_info.items():
        right_widgets.children += (wg.Text(str(val), description=str(key).capitalize()),)

def show_meas(*args):
    """
    Args:
        *args:
    """
    meas.plot_info()


choose_datadir = wg.Text('/notebooks/ana/data', description='Data Dir:')
meas_types = [folder.split(os.sep)[-2] for folder in glob(os.sep.join(['%s', '*/']) % choose_datadir.value)]
choose_type = wg.Dropdown(options=meas_types, value='MFN', description='Meas Type:')
meas_numbers = get_meas_numbers(choose_datadir.value, choose_type.value)
choose_number = wg.Dropdown(options=meas_numbers, description='Meas Nr.:', value='m491')
choose_meas_class = wg.Dropdown(options=['DAQ', 'HLoop', 'RAW', 'Signal Analyzer'], description='Meas Class:')

# Display Elements
title_widget = wg.HTML('<h1>Load Measurements</h1>')
display_filename = wg.Label('')
button_widget = wg.Button(description='Load', button_style='success')
button_show = wg.Button(description='Show Measurement', button_style='info', disabled=True)
    
update_filename()
# Connect Widgets
choose_datadir.observe(get_new_meastypes)
choose_type.observe(get_new_numbers)
choose_number.observe(update_filename)
button_widget.on_click(load_file)
button_show.on_click(show_meas)

left_widgets = wg.VBox([wg.HTML("<h2>Select Measurement</h2>"),
                        choose_datadir, 
                        choose_type, 
                        choose_number,
                        choose_meas_class,
                       ])
mid_widgets = wg.HBox([left_widgets, right_widgets])

load_layout = wg.VBox([title_widget, 
                       mid_widgets, display_filename, 
                       wg.HBox([button_widget, button_show])
                      ])
display(load_layout)