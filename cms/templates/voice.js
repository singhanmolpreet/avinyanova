// voice.js

const recognition = new webkitSpeechRecognition() || new SpeechRecognition();
const synth = window.speechSynthesis;

function startVoiceInput() {
    recognition.lang = 'en-US'; // Set language
    recognition.start();
}

recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    document.getElementById('user_prompt').value = transcript;
    document.getElementById('voice_input_form').submit(); // Submit form with voice input
};

function speak(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    synth.speak(utterance);
}

// Attach event listeners to buttons
document.getElementById('voice_input_button').addEventListener('click', startVoiceInput);