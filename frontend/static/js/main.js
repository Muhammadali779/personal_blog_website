// MAIN.JS - Core JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle
    const mobileToggle = document.getElementById('mobileMenuToggle');
    const mobileMenu = document.getElementById('mobileMenu');
    
    if (mobileToggle) {
        mobileToggle.addEventListener('click', () => {
            mobileMenu.classList.toggle('active');
        });
    }
});
