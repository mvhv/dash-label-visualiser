import dash
import dash_bootstrap_components as dbc

import callback
import component


def init_app():
    """Initialise the Dash server, build layout and bind callbacks"""
    app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])  # initialising dash app
    app.layout = component.app_container()
    callback.bind_all(app)
    return app


if __name__ == '__main__':
    app = init_app()
    app.run_server(debug=True)
