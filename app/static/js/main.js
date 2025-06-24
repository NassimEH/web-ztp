const themeToggle = document.getElementById('theme-toggle');
const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');

const currentTheme = localStorage.getItem('theme') || (prefersDarkScheme.matches ? 'dark' : 'light');
if (currentTheme === 'dark') {
    document.body.classList.add('dark');
}

if (themeToggle) {
    themeToggle.innerHTML = currentTheme === 'dark' ? 
        '<ion-icon name="sunny-outline"></ion-icon>' : 
        '<ion-icon name="moon-outline"></ion-icon>';

    themeToggle.onclick = function() {
        if (document.body.classList.contains('dark')) {
            document.body.classList.remove('dark');
            localStorage.setItem('theme', 'light');
            themeToggle.innerHTML = '<ion-icon name="moon-outline"></ion-icon>';
        } else {
            document.body.classList.add('dark');
            localStorage.setItem('theme', 'dark');
            themeToggle.innerHTML = '<ion-icon name="sunny-outline"></ion-icon>';
        }
    };
}
