// script.js
document.addEventListener('DOMContentLoaded', () => {
    const rows = document.querySelectorAll('table tr[data-id]');
    rows.forEach(row => {
        row.addEventListener('click', () => {
            const expense = row.dataset.name;
            alert(`You clicked on expense: ${expense}`);
        });
    });
});