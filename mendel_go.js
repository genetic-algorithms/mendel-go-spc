(function() {
    initPopover();
    initBooleanFields();
    initCustomRelations();
    initImportSettings();
    initExportSettings();

    function initPopover() {
        $('[data-toggle="popover"]').popover({
            container: 'body',
            html: true,
        });
    }

    function initBooleanFields() {
        var form = document.querySelector('.mendel-input-form');
        var fields = form.querySelectorAll('.boolean-form-field');

        for (var i = 0; i < fields.length; ++i) {
            initField(form, fields[i]);
        }

        function initField(form, field) {
            var checkboxInput = field.querySelector('.boolean-form-field__checkbox');
            var hiddenInput = field.querySelector('.boolean-form-field__hidden');

            form.addEventListener('submit', onSubmit);

            function onSubmit() {
                hiddenInput.value = checkboxInput.checked ? 'True' : 'False';
            }
        }
    }

    function initCustomRelations() {
        crossoverModel();
        filesToOutput();

        function crossoverModel() {
            var select = document.querySelector('select[name="crossover_model"]');

            var relatedElements = [
                document.querySelector('input[name="mean_num_crossovers"]'),
            ];

            onChange();
            select.addEventListener('change', onChange);

            function onChange() {
                for (var i = 0; i < relatedElements.length; ++i) {
                    var relatedElement = relatedElements[i];
                    relatedElement.readOnly = (select.value !== 'partial');
                }
            }
        }

        function filesToOutput() {
            var hiddenInput = document.querySelector('input[name="files_to_output"]');
            var allCheckbox = document.getElementById('files_to_output_all');
            var fitCheckbox = document.getElementById('files_to_output_fit');
            var hstCheckbox = document.getElementById('files_to_output_hst');
            var alleleBinsCheckbox = document.getElementById('files_to_output_allele_bins');

            onChange();

            allCheckbox.addEventListener('change', onChange);
            fitCheckbox.addEventListener('change', onChange);
            hstCheckbox.addEventListener('change', onChange);
            alleleBinsCheckbox.addEventListener('change', onChange);

            function onChange() {
                var outputFiles = [];

                if (allCheckbox.checked) {
                    outputFiles.push('*');

                    fitCheckbox.disabled = true;
                    hstCheckbox.disabled = true;
                    alleleBinsCheckbox.disabled = true;
                } else {
                    if (fitCheckbox.checked) {
                        outputFiles.push('mendel.fit');
                    }

                    if (hstCheckbox.checked) {
                        outputFiles.push('mendel.hst');
                    }

                    if (alleleBinsCheckbox.checked) {
                        outputFiles.push('allele-bins/');
                        outputFiles.push('normalized-allele-bins/');
                        outputFiles.push('allele-distribution/');
                    }

                    fitCheckbox.disabled = false;
                    hstCheckbox.disabled = false;
                    alleleBinsCheckbox.disabled = false;
                }

                hiddenInput.value = outputFiles.join(',');
            }
        }
    }

    function initImportSettings() {
        var button = document.querySelector('.import-export-section .import-button');
        var mainForm = document.querySelector('.mendel-input-form');
        var form = document.querySelector('.import-form');
        var input = form.querySelector('input');

        button.addEventListener('click', onButtonClick);
        input.addEventListener('change', onInputChange);

        function onButtonClick() {
            input.click();
        }

        function onInputChange() {
            var f = input.files[0];
            var reader = new FileReader();
            reader.onload = function(e) {
                var text = e.target.result;
                input.value = '';
                var data = toml.parse(text);

                var groupKeys = Object.keys(data);
                groupKeys.forEach(function(groupKey) {
                    var groupValue = data[groupKey];

                    var keys = Object.keys(groupValue);
                    keys.forEach(function(key) {
                        var value = groupValue[key];
                        importItem(key, value);
                    });
                });
            };
            reader.readAsText(f);
        }

        function importItem(key, value) {
            if (key === 'data_file_path') return;

            if (key === 'files_to_output') {
                var fileNames = value.split(',');

                var fitCheckbox = document.getElementById('files_to_output_fit');
                var hstCheckbox = document.getElementById('files_to_output_hst');
                var alleleBinsCheckbox = document.getElementById('files_to_output_allele_bins');

                fitCheckbox.checked = fileNames.indexOf('mendel.fit') >= 0;
                hstCheckbox.checked = fileNames.indexOf('mendel.hst') >= 0;
                alleleBinsCheckbox.checked = fileNames.indexOf('allele-bins/') >= 0;

                fitCheckbox.dispatchEvent(new Event('change'));
                hstCheckbox.dispatchEvent(new Event('change'));
                alleleBinsCheckbox.dispatchEvent(new Event('change'));
            } else {
                var input = mainForm.querySelector('input[name="' + key + '"], select[name="' + key + '"]');

                if (input) {
                    if (input.parentNode.classList.contains('boolean-form-field')) {
                        var checkbox = input.parentNode.querySelector('.boolean-form-field__checkbox');
                        checkbox.checked = value;
                        checkbox.dispatchEvent(new Event('change'));
                    } else {
                        input.value = value;
                        input.dispatchEvent(new Event('change'));
                    }
                }
            }
        }
    }

    function initExportSettings() {
        var originalTomlDict = JSON.parse(document.querySelector('.js-data__original-toml-dict').textContent);
        var mainForm = document.querySelector('.mendel-input-form');
        var button = document.querySelector('.import-export-section .export-button');
        var a = document.createElement('a');
        a.setAttribute('download', 'export.toml');

        button.addEventListener('click', onClick);

        function onClick() {
            var output = '';
            var groupKeys = Object.keys(originalTomlDict);
            groupKeys.forEach(function(groupKey) {
                output += '[' + groupKey + ']\n';

                var groupValue = originalTomlDict[groupKey];
                var keys = Object.keys(groupValue);

                keys.forEach(function(key) {
                    var value = groupValue[key];

                    var input = mainForm.querySelector('input[name="' + key + '"], select[name="' + key + '"]');

                    if (input) {
                        var outputValue;

                        if (typeof value === 'boolean') {
                            var checkbox = input.parentNode.querySelector('.boolean-form-field__checkbox');
                            outputValue = JSON.stringify(checkbox.checked);
                        } else if (typeof value === 'number') {
                            outputValue = input.value;
                        } else {
                            outputValue = '"' + input.value + '"';
                        }

                        output += key + ' = ' + outputValue + '\n';
                    }
                });
            });

            a.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(output));
            a.click();
        }
    }
}());
