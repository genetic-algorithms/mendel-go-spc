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
