import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

import util


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

def app_headers():
    height = 2048
    width = 2048
    label_types = ["asdf", "asdf"]
    label_names = ["axcv", "xdfg"]

    return dbc.Row(
        [
            html.H1('General Info'),
            html.H3(f"Image Size (H x W) = {height} x {width}"),
            html.H3(f"Label Types = {label_types}"),
            html.H3(f"Label Names = {label_names}")
        ],
        className='mb-5'
    )

def plot_container(title, plot_id, dropdown_id, options):
    return html.Div([
        html.H1(title),
        dcc.Dropdown(dropdown_id, options, options[0]['value']),
        dcc.Graph(plot_id, className="ratio ratio-4x3")
    ])


def app_content(data=None):
    options = util.dropdown_options(data)

    return dbc.Row(
        [
            dbc.Col(
                plot_container(
                    title="Bounding Box Height vs Width",
                    plot_id="h_w_plot",
                    dropdown_id="h_w_dropdown",
                    options=options
                ),
                lg=6
            ),
            dbc.Col(
                plot_container(
                    title="Bounding Box X vs Y",
                    plot_id="x_y_plot",
                    dropdown_id="x_y_dropdown",
                    options=options
                ),
                lg=6
            ),
            dbc.Col(
                plot_container(
                    title="Bounding Box Area",
                    plot_id="area_plot",
                    dropdown_id="area_dropdown",
                    options=options
                ),
                lg=6
            ),
            dbc.Col(
                plot_container(
                    title="Segmentation Area",
                    plot_id="segmentation_plot",
                    dropdown_id="segmentation_dropdown",
                    options=options
                ),
                lg=6
            ),
            dcc.State("memory-labels")
        ],
        id="app_body_content"
    )

def app_container():
    return dbc.Container([
            app_upload(),
            app_headers(),
            app_content()
        ],
        fluid=True,
        className='px-5 py-5'
    )