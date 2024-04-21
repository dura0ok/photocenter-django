import Toastify from 'toastify-js';

import 'toastify-js/src/toastify.css';

export const showErrorToast = (message) => {
    Toastify({
        text: message,
        duration: 3000,
        close: true,
        gravity: 'top',
        position: 'left',
        backgroundColor: 'red',
        stopOnFocus: true,
    }).showToast();
}