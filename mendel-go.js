(function() {
    initPopover();
    initTextFields();
    initCustomRelations();

    function initPopover() {
        $('[data-toggle="popover"]').popover({
            container: 'body',
            html: true,
        });
    }

    function initTextFields() {
        var form = document.querySelector('.mendel-input-form');
        var fields = form.querySelectorAll('.text-form-field');

        for (var i = 0; i < fields.length; ++i) {
            initField(form, fields[i]);
        }

        function initField(form, field) {
            var visibleInput = field.querySelector('.text-form-field__visible');
            var hiddenInput = field.querySelector('.text-form-field__hidden');

            form.addEventListener('submit', onSubmit);

            function onSubmit() {
                hiddenInput.value = '"' + visibleInput.value + '"';
            }
        }
    }

    function initCustomRelations() {
        crossoverModel();

        function crossoverModel() {
            var select = document.querySelector('select[name="crossover_model"]');

            var relatedElements = [
                document.querySelector('input[name="mean_num_crossovers"]'),
                document.querySelector('input[name="crossover_fraction"]'),
            ];

            onChange();
            select.addEventListener('change', onChange);

            function onChange() {
                for (var i = 0; i < relatedElements.length; ++i) {
                    var relatedElement = relatedElements[i];
                    relatedElement.readOnly = (select.value !== '"partial"');
                }
            }
        }
    }
}());
