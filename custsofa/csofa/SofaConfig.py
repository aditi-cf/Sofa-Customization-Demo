from GenricConfig import Furniture, Components, ComponentInfo
from .models import Size, Back, BackVariant, PipeVariant, Pipe, Arm, ArmVariant, LegVariant, Leg, Color


def config_sofa():
    furniture = Furniture()
    furniture.name = 'sofa'

    components = Components()
    components.name = 'arm'
    c_info = ComponentInfo()
    c_info.add_dependent_list([
        {'back': {'back_all': {'size': 'arm', 'color': 'arm', 'arm': 'arm'}}},
        {'leg': {'leg_all': {'size': 'arm', 'arm': 'arm'}}},
        {'pipe': {'pipe_all': {'size': 'arm', 'color': 'arm', 'arm': 'arm', 'back': 'back'}}}
    ])
    c_info.add_api_list({
        'arm_all': {'size': 'arm', 'color': 'arm', 'back': 'back'},
        'arm_color_all': {'size': 'arm', 'arm': 'arm', 'back': 'back'}
    })
    c_info.add_property_list(ArmVariant.objects.filter(size='size_1', armId=Arm.objects.filter(name='arm_1'), color=Color.objects.filter(name='green'))[0].as_json())
    components.set_comp_info(c_info)
    furniture.add_component(components.as_json())

    components = Components()
    components.name = 'back'
    c_info = ComponentInfo()
    c_info.add_dependent_list([{'pipe': {'pipe_all': {'size': 'arm', 'color': 'arm', 'arm': 'arm', 'back': 'back'}}}])
    c_info.add_api_list({
        'back_all': {'size': 'back', 'color': 'back', 'arm': 'back'},
        'back_color_all': {'size': 'back', 'back': 'back', 'arm': 'back'}
    })
    c_info.add_property_list(BackVariant.objects.filter(size='size_1', backId=Back.objects.filter(name='back_1'), armId=Arm.objects.filter(name='arm_1'))[0].as_json())
    components.set_comp_info(c_info)
    furniture.add_component(components.as_json())

    components = Components()
    components.name = 'leg'
    c_info = ComponentInfo()
    c_info.add_dependent_list([])
    c_info.add_api_list({
        'leg_all': {'size': 'leg', 'arm': 'leg'},
        'leg_color_all': {'size': 'leg', 'arm': 'leg', 'leg': 'leg'}
    })
    c_info.add_property_list(LegVariant.objects.filter(size='size_1', armId=Arm.objects.filter(name='arm_1'))[0].as_json())
    components.set_comp_info(c_info)
    furniture.add_component(components.as_json())

    components = Components()
    components.name = 'pipe'
    c_info = ComponentInfo()
    c_info.add_dependent_list([])
    c_info.add_api_list({
        'pipe_all': {'size': 'pipe', 'color': 'pipe', 'arm': 'pipe', 'back': 'pipe'},
        'pipe_color_all': {'size': 'pipe', 'pipe': 'pipe', 'arm': 'pipe', 'back': 'pipe'}
    })
    c_info.add_property_list(PipeVariant.objects.filter(size='size_1', color=Color.objects.filter(name='lightgreen'), armId=Arm.objects.filter(name='arm_1'), backId=Back.objects.filter(name='back_1'))[0].as_json())
    components.set_comp_info(c_info)
    furniture.add_component(components.as_json())

    furniture.add_select_option({'name': 'size', 'value': [Size.objects.filter(name='size_1')[0].as_json()]})

    furniture.update_price()

    # tooloption: {url: component}
    furniture.add_tooloptions([('Size', {'size_all': 'size'}), ('Arm', {'arm_all': 'arm'}), ('Arm Color', {'arm_color_all': 'arm'}),
                                ('Back', {'back_all': 'back'}), ('Back Color', {'back_color_all': 'back'}), ('Leg', {'leg_all': 'leg'}),
                                ('Leg Color', {'leg_color_all': 'leg'}), ('Pipe', {'pipe_all': 'pipe'}), ('Pipe Color', {'pipe_color_all': 'pipe'})])

    return furniture.as_json()
