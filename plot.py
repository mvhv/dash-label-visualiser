import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


class PlotElement():
    def __init__(self, id, title, make, task, data_ids, data_names):
        self.id = id
        self.title = title
        self.make = make
        self.task = task
        self.data_ids = data_ids
        self.data_names = data_names

    def fields(self):
        zip(self.data_names, self.data_ids)
    
    def label_data(self, field_id, label, data):
        return data[field_id][label]

    def df(self, label, data):
        return pd.DataFrame(
            {field_name: self.label_data(field_id) for field_name, field_id in self.fields()}
        )

    def graph_config(self, label, data):
        {
            "df": self.df(label, data),
            "x": self.data_names[0]

        }
    )


def make_h_w_plot(dropdown_value, data):
    if "BB_width" in data and "BB_height" in data:
        x = data['BB_width'][dropdown_value]
        y = data['BB_height'][dropdown_value]
    else:
        x = list()
        y = list()
    # BB_width = pars['BB_width'][dropdown_value]
    # BB_height = pars['BB_height'][dropdown_value]
    # fig = go.Figure([go.Scatter()])
    df = pd.DataFrame({
        'Bounding Box Width': x,
        'Bounding Box Height': y
    })
    
    return px.scatter(
        df,
        x='Bounding Box Width',
        y='Bounding Box Height',
        marginal_x='histogram',
        marginal_y='histogram',
        trendline='ols'
    )


def make_x_y_plot(dropdown_value, data):
    if "BB_x" in data and "BB_y" in data:
        x = data['BB_x'][dropdown_value]
        y = data['BB_y'][dropdown_value]
    else:
        x = list()
        y = list()
    # BB_X = pars['BB_x'][dropdown_value]
    # BB_Y = pars['BB_y'][dropdown_value]
    # fig = go.Figure([go.Scatter()])
    df = pd.DataFrame({
        'Bounding Box X': x,
        'Bounding Box Y': y
    })

    return px.scatter(
        df,
        x='Bounding Box X',
        y='Bounding Box Y',
        marginal_x='histogram',
        marginal_y='histogram',
        trendline='ols'
    )


def make_area_plot(dropdown_value, data):
    if "BB_area" in data:
        x = data['BB_area'][dropdown_value]
    else:
        x = list()
    # BB_area = pars
    df = pd.DataFrame({
        'Bounding Box Area': x
    })

    return px.histogram(
        df,
        x='Bounding Box Area'
    )


def make_segmentation_plot(dropdown_value, data):
    if "seg_area" in data:
        x = data['seg_area'][dropdown_value]
    else:
        x = list()
    # BB_area = pars['seg_area'][dropdown_value]
    df = pd.DataFrame({
        'Segmentation Area': x
    })
    
    return px.histogram(
        df,
        x='Segmentation Area'
    )

def make_histo_plot(dropdown_value, plot_element, data):
    if plot_element.task not in dropdown_value:
        return ""
    else:
        plot_element.graph_config(dropdown_value, data)

def plot_elements():
    return [
        PlotElement("h-w", "Bounding Box Height vs Width", make_h_w_plot, "OD", ["BB_width", "BB_height"], ["Bounding Box Width", "Bounding Box Height"]),
        PlotElement("x-y", "Bounding Box X vs Y", make_x_y_plot, "OD", ["BB_x", "BB_y"], ["Bounding Box X", "Bounding Box Y"]),
        PlotElement("area", "Bounding Box Area", make_area_plot, "OD", ["BB_area"], ["Bounding Box Area"]),
        PlotElement("segmentation", "Segmentation Area", make_segmentation_plot, "SG", ["seg_area"], ["Segmentation Area"])
    ]