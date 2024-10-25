// schedule.js
document.getElementById("scheduleForm").addEventListener("submit", function(e) {
    const formFields = document.querySelectorAll("#scheduleForm input, #scheduleForm textarea");
    let valid = true;

    formFields.forEach(field => {
        if (!field.value.trim()) {
            valid = false;
            field.classList.add("error");
        } else {
            field.classList.remove("error");
        }
    });

    if (!valid) {
        e.preventDefault();
        alert("Please fill out all required fields.");
    }
});
