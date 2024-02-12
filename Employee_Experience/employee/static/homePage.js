document.addEventListener('DOMContentLoaded', function() {
    var addRowBtn = document.getElementById('addRowBtn');
    var tableBody = document.querySelector('#jobTable tbody');
    var saveBtn = document.querySelector('button[type="submit"]');

    addRowBtn.addEventListener('click', function() {
        var rowCount = tableBody.querySelectorAll('tr').length;
        var newRow = document.createElement('tr');
        newRow.innerHTML = `
            <td>${rowCount + 1}</td>
            <td><input type="text" name="company_name_${rowCount + 1}"></td>
            <td><input type="text" name="role_${rowCount + 1}"></td>
            <td><input type="date" name="date_of_joining_${rowCount + 1}"></td>
            <td><input type="date" name="last_date_${rowCount + 1}"></td>
            <td><button style="width: 100%; background-color: red;" type="button" class="remove-row">X</button></td>
        `;
        tableBody.appendChild(newRow);
    });

    saveBtn.addEventListener('click', function() {
        var formData = new FormData(document.getElementById('experienceForm'));
        fetch('{% url "homePage" %}', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Data saved successfully:', data);
            
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
    });
});
