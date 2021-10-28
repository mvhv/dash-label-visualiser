import dash
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

import util
import components
from plots import update_h_w_plot, update_area_plot, update_x_y_plot, update_segmentation_plot

def update_body_content(content):
    data = util.parse_upload_data(content)
    return components.app_content(data)


def bind_callbacks(app):
    app.callback(
        Output("h_w_plot", "figure"),
        Input("h_w_dropdown", "value"),
        State("memory-labels", "data"),
    )(update_h_w_plot)

    app.callback(
        Output("x_y_plot", "figure"),
        Input("x_y_dropdown", "value"),
        State("memory-labels", "data"),
    )(update_x_y_plot)

    app.callback(
        Output("area_plot", "figure"),
        Input("area_dropdown", "value"),
        State("memory-labels", "data"),
    )(update_area_plot)

    app.callback(
        Output("segmentation_plot", "figure"),
        Input("segmentation_dropdown", "value"),
        State("memory-labels", "data"),
    )(update_segmentation_plot)

    app.callback(
        Output("app_body_content", "figure"),
        Input("upload_data", "contents")
    )(update_body_content)
    # def update_output(contents, dropdown_value="OD_SANDING_HOSE"):
    #     lab = parse_contents(contents[0])

    #     plot_width_height(dropdown_value, lab)