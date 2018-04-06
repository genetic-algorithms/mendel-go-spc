from __future__ import unicode_literals

from bottle import template


def get_visible_field_ids(tabs):
    visible_field_ids = []

    for tab in tabs:
        for field in tab['fields']:
            visible_field_ids.append(field['id'])

            if 'children' in field:
                for child in field['children']:
                    visible_field_ids.append(child['id'])

    return visible_field_ids


def get_hidden_fields(tabs, params):
    visible_field_ids = get_visible_field_ids(tabs)
    hidden_fields = {}

    for key, value in params.iteritems():
        if not key in visible_field_ids:
            hidden_fields[key] = value

    return hidden_fields


def render_form_row(config_field, config_field_id, label_index):
    template_str = '''
        <div class="form-row">
            <label for="{{config_field_id}}" class="form-row__label">{{label_index}}. {{config_field['label']}}:</label>

            <div class="form-row__widget">
                {{!widget}}
            </div>

            % if 'help' in config_field:
                <div class="form-row__help">
                    <a class="form-help-popover"
                        data-toggle="popover"
                        data-trigger="focus"
                        data-placement="bottom"
                        tabindex="-1"
                        role="button"
                        title="{{config_field_id}}"
                        data-content='{{config_field['help']}}
                            % if 'more_help_url' in config_field:
                                <a href="{{config_field['more_help_url']}}" target="_blank">Read More</a>
                            % end
                        '>
                        ?
                    </a>
                </div>
            % end
        </div>
    '''

    template_kwargs = {
        'config_field': config_field,
        'config_field_id': config_field_id,
        'label_index': label_index,
        'widget': render_widget(config_field, config_field_id),
    }

    return template(template_str, **template_kwargs)


def render_widget(widget, widget_id):
    if widget['type']['id'] == 'number':
        return render_number_widget(widget, widget_id)
    elif widget['type']['id'] == 'select':
        return render_select_widget(widget, widget_id)
    elif widget['type']['id'] == 'boolean':
        return render_boolean_widget(widget, widget_id)
    elif widget['type']['id'] == 'text':
        return render_text_widget(widget, widget_id)
    else:
        return ''


def render_number_widget(widget, widget_id):
    template_str = '''
        <div class="number-form-field">
            <input class="form-control" id="{{id}}" type="number" name="{{id}}" value="{{value}}" min="{{min}}" max="{{max}}" step="{{step}}" />
        </div>
    '''

    template_kwargs = {
        'id': widget_id,
        'value': widget['value'],
        'min': widget['type']['min'],
        'max': widget['type']['max'],
        'step': widget['type']['step'],
    }

    return template(template_str, **template_kwargs)


def render_select_widget(widget, widget_id):
    template_str = '''
        <div class="select-form-field">
            <select class="form-control" id="{{id}}" name="{{id}}">
                % for choice_value, choice_title in choices:
                    % if choice_value == value:
                        <option value="{{choice_value}}" selected>{{choice_title}}</option>
                    % else:
                        <option value="{{choice_value}}">{{choice_title}}</option>
                    % end
                % end
            </select>
        </div>
    '''

    template_kwargs = {
        'id': widget_id,
        'value': widget['value'],
        'choices': widget['type']['choices'],
    }

    return template(template_str, **template_kwargs)


def render_boolean_widget(widget, widget_id):
    template_str = '''
        <div class="boolean-form-field">
            <input class="boolean-form-field__checkbox" id="{{id}}" type="checkbox" {{checked}} />
            <input class="boolean-form-field__hidden" type="hidden" name="{{id}}" />
        </div>
    '''

    template_kwargs = {
        'id': widget_id,
        'checked': 'checked' if widget['value'] else '',
    }

    return template(template_str, **template_kwargs)


def render_text_widget(widget, widget_id):
    template_str = '''
        <div class="text-form-field">
            <input class="form-control" id="{{id}}" type="text" name="{{id}}" value="{{value}}" />
        </div>
    '''

    template_kwargs = {
        'id': widget_id,
        'value': widget['value'],
    }

    return template(template_str, **template_kwargs)
