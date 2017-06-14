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
        polygenicBeneficials();

        function polygenicBeneficials() {
            var checkbox = document.querySelector('input[name="polygenic_beneficials"]');

            var relatedElements = [
                document.querySelector('input[name="polygenic_init"]').parentNode.querySelector('.text-form-field__visible'),
                document.querySelector('input[name="polygenic_target"]').parentNode.querySelector('.text-form-field__visible'),
                document.querySelector('input[name="polygenic_effect"]'),
            ];

            onChange();
            checkbox.addEventListener('change', onChange);

            function onChange() {
                for (var i = 0; i < relatedElements.length; ++i) {
                    var relatedElement = relatedElements[i];
                    relatedElement.readOnly = !checkbox.checked;
                }
            }
        }
    }
}());
