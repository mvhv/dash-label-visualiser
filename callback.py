from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from pprint import pprint
import util
import plot


def bind_all(app):

    for el in plot.plot_elements():
        @app.callback(
            Output(f"{el.id}-plot", "figure"),
            [Input(f"{el.id}-dropdown", "value"),
            Input("memory-labels", "data"),]
        )
        def update_plot(dropdown_value, data):
            if dropdown_value == "NA" or data is None:
                raise PreventUpdate
            else:
                return el.make(dropdown_value, data)

    @app.callback(
        [Output("app-body-content", "children"),
        Output("memory-labels", "data")],
        Input("upload-data", "contents")
    )
    def update_body_upload_content(contents):
        if contents is None:
            raise PreventUpdate
        else:
            data = util.parse_upload_data(contents)
            pprint(data)
            return util.make_body_content(data), data