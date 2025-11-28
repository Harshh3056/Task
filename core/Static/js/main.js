// Example: Alert when submitting quiz
document.addEventListener('DOMContentLoaded', function() {
    const quizForm = document.querySelector('form');
    if (quizForm) {
        quizForm.addEventListener('submit', function() {
            alert('Your quiz has been submitted!');
        });
    }
});
