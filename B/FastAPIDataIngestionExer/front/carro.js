async function get_carros() {
    await axios.get("http://127.0.0.1:9000/api/v1/carro/").then((response) => {
        const carro = response.data;
        const container = document.getElementById("carros")
        carro.forEach(element => {
            const carroDiv = document.createElement('div');
            carroDiv.classList.add("carro");
            carroDiv.innerHTML = `
                <h2>${element.modelo_carro}</h2>
                <p>${element.montadora}</p>
                <p>${element.potencia}</p>
                <p>${element.unidade_potencia}</p>
                <p>ID: ${element.id}</p>
                <p>Equipe: ${element.id_equipe}</p>
                <hr>
            `
            container.appendChild(carroDiv);
        })
    })
}

get_carros()