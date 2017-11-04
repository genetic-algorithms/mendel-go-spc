(function() {
    initPopover();
    initBooleanFields();
    initCustomRelations();

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
        trackNeutrals();
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

        function trackNeutrals() {
            var zeroTrackingThreshold = document.querySelector('.zero-tracking-threshold');
            var checkbox = document.getElementById('track_neutrals');

            checkbox.addEventListener('change', onChange);

            function onChange() {
                if (checkbox.checked) {
                    zeroTrackingThreshold.disabled = false;
                } else {
                    zeroTrackingThreshold.disabled = true;
                }
            }
        }

        function filesToOutput() {
            var hiddenInput = document.querySelector('input[name="files_to_output"]');
            var fitCheckbox = document.getElementById('files_to_output_fit');
            var hstCheckbox = document.getElementById('files_to_output_hst');
            var alleleBinsCheckbox = document.getElementById('files_to_output_allele_bins');

            onChange();

            fitCheckbox.addEventListener('change', onChange);
            hstCheckbox.addEventListener('change', onChange);
            alleleBinsCheckbox.addEventListener('change', onChange);

            function onChange() {
                var outputFiles = [];

                if (fitCheckbox.checked) {
                    outputFiles.push('mendel.fit');
                }

                if (hstCheckbox.checked) {
                    outputFiles.push('mendel.hst');
                }

                if (alleleBinsCheckbox.checked) {
                    outputFiles.push('allele-bins/');
                    outputFiles.push('normalized-allele-bins/');
                }

                hiddenInput.value = outputFiles.join(',');
            }
        }
    }
}());
