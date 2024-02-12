function validateForm() {
    var password = document.getElementById("password").value;
    var confirm_password = document.getElementById("confirm_password").value;

    if (password != confirm_password) {
        document.getElementById("password_match_error").innerHTML = "Passwords not matching";
        return false;
    }

    return true;
}