// CODE-COPY.JS - Copy Code Functionality
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.btn-copy').forEach(btn => {
        btn.addEventListener('click', function() {
            const targetId = this.getAttribute('data-clipboard-target');
            const code = document.getElementById(targetId);
            
            if (code) {
                navigator.clipboard.writeText(code.textContent).then(() => {
                    const span = this.querySelector('span');
                    const originalText = span.textContent;
                    span.textContent = 'Copied!';
                    setTimeout(() => {
                        span.textContent = originalText;
                    }, 2000);
                });
            }
        });
    });
});
