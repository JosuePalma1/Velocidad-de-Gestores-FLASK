function deleteRecords(url) {
    // Mostrar mensaje de confirmación antes de eliminar
    Swal.fire({
        title: '¿Está seguro?',
        text: "¡No podrá revertir esta acción!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminar',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            // Realizar la petición DELETE
            fetch(url, { 
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    Swal.fire({
                        icon: 'success',
                        title: '¡Registros eliminados!',
                        text: 'Los registros han sido eliminados correctamente.',
                        showConfirmButton: false,
                        timer: 1500
                    }).then(() => {
                        // Recargar los contadores o actualizar la UI según sea necesario
                        location.reload();
                    });
                } else {
                    throw new Error('Error al eliminar registros');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                Swal.fire({
                    icon: 'error',
                    title: 'Error al eliminar',
                    text: 'No se pudieron eliminar los registros. Por favor, intente nuevamente.',
                    showConfirmButton: true
                });
            });
        }
    });
}

// Status check function con mejor manejo de errores
function checkStatus(url, name) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (data.status) {
                Swal.fire({
                    title: name,
                    text: '¡Conexión establecida con éxito!',
                    icon: 'success',
                    timer: 1500
                });
            } else {
                throw new Error('Connection failed');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            Swal.fire({
                title: name,
                text: 'Error al conectar con la base de datos',
                icon: 'error',
                showConfirmButton: true
            });
        });
}

// Event Listeners
document.addEventListener('DOMContentLoaded', function () {
    // Status check event listeners
    const statusButtons = {
        'mysql_statu': 'MySQL',
        'postgres_statu': 'PostgreSQL',
        'oracle_statu': 'Oracle',
        'sqlserver_statu': 'SQL Server'
    };

    Object.entries(statusButtons).forEach(([id, name]) => {
        document.getElementById(id)?.addEventListener('click', () => {
            checkStatus(`/test_connection/${id.split('_')[0]}`, name);
        });
    });

    // Delete functions
    window.delete_mysql = () => deleteRecords('/delete/mysql');
    window.delete_postgres = () => deleteRecords('/delete/postgres');
    window.delete_oracle = () => deleteRecords('/delete/oracle');
    window.delete_sqlserver = () => deleteRecords('/delete/sqlserver');
});