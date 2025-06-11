function initDHCPSlider(subnet, initialMin, initialMax) {
    // Valeurs par défaut adaptées à un subnet /24
    const min_ip = 2;
    const max_ip = 254;
    
    // Convertit les IPs complètes en dernier octet pour le slider
    const getLastOctet = (ip) => ip ? parseInt(ip.split('.').pop()) : min_ip;
    
    $("#slider-range").slider({
        range: true,
        min: min_ip,
        max: max_ip,
        values: [
            getLastOctet(initialMin),
            getLastOctet(initialMax)
        ],
        slide: function(event, ui) {
            updateIPRangeDisplay(subnet, ui.values[0], ui.values[1]);
        },
        change: function(event, ui) {
            updateIPRangeDisplay(subnet, ui.values[0], ui.values[1]);
        }
    });
    
    // Initialisation
    const initialValues = $("#slider-range").slider("values");
    updateIPRangeDisplay(subnet, initialValues[0], initialValues[1]);
}

function updateIPRangeDisplay(subnet, min, max) {
    const fullMinIP = `${subnet}.${min}`;
    const fullMaxIP = `${subnet}.${max}`;
    
    $("#ip-range").val(`${fullMinIP} - ${fullMaxIP}`);
    $("#id_min_ip_pool").val(fullMinIP);
    $("#id_max_ip_pool").val(fullMaxIP);
}

$(document).ready(function() {
    // Initialise le slider quand la page est prête
    const subnet = "{{ form.instance.subnet|default:'192.168.1' }}";
    const initialMin = "{{ form.instance.min_ip_pool|default:'' }}";
    const initialMax = "{{ form.instance.max_ip_pool|default:'' }}";
    
    initDHCPSlider(subnet, initialMin, initialMax);
});