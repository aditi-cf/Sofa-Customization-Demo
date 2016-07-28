from collections import OrderedDict


class ComponentInfo:
    def __init__(self):
        self.properties = {}
        self.dependents = []
        self.apis = {}

    def add_property(self, name, val):
        self.properties[name] = val

    def add_property_list(self, p_list):
        self.properties.update(p_list)

    def add_dependent_list(self, d_list):
        self.dependents.extend(d_list)

    def add_dependent(self, d):
        self.dependents.append(d)

    def add_api(self, api, api_args):
        self.apis[api] = api_args

    def add_api_list(self, a_list):
        self.apis.update(a_list)

    def as_json(self):
        data = {
            'properties': self.properties,
            'dependents': self.dependents,
            'apis': self.apis
        }
        return data


class Components:
    def __init__(self):
        self.name = ''
        self.comp_info = {}

    def set_name(self, n):
        self.name = n

    def set_comp_info(self, c_info):
        self.comp_info.update(c_info.as_json())

    def as_json(self):
        data = {
            'name': self.name,
            'comp_info': self.comp_info
        }
        return data


class Furniture:
    def __init__(self):
        self.name = ''
        self.selectBar = {}
        self.components = OrderedDict([])
        self.toolOptions = OrderedDict([])
        self.price = 0

    def add_select_option(self, sel_opt):
        self.selectBar = sel_opt


    def add_component(self, comp):
        self.components[comp.get('name')] = comp.get('comp_info')

    def add_tooloptions(self, t_list):
        self.toolOptions.update(OrderedDict(t_list))


    def as_json(self):
        data = {
            'name': self.name,
            'components': self.components,
            'toolOptions': self.toolOptions,
            'selectBar': self.selectBar,
            'price': self.price
        }
        return data

    def update_price(self):
        for comp,cval in self.components.iteritems():
            self.price += float(cval['properties']['price'])

def print1(fur):
    print fur.__dict__


