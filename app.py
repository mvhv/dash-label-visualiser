import numpy as np
import pandas as pd
from skimage import draw as skid
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px

import callbacks
import components


def init_app():
    """Initialise the Dash server, build layout and bind callbacks"""
    app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])  # initialising dash app
    app.layout(components.app_container())
    callbacks.bind_callbacks(app)
    return app


if __name__ == '__main__':
    app = init_app()
    app.run_server(debug=True)







    # options = []
    # # for label_name in pars['label_names']:
    # for label_name in ["OD_test1", "OD_test2", "SG_test3"]:
    #     if label_name.startswith(task):
    #         tmp = {
    #             'label': label_name,
    #             'value': label_name
    #         }

    #         options.append(tmp)
    # return options


# colors = {
#     'background': '#111111',
#     'text': '#7FDBFF'
# }







# def parse_contents(contents):
#     content_type, content_string = contents.split(',')

#     decoded = base64.b64decode(content_string)
#     tmp = decoded.decode('utf-8')
#     tmp = json.loads(tmp)
#     pars = get_pars(tmp)
#     return pars
    # try:
    #     with open(decoded.decode('utf-8')) as f:
    #         labels = json.load(f)
    #         pars = get_pars(labels)
    #     return pars
    # except Exception as e:
    #     print(e)
    #     return html.Div([
    #         'There was an error processing this file.'
    #     ])

# pars = get_pars(labels)

# # BB height vs width
# header_HW = html.H1(id='header_BB_HW',
#                     children='Bounding Box Height vs Width')
# options = make_dropdown_options(task='OD')
# dropdown_HW = html.Div([
#     dcc.Dropdown(id='dropdown_height_width',
#                  options=options,
#                  value=options[0]['value'])
# ])
# plot_HW = dcc.Graph(id='height_width_plot',
#                     className="ratio ratio-4x3")
# HW_div = html.Div(
#     children=[header_HW, dropdown_HW, plot_HW]
# )

# # BB X vs Y
# header_XY = html.H1(id='header_BB_XY',
#                     children='Bounding Box X vs Y')
# options = make_dropdown_options(task='OD')
# dropdown_XY = html.Div([
#     dcc.Dropdown(id='dropdown_XY',
#                  options=options,
#                  value=options[0]['value'])
# ])
# plot_XY = dcc.Graph(id='XY_plot',
#                     className="ratio ratio-4x3")
# XY_div = html.Div(
#     children=[header_XY, dropdown_XY, plot_XY]
# )

# # BB area histogram
# header_BB_area = html.H1(id='header_BB_area',
#                          children='Bounding Box Area')
# # options = make_dropdown_options(task='SG')
# dropdown_BB_area = html.Div([
#     dcc.Dropdown(id='dropdown_BB_area',
#                  options=options,
#                  value=options[0]['value']
#                  )
# ])
# plot_BB_area = dcc.Graph(id='BB_area_plot',
#                          className="ratio ratio-4x3")
# BB_area_div = html.Div(
#     children=[header_BB_area, dropdown_BB_area, plot_BB_area]
# )

# # Segmentation Area Histogram
# header_SG_area = html.H1(id='header_SG_area',
#                          children='Segmentation Area')
# options = make_dropdown_options(task='SG')
# dropdown_SG_area = html.Div([
#     dcc.Dropdown(id='dropdown_SG_area',
#                  options=options,
#                  value=options[0]['value']
#                  )
# ])
# plot_SG_area = dcc.Graph(id='SG_area_plot',
#                          className="ratio ratio-4x3")
# SG_area_div = html.Div(
#     children=[header_SG_area, dropdown_SG_area, plot_SG_area]
# )