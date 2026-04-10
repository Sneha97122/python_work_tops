function validateForm() {
    let phone = document.getElementById("phone").value;
    let email = document.getElementById("email").value;

    if (phone.length !== 10) {
        alert("Phone must be 10 digits");
        return false;
    }

    if (!email.includes("@")) {
        alert("Enter valid email");
        return false;
    }

    return true;
}
