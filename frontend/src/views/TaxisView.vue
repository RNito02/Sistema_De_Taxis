<template class="TaxisView">
    <div class="card">
        <div class="container">
            <table id="miTabla" class="display">
                <thead>
                    <tr>
                        <th v-for="header in headers" :key="header.value">{{ header.text }}</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in datosDeTuApi" :key="item.id">
                        <td>{{ item.matricula }}</td>
                        <td>{{ item.conductor }}</td>
                        <td>{{ item.colonia }}</td>
                        <td>{{ item.numero_taxi }}</td>
                        <td>{{ item.ubicacion_actual }}</td>
                        <td>{{ item.disponibilidad }}</td>
                        <td>{{ item.telefono }}</td>
                        <td>{{ item.genero }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import 'datatables.net-bs4';
import 'datatables.net-bs4/css/dataTables.bootstrap4.css';

import $ from 'jquery';

export default {
    data() {
        return {
            headers: [
                { text: 'Matricula', value: 'matricula' },
                { text: 'Conductor', value: 'conductor' },
                { text: 'Colonia', value: 'colonia' },
                { text: 'Numero Taxi', value: 'numero_taxi' },
                { text: 'Ubicacion Actual', value: 'ubicacion_actual' },
                { text: 'Disponibilidad', value: 'disponibilidad' },
                { text: 'Telefono', value: 'telefono' },
                { text: 'Genero', value: 'genero' },
            ],
            datosDeTuApi: [],
        };
    },
    mounted() {
        axios.get('http://127.0.0.1:8000/get_all_taxis').then(response => {
            this.datosDeTuApi = response.data;
            console.log(this.datosDeTuApi); // Verifica los datos en la consola

            $(this.$el).find('table').DataTable({
                searching: true, // Asegúrate de habilitar la búsqueda
                // Otras opciones de configuración aquí
            });
        });
    },
    beforeDestroy() {
        $(this.$el).find('table').DataTable().destroy();
    },
};
</script>

  
<style>
/* Puedes agregar estilos personalizados aquí si es necesario */
</style>
  