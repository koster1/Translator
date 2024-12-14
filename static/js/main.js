// Limit character input and handle form submission
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const textarea = document.getElementById('text');
    const charCount = document.getElementById('char-count');
    const loadingDiv = document.getElementById('loading');
    const maxCharLength = 2000;  // Max characters allowed in the textarea
    const maxHeight = 200;   // Max height of the textarea before showing a scrollbar

    // Handle input changes: enforce max length and adjust textarea size
    textarea.addEventListener('input', function () {
        let currentLength = textarea.value.length;

        // Limit textarea content to maxCharLength characters
        if (currentLength > maxCharLength) {
            textarea.value = textarea.value.substring(0, maxCharLength);
            currentLength = maxCharLength;
        }

        // Update character count and change color if limit is reached
        charCount.textContent = `${currentLength} / ${maxCharLength}`;
        charCount.style.color = currentLength >= maxCharLength ? 'red' : 'white';

        // Adjust the height of the textarea dynamically based on content
        this.style.height = 'auto';  // Reset height for accurate calculation
        const contentHeight = this.scrollHeight;
        this.style.height = contentHeight > maxHeight ? `${maxHeight}px` : `${contentHeight}px`;
        this.style.overflowY = contentHeight > maxHeight ? 'auto' : 'hidden';
    });

    // Allow form submission with Enter key (without Shift for newline)
    textarea.addEventListener('keydown', function (event) {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault();  // Prevent newline

            // Show loading indicator before submitting
            loadingDiv.style.display = 'block';

            // Submit the form
            form.submit();
        }
    });

    // Show loading indicator when form is submitted via button
    form.addEventListener('submit', function (event) {
        if (textarea.value.length > maxCharLength) {
            event.preventDefault();
            alert(`Input text exceeds the maximum allowed length of ${maxCharLength} characters.`);
        } else {
            loadingDiv.style.display = 'block';  // Show loading indicator on form submit
        }
    });
});
