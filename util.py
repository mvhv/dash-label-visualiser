import json
import base64
import numpy as np
from skimage import draw as skid


def concatenate_list_data(list):
    result = ''
    for item in list:
        if item == list[-1]:
            result += str(item)
        else:
            result += str(item) + ' , '
    return result


def dropdown_options(label_names, task='OD'):
    return [{"label": name, "value": name} for name in label_names if name.startswith(task)]


def parse_upload_data(data):
    """assume data is a one element list containing a
    string with a comma separated header and a base64
    encoded body"""
    header, data_b64 = data[0].split(',')

    data_utf8 = base64.b64decode(data_b64).decode('utf-8')
    data_json = json.loads(data_utf8)
    return parse_annotations(data_json)


def parse_annotations(json_labels):
    pars = {
        'original_height': [],
        'original_width': [],
        'label_types': [],
        'label_names': [],
        'BB_width': {},
        'BB_height': {},
        'BB_area': {},
        'BB_x': {},
        'BB_y': {},
        'seg_area': {}
    }

    original_width = []
    original_height = []
    label_types = []
    label_names = []
    BB_width = []
    BB_height = []
    BB_area = []
    BB_x = []
    BB_y = []
    seg_area = []

    # find label types
    for label_item in range(len(json_labels)):
        result = json_labels[label_item]['annotations'][0]['result']
        for ann in result:
            ann_type = ann['type']
            label_types.append(ann_type)
            label_name_tmp = ann['value'][ann['type']][0]
            label_names.append(label_name_tmp)
            orig_width = ann['original_width']
            orig_height = ann['original_height']
            original_width.append(orig_width)
            original_height.append(orig_height)

    pars['label_types'] = list(set(label_types))
    pars['label_names'] = list(set(label_names))
    pars['original_height'] = list(set(original_height))
    pars['original_width'] = list(set(original_width))

    for label_name in pars['label_names']:
        for label_item in range(len(json_labels)):
            result = json_labels[label_item]['annotations'][0]['result']

            for ann in result:
                orig_width = ann['original_width']
                orig_height = ann['original_height']

                label_name_tmp = ann['value'][ann['type']][0]
                ann_type = ann['type']

                if ann_type == 'rectanglelabels' and label_name_tmp == label_name:

                    rect_width = ann['value']['width'] * 0.01 * orig_width
                    rect_height = ann['value']['height'] * 0.01 * orig_height
                    rect_x = ann['value']['x'] * 0.01 * orig_width
                    rect_y = ann['value']['y'] * 0.01 * orig_height
                    rect_area = rect_height * rect_width

                    if label_item == 0:
                        pars['BB_width'][label_name_tmp] = []
                        pars['BB_height'][label_name_tmp] = []
                        pars['BB_area'][label_name_tmp] = []
                        pars['BB_x'][label_name_tmp] = []
                        pars['BB_y'][label_name_tmp] = []

                    pars['BB_width'][label_name_tmp].append(rect_width)
                    pars['BB_height'][label_name_tmp].append(rect_height)
                    pars['BB_area'][label_name_tmp].append(rect_area)
                    pars['BB_x'][label_name_tmp].append(rect_x)
                    pars['BB_y'][label_name_tmp].append(rect_y)

                if ann_type == 'polygonlabels' and label_name_tmp == label_name:
                    mask = np.zeros((orig_height, orig_width, 1), dtype=np.int32)

                    r, c = [], []
                    for point in ann['value']['points']:
                        r.append(point[0] * 0.01 * orig_height)
                        c.append(point[1] * 0.01 * orig_width)

                    rr, cc = skid.polygon(r, c, (orig_height, orig_width))
                    colour = 1
                    if rr.max() >= mask.shape[0]:
                        print('rr is too large')
                    if cc.max() >= mask.shape[1]:
                        print('cc is too large')

                    mask[rr, cc] = (colour)  # (colour, colour, colour)

                    seg_area_tmp = len(mask[mask == 1])
                    if label_item == 0:
                        pars['seg_area'][label_name_tmp] = []
                    pars['seg_area'][label_name_tmp].append(seg_area_tmp)

    return pars