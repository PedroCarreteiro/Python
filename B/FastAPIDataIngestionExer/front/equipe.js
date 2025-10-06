async function get_equipes() {
    await axios.get("http://127.0.0.1:8000/api/v1/equipe/").then((response) => {
        const equipes = response.data;
        const container = document.getElementById("equipes")
        equipes.forEach(element => {
            const equipeDiv = document.createElement('div');
            equipeDiv.classList.add("equipe");
            equipeDiv.innerHTML = `
                <h2>${element.nome_equipe}</h2>
                <p>${element.nacionalidade_equipe}</p>
                <p>${element.id}</p>
                <hr>
            `
            container.appendChild(equipeDiv);
        })
    })
}

get_equipes()