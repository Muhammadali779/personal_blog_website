// CONTACT FORM - Form submission handler
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('contactForm');
    const message = document.getElementById('formMessage');
    
    if (form) {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(form);
            
            // Here you would normally send to backend
            // For now, just show success message
            message.style.display = 'block';
            message.className = 'form-message success';
            message.textContent = 'Thank you for your message! I\'ll get back to you soon.';
            
            // Reset form
            form.reset();
            
            // Hide message after 5 seconds
            setTimeout(() => {
                message.style.display = 'none';
            }, 5000);
        });
    }
});
