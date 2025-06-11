document.addEventListener('DOMContentLoaded', function () {
    const minSlider = document.getElementById('minRange');
    const maxSlider = document.getElementById('maxRange');
    const minValue = document.getElementById('minValue');
    const maxValue = document.getElementById('maxValue');
    const minHidden = document.getElementById('id_min_ip_pool');
    const maxHidden = document.getElementById('id_max_ip_pool');

    function updateTrackStyle() {
        const min = parseInt(minSlider.value);
        const max = parseInt(maxSlider.value);
        const percentageMin = (min / 255) * 100;
        const percentageMax = (max / 255) * 100;

        minSlider.style.background = `
            linear-gradient(
                to right,
                #dee2e6 0%,
                #dee2e6 ${percentageMin}%,
                #0d6efd ${percentageMin}%,
                #0d6efd ${percentageMax}%,
                #dee2e6 ${percentageMax}%,
                #dee2e6 100%
            )
        `;
    }

    function syncSliders() {
        minSlider.value = minHidden.value;
        maxSlider.value = maxHidden.value;
        minValue.textContent = minSlider.value;
        maxValue.textContent = maxSlider.value;
        updateTrackStyle();
    }

    minSlider.addEventListener('input', function () {
        if (parseInt(this.value) > parseInt(maxSlider.value)) {
            this.value = maxSlider.value;
        }
        minValue.textContent = this.value;
        minHidden.value = this.value;
        updateTrackStyle();
    });

    maxSlider.addEventListener('input', function () {
        if (parseInt(this.value) < parseInt(minSlider.value)) {
            this.value = minSlider.value;
        }
        maxValue.textContent = this.value;
        maxHidden.value = this.value;
        updateTrackStyle();
    });

    syncSliders();
});
