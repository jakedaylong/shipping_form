import shipping_form as sf
from nicegui.elements.mixins.value_element import ValueElement


def print():
    print(sf.recipient_name.value)
