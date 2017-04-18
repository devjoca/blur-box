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
});