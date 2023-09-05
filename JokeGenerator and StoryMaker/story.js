document.addEventListener('DOMContentLoaded', function () {
    const shayariInput = document.getElementById('shayariInput');
    const generateButton = document.getElementById('generateButton');
    const generatedShayari = document.getElementById('generatedShayari');

    generateButton.addEventListener('click', async () => {
        const promptText = shayariInput.value;

        if (promptText.trim() === '') {
            alert('Please enter a prompt.');
            return;
        }

        try {
            const response = await fetch(`http://localhost:8080/chat?prompt=Think you are story teller and Don't show introductory part and show only one best story not more than that of about 100 words. Now write story on ${encodeURIComponent(promptText)}`);
            const data = await response.text(); // Note the use of text() method

            // Display the generated shayari
            generatedShayari.textContent = data;
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    });
});
