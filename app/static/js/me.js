document.getElementById('avatar').addEventListener('change', function(e) {
    if (this.files && this.files[0]) {
        this.closest('form').submit();
    }
});