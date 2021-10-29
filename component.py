from dash import dcc, html
import dash_bootstrap_components as dbc
from pprint import pprint

import util
import plot


def app_upload():
    return html.Div([
        # dcc.Upload(html.Button('Upload File', className="btn btn-warning")),
        #
        # html.Hr(),
        dcc.Upload(
            id='upload-data',
            children=[
                html.H5('Drag and Drop or '),
                html.A(html.H5('Select a File'))
            ],
            style={
                'width': '100%',
                'height': '70px',
                'lineHeight': '60px',
                'borderWidth': '2px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center'
            },
            multiple=True
        )
    ])


def app_headers(data=None):
    if data is None:
        return dbc.Row(
            [
                html.H1('General Info'),
                html.H3('Upload a LabelStudio JSON file to analyse.'),
            ],
            className='mb-5'
        )
    else:
        height = 2048
        width = 2048
        label_types = ["asdf", "asdf"]
        label_names = ["axcv", "xdfg"]
        return dbc.Row(
            [
                html.H1('General Info'),
                html.H3(f"Image Size (H x W) = {height} x {width}"),
                html.H3(f"Label Types = {label_types}"),
                html.H3(f"Label Names = {label_names}"),
            ],
            className='mb-5'
        )

def plot_container(plot_element, data=None):
    options = util.dropdown_options(plot_element, data)
    pprint(vars(plot_element))
    print(options)
    return html.Div([
        html.H1(plot_element.title),
        dcc.Dropdown(f"{plot_element.id}-dropdown", options, options[0]['value']),
        dcc.Graph(f"{plot_element.id}-plot", className="ratio ratio-4x3")
    ])


def app_content(data=None):
    return dbc.Row(
        [dbc.Col(plot_container(el, data), lg=6) for el in plot.plot_elements()]
    )


def app_container(data=None):
    return html.Div(
        [
            dbc.Container(
                [
                    html.Div(app_upload(), id="app-upload"),
                    html.Div(app_headers(), id="app-headers"),
                    html.Div(app_content(), id="app-body-content")
                ],
                fluid=True,
                className='px-5 py-5'
            ),
            dcc.Store("memory-labels"),
        ]
    )