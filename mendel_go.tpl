<%
    from spc_apps.mendel_go.settings import get_config_fields, get_config_tabs
    from spc_apps.mendel_go.util import get_hidden_fields, render_form_row

    config_fields = get_config_fields(apps[app].params)
    config_tabs = get_config_tabs()
%>

<!DOCTYPE html>
<html>
<head>
    <title>{{tab_title}}</title>

    <meta name="viewport" content="width=device-width, initial-scale=1" />

    <link rel="stylesheet" href="/static/css/bootstrap.min.css" />
    <link rel="stylesheet" href="/static/css/bootstrap-tagsinput.css" />
    <link rel="stylesheet" href="/static/css/style-metro.css" />

    <link rel="stylesheet" href="/static/apps/mendel_go/mendel_go.css" />
</head>
<body>
    <div class="container-fluid">
        %include('navbar')
        %include('apps/alert')
        <div id="memory" class="alert-info hidden-xs"></div>
        <div id="danger" class="alert-danger"></div>
        <div id="warning" class="alert-warning"></div>
    </div>


    <form class="mendel-input-form" name="mendel_input" method="post" action="/confirm">
        <input type="hidden" name="app" value="{{app}}">
        <input type="hidden" name="data_file_path" value="./">
        <input class="zero-tracking-threshold" type="hidden" name="tracking_threshold" value="0" disabled />

        <a class="user-manual-link" href="/static/apps/mendel/help.html" target="_blank">User Manual</a>

        <div class="page-width">
            <div class="page-width__inner">
                <div class="form-sections">
                    % for i, config_tab in enumerate(config_tabs):
                        <div class="form-section">
                            <div class="form-section__title">{{config_tab['title']}}</div>
                            <div class="form-section__fields">
                                % for j, tab_field in enumerate(config_tab['fields']):
                                    % config_field_id = tab_field['id']
                                    % config_field = config_fields[config_field_id]

                                    {{!render_form_row(config_field, config_field_id, unicode(j + 1))}}

                                    <div class="form-child-rows">
                                        % if 'children' in tab_field:
                                            % for k, child in enumerate(tab_field['children']):
                                                % config_field_id = child['id']
                                                % config_field = config_fields[config_field_id]

                                                {{!render_form_row(config_field, config_field_id, chr(97 + k))}}
                                            % end
                                        % end
                                    </div>
                                % end
                            </div>
                        </div>
                    % end

                    <div class="form-section">
                        <div class="form-section__title">Job</div>
                        <div class="form-section__fields">
                            <div class="form-row">
                                <div class="form-row__label">1. Tags:</div>
                                <div class="form-row__widget">
                                    <input class="form-control tags-input" type="text" id="desc" name="desc" data-role="tagsinput" placeholder="Enter tag…" />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <button class="form-submit-button btn btn-success" type="submit">Continue</button>
            </div>
        </div>
    </form>

    <script src="/static/jquery-2.1.4.min.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>
    <script src="/static/js/jquery.highlight.js"></script>
    <script src="/static/js/jquery.validate.min.js"></script>
    <script src="/static/js/bootstrap-tagsinput.min.js"></script>
    <script src="/static/js/bootstrap-notify.min.js"></script>

    <script src="/static/apps/mendel_go/mendel_go.js"></script>
</body>
</html>
