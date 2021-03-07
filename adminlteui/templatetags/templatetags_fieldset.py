from django.urls import reverse
from django import template

register = template.Library()


@register.filter('test')
def test(obj):
    try:
        print()
        print(obj.widget.__dict__)
    except:
        pass
    return ''


@register.filter('div_cols')
def div_cols(field):
    if not field.is_readonly:
        if 'cols' in field.field.form.Meta.model.__dict__ \
                and field.field.name in field.field.form.Meta.model.cols:
            return field.field.form.Meta.model.cols[field.field.name]
    else:
        if 'cols' in field.model_admin.model.__dict__ \
                and field.field['name'] in field.model_admin.model.cols:
            return field.model_admin.model.cols[field.field['name']]
    return 4


@register.filter('input_type')
def input_type(ob):
    '''
    Extract form field type
    :param ob: form field
    :return: string of form field widget type
    '''
    return ob.field.widget.__class__.__name__


@register.filter(name='add_classes')
def add_classes(value, arg):
    '''
    Add provided classes to form field
    :param value: form field
    :param arg: string of classes seperated by ' '
    :return: edited field
    '''
    css_classes = value.field.widget.attrs.get('class', '')
    # check if class is set or empty and split its content to list (or init list)
    if css_classes:
        css_classes = css_classes.split(' ')
    else:
        css_classes = []
    # prepare new classes to list
    args = arg.split(' ')
    for a in args:
        if a not in css_classes:
            css_classes.append(a)
    # join back to single string
    return value.as_widget(attrs={'class': ' '.join(css_classes)})
