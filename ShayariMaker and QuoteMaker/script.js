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
            const response = await fetch(`http://localhost:8080/chat?prompt=Don't show introductory part and give shayari in proper format like 1...in one line 2..in another line  and so on ${encodeURIComponent(promptText)} shayari`);
            const data = await response.text(); // Note the use of text() method

            // Display the generated shayari
            generatedShayari.textContent = data;
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    });
});
