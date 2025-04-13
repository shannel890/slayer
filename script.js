document.getElementById("contactForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();

    if (!name || !email || !message) {
        alert("Please fill in all fields.");
        return;
    }

    fetch("/submit", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email, message })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = data.message;
        document.getElementById("contactForm").reset();
    })
    .catch(error => {
        document.getElementById("response").innerText = "Something went wrong.";
        console.error("Error:", error);
    });
});
