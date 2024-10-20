// DOM Elements
const appointmentForm = document.querySelector('#booking-form form');
const appointmentsList = document.querySelector('#appointments ul');

// Listen for form submission to book an appointment
appointmentForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from refreshing the page

    const formData = new FormData(appointmentForm);
    const name = formData.get('name');
    const time = formData.get('time');

    if (name && time) {
        // Simulate adding the appointment dynamically
        const appointmentItem = document.createElement('li');
        appointmentItem.classList.add('appointment-item');
        appointmentItem.innerHTML = `<strong>${name}</strong> - <em>${time}</em> <button class="delete-appointment">Delete</button>`;
        
        appointmentsList.appendChild(appointmentItem);

        // Clear the form after submission
        appointmentForm.reset();
    }
});

// Handle dynamic appointment deletion
appointmentsList.addEventListener('click', function(event) {
    if (event.target.classList.contains('delete-appointment')) {
        const appointmentItem = event.target.closest('li');
        appointmentsList.removeChild(appointmentItem);
    }
});

// Optional: Add AJAX call to submit the form without reloading the page (for backend integration)
function submitForm(formData) {
    fetch('/book', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

// Developer customization hook (example)
function customizeScheduler(options) {
    // Example: Change form colors dynamically
    if (options.formBackgroundColor) {
        document.querySelector('#booking-form').style.backgroundColor = options.formBackgroundColor;
    }
    if (options.textColor) {
        document.body.style.color = options.textColor;
    }
}

// Example usage of customization hook
customizeScheduler({
    formBackgroundColor: '#eef',
    textColor: '#333'
});