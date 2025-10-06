async function get_equipes() {
    await axios.get("http://127.0.0.1:8000/api/v1/carro/").then((response) => {
        const equipes = response.data;
        const container = document.getElementById("carros")
        equipes.forEach(element => {
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

get_equipes()