document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('#contactForm');
    const alertContainer = document.querySelector('#alert-container');

    if (form) {
        form.addEventListener('submit', function (event) {
            event.preventDefault(); // Evita el envío por defecto del formulario

            const formData = new FormData(form);

            fetch('http://127.0.0.1:8000/crear_mensaje/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': getCookie('csrftoken') // Incluye el token CSRF para seguridad
                }
            })
            .then(response => response.json())
            .then(data => {
                showAlert('Mensaje enviado exitosamente', 'success');
                form.reset(); // Opcional: limpia el formulario después del envío
            })
            .catch(error => {
                console.error('Error:', error);
                showAlert('Hubo un problema al enviar el mensaje.', 'danger');
            });
        });
    }

    function showAlert(message, type) {
        // Limpiar cualquier alerta existente
        alertContainer.innerHTML = '';

        // Crear una nueva alerta
        const alert = document.createElement('div');
        alert.className = `alert alert-${type}`;
        alert.role = 'alert';
        alert.textContent = message;

        // Agregar la alerta al contenedor
        alertContainer.appendChild(alert);

        // Opcional: Ocultar la alerta después de unos segundos
        setTimeout(() => {
            alert.remove();
        }, 5000);
    }

    // Función para obtener el token CSRF de las cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
