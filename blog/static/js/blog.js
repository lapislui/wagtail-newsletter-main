document.addEventListener('DOMContentLoaded', function() {
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Progressive image loading
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.removeAttribute('data-src');
                observer.unobserve(img);
            }
        });
    });

    images.forEach(img => imageObserver.observe(img));

    // Reading time estimate
    const articleContent = document.querySelector('.post-content');
    if (articleContent) {
        const words = articleContent.textContent.trim().split(/\s+/).length;
        const readingTime = Math.ceil(words / 200); // Assuming 200 words per minute
        const readingTimeElement = document.createElement('span');
        readingTimeElement.classList.add('reading-time');
        readingTimeElement.textContent = `${readingTime} min read`;
        document.querySelector('.post-meta').appendChild(readingTimeElement);
    }
});