import pandas as pd

def update_h_w_plot(dropdown_value, data):
    # BB_width = pars['BB_width'][dropdown_value]
    # BB_height = pars['BB_height'][dropdown_value]
    # fig = go.Figure([go.Scatter()])
    df = pd.DataFrame({
        'Bounding Box Width': data["width"],
        'Bounding Box Height': data["height"]
    })
    
    return px.scatter(
        df,
        x='Bounding Box Width',
        y='Bounding Box Height',
        marginal_x='histogram',
        marginal_y='histogram',
        trendline='ols'
    )


def update_x_y_plot(dropdown_value, data):
    # BB_X = pars['BB_x'][dropdown_value]
    # BB_Y = pars['BB_y'][dropdown_value]
    # fig = go.Figure([go.Scatter()])
    df = pd.DataFrame({
        'Bounding Box X': data["x"],
        'Bounding Box Y': data["y"]
    })

    return px.scatter(
        df,
        x='Bounding Box X',
        y='Bounding Box Y',
        marginal_x='histogram',
        marginal_y='histogram',
        trendline='ols'
    )


def update_area_plot(dropdown_value, data):
    # BB_area = pars['BB_area'][dropdown_value]
    df = pd.DataFrame({
        'Bounding Box Area': data["area"]
    })

    return px.histogram(
        df,
        x='Bounding Box Area'
    )


def update_segmentation_plot(dropdown_value, data):
    # BB_area = pars['seg_area'][dropdown_value]
    df = pd.DataFrame({
        'Segmentation Area': BB_area
    })
    
    return px.histogram(df, x='Segmentation Area')