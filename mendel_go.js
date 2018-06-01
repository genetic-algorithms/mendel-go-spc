(function() {
    initPopover();
    initWidgets();
    initCustomRelations();
    initImportSettings();
    initExportSettings();

    function initPopover() {
        $('[data-toggle="popover"]').popover({
            container: 'body',
            html: true,
        });
    }

    function initWidgets() {
        var form = document.querySelector('.mendel-input-form');

        form.addEventListener('submit', onSubmit);

        function onSubmit() {
            submitBooleanFields();
            submitSelectFields();
        }

        function submitBooleanFields() {
            const fields = form.querySelectorAll('.boolean-form-field');

            for (let i = 0; i < fields.length; ++i) {
                const field = fields[i];
                const checkboxInput = field.querySelector('.boolean-form-field__checkbox');
                const hiddenInput = field.querySelector('.boolean-form-field__hidden');
                hiddenInput.value = checkboxInput.checked ? 'True' : 'False';
            }
        }

        function submitSelectFields() {
            const selects = form.querySelectorAll('.select-form-field select');

            for (let i = 0; i < selects.length; ++i) {
                // Select fields don't have a readOnly property so we simulate it by using disabled
                // and then enabling them on submit
                selects[i].disabled = false;
            }
        }
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
        const fields = {
            crossover_model: document.querySelector('select[name="crossover_model"]'),
            files_to_output_all: document.getElementById('files_to_output_all'),
            files_to_output_allele_bins: document.getElementById('files_to_output_allele_bins'),
            files_to_output_fit: document.getElementById('files_to_output_fit'),
            files_to_output_hst: document.getElementById('files_to_output_hst'),
            files_to_output: document.querySelector('input[name="files_to_output"]'),
            fitness_effect_model: document.querySelector('select[name="fitness_effect_model"]'),
            frac_fav_mutn: document.querySelector('input[name="frac_fav_mutn"]'),
            max_fav_fitness_gain: document.querySelector('input[name="max_fav_fitness_gain"]'),
            mean_num_crossovers: document.querySelector('input[name="mean_num_crossovers"]'),
            uniform_fitness_effect_del: document.querySelector('input[name="uniform_fitness_effect_del"]'),
            uniform_fitness_effect_fav: document.querySelector('input[name="uniform_fitness_effect_fav"]'),
            selection_model: document.querySelector('select[name="selection_model"]'),
            partial_truncation_value: document.querySelector('input[name="partial_truncation_value"]'),
            num_contrasting_alleles: document.querySelector('input[name="num_contrasting_alleles"]'),
            max_total_fitness_increase: document.querySelector('input[name="max_total_fitness_increase"]'),
            initial_allele_fitness_model: document.querySelector('select[name="initial_allele_fitness_model"]'),
            initial_alleles_pop_frac: document.querySelector('input[name="initial_alleles_pop_frac"]'),
            initial_alleles_frequencies: document.querySelector('input[name="initial_alleles_frequencies"]'),
            pop_growth_model: document.querySelector('select[name="pop_growth_model"]'),
            pop_growth_rate: document.querySelector('input[name="pop_growth_rate"]'),
            pop_growth_rate2: document.querySelector('input[name="pop_growth_rate2"]'),
            max_pop_size: document.querySelector('input[name="max_pop_size"]'),
            carrying_capacity: document.querySelector('input[name="carrying_capacity"]'),
            bottleneck_generation: document.querySelector('input[name="bottleneck_generation"]'),
            bottleneck_pop_size: document.querySelector('input[name="bottleneck_pop_size"]'),
            num_bottleneck_generations: document.querySelector('input[name="num_bottleneck_generations"]'),
            tracking_threshold: document.querySelector('input[name="tracking_threshold"]'),
            plot_allele_gens: document.querySelector('input[name="plot_allele_gens"]'),
            omit_first_allele_bin: document.getElementById('omit_first_allele_bin'),
        };

        update();
        fields.crossover_model.addEventListener('change', update);
        fields.fitness_effect_model.addEventListener('change', update);
        fields.frac_fav_mutn.addEventListener('input', update);
        fields.files_to_output_all.addEventListener('change', update);
        fields.files_to_output_fit.addEventListener('change', update);
        fields.files_to_output_hst.addEventListener('change', update);
        fields.files_to_output_allele_bins.addEventListener('change', update);
        fields.selection_model.addEventListener('change', update);
        fields.num_contrasting_alleles.addEventListener('input', update);
        fields.initial_allele_fitness_model.addEventListener('change', update);
        fields.pop_growth_model.addEventListener('change', update);
        fields.bottleneck_generation.addEventListener('input', update);

        function update() {
            fields.mean_num_crossovers.readOnly = (fields.crossover_model.value !== 'partial');
            fields.uniform_fitness_effect_del.readOnly = (fields.fitness_effect_model.value !== 'fixed');
            fields.uniform_fitness_effect_fav.readOnly = (
                fields.fitness_effect_model.value !== 'fixed' ||
                parseFloat(fields.frac_fav_mutn.value) === 0
            );
            fields.max_fav_fitness_gain.readOnly = (parseFloat(fields.frac_fav_mutn.value) === 0);
            fields.partial_truncation_value.readOnly = (fields.selection_model.value !== 'partialtrunc');
            fields.max_total_fitness_increase.readOnly = (parseFloat(fields.num_contrasting_alleles.value) === 0);
            fields.initial_allele_fitness_model.disabled = (parseFloat(fields.num_contrasting_alleles.value) === 0);
            fields.initial_alleles_pop_frac.readOnly = (
                parseFloat(fields.num_contrasting_alleles.value) === 0 ||
                fields.initial_allele_fitness_model.value === 'variablefreq'
            );
            fields.initial_alleles_frequencies.readOnly = (
                parseFloat(fields.num_contrasting_alleles.value) === 0 ||
                fields.initial_allele_fitness_model.value === 'allunique'
            );
            fields.pop_growth_rate.readOnly = (fields.pop_growth_model.value === 'none');
            fields.pop_growth_rate2.readOnly = (fields.pop_growth_model.value !== 'founders');
            fields.max_pop_size.readOnly = (fields.pop_growth_model.value !== 'exponential');
            fields.carrying_capacity.readOnly = (
                fields.pop_growth_model.value === 'none' ||
                fields.pop_growth_model.value === 'exponential'
            );
            fields.bottleneck_generation.readOnly = (fields.pop_growth_model.value !== 'founders');
            fields.bottleneck_pop_size.readOnly = (
                fields.pop_growth_model.value !== 'founders' ||
                parseFloat(fields.bottleneck_generation.value) === 0
            );
            fields.num_bottleneck_generations.readOnly = (
                fields.pop_growth_model.value !== 'founders' ||
                parseFloat(fields.bottleneck_generation.value) === 0
            );
            fields.tracking_threshold.readOnly = (!fields.files_to_output_all.checked && !fields.files_to_output_allele_bins.checked);
            fields.plot_allele_gens.readOnly = (!fields.files_to_output_all.checked && !fields.files_to_output_allele_bins.checked);
            fields.omit_first_allele_bin.disabled = (!fields.files_to_output_all.checked && !fields.files_to_output_allele_bins.checked);

            filesToOutput();

            function filesToOutput() {
                const outputFiles = [];

                if (fields.files_to_output_all.checked) {
                    outputFiles.push('*');

                    fields.files_to_output_fit.disabled = true;
                    fields.files_to_output_hst.disabled = true;
                    fields.files_to_output_allele_bins.disabled = true;
                } else {
                    if (fields.files_to_output_fit.checked) {
                        outputFiles.push('mendel.fit');
                    }

                    if (fields.files_to_output_hst.checked) {
                        outputFiles.push('mendel.hst');
                    }

                    if (fields.files_to_output_allele_bins.checked) {
                        outputFiles.push('allele-bins/');
                        outputFiles.push('normalized-allele-bins/');
                        outputFiles.push('allele-distribution/');
                    }

                    fields.files_to_output_fit.disabled = false;
                    fields.files_to_output_hst.disabled = false;
                    fields.files_to_output_allele_bins.disabled = false;
                }

                fields.files_to_output.value = outputFiles.join(',');
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
