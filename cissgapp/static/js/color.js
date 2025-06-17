document.addEventListener('DOMContentLoaded', function () {
    const today = new Date().toISOString().split('T')[0]; // Format: YYYY-MM-DD
    const rows = document.querySelectorAll('tr.date-row');

    rows.forEach(row => {
      const endDateInput = row.querySelector('input[name="end_date"]');
      if (!endDateInput) return;

      const endDate = endDateInput.value;

      if (endDate < today) {
        row.classList.add('table-info'); // Before today
      } else if (endDate === today) {
        row.style.backgroundColor = 'yellow'; // Equal to today
      } else if (endDate > today) {
        row.classList.add('table-danger'); // After today
      }
    });
  });