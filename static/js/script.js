document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');

    async function performAction(url, alertInsert, alertResponse, showInput) {
        try {
            // Mostrar alerta de inserción antes de la petición
            await Swal.fire({
                icon: 'info',
                title: alertInsert,
                showConfirmButton: false,
                timer: 800
            });

            const formData = new FormData(form);
            const response = await fetch(url, {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                throw new Error(`Error HTTP: ${response.status}`);
            }

            const data = await response.json();
            const inputElement = document.querySelector(showInput);
            if (inputElement && inputElement instanceof HTMLInputElement) {
                inputElement.value = data.count;
            }

            await Swal.fire({
                icon: 'success',
                title: alertResponse,
                showConfirmButton: false,
                timer: 1500
            });
        } catch (error) {
            console.error('Error:', error);
            await Swal.fire({
                icon: 'error',
                title: 'Error: intente nuevamente',
                showConfirmButton: false,
                timer: 1500
            });
        }
    }

    // MySQL
    window.mysql_lmd = function () {
        performAction(
            "/insert_ldm/mysql",
            '¡Insertando registros MySQL!',
            '¡Registros insertados MySQL!',
            '#txt_mysqlLMD'
        );
    };

    window.mysql_sp = function () {
        performAction(
            "/insert_sp/mysql",
            '¡Insertando registros MySQL SP!',
            '¡Registros insertados MySQL SP!',
            '#txt_mysqlSP'
        );
    };

    // PostgreSQL
    window.postgres_lmd = function () {
        performAction(
            "/insert_ldm/postgres",
            '¡Insertando registros PostgreSQL!',
            '¡Registros insertados PostgreSQL!',
            '#txt_pgLMD'
        );
    };

    window.postgres_sp = function () {
        performAction(
            "/insert_sp/postgres",
            '¡Insertando registros PostgreSQL SP!',
            '¡Registros insertados PostgreSQL SP!',
            '#txt_postgresSP'
        );
    };

    // Oracle
    window.oracle_lmd = function () {
        performAction(
            "/insert_ldm/oracle",
            '¡Insertando registros Oracle!',
            '¡Registros insertados Oracle!',
            '#txt_oracleLMD'
        );
    };

    window.oracle_sp = function () {
        performAction(
            "/insert_sp/oracle",
            '¡Insertando registros Oracle SP!',
            '¡Registros insertados Oracle SP!',
            '#txt_oracleSP'
        );
    };

    // SQL Server
    window.sqlserver_lmd = function () {
        performAction(
            "/insert_ldm/sqlserver",
            '¡Insertando registros SQL Server!',
            '¡Registros insertados SQL Server!',
            '#txt_sqlserverLMD'
        );
    };

    window.sqlserver_sp = function () {
        performAction(
            "/insert_sp/sqlserver",
            '¡Insertando registros SQL Server SP!',
            '¡Registros insertados SQL Server SP!',
            '#txt_sqlserverSP'
        );
    };
});

