function updateDateTime() {
            const now = new Date();
            const options = {
                weekday: 'long',
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            };
            const date = now.toLocaleDateString(undefined, options);
            const time = now.toLocaleTimeString();
            document.getElementById('datetime').innerHTML = `${date} | ${time}`;
        }

        setInterval(updateDateTime, 1000);
        updateDateTime(); // Initial call