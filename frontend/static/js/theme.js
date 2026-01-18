// THEME.JS - Dark/Light Mode Toggle
(function() {
    const theme = localStorage.getItem('theme') || 'light';
    document.body.classList.toggle('dark-mode', theme === 'dark');
    
    const toggle = document.getElementById('themeToggle');
    if (toggle) {
        toggle.addEventListener('click', () => {
            const isDark = document.body.classList.toggle('dark-mode');
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
        });
    }
})();
