jQuery(document).ready(function($) {
    var file_input = $('#file_input');
    var form = $('#form');

    file_input.change(function() {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#img_preview').attr('src', e.target.result);
        }

        reader.readAsDataURL(this.files[0]);
    });

    form.submit(function(e) {
        e.preventDefault();

        $.post(form.attr('action'), {
            image: $('#img_preview').attr('src')
        }).then(function(data) {
            $('#img_blur').attr('src', 'data:image/png;base64,' + data)
        })
    })
});