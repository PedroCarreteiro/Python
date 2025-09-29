// // Fetch

// async function puxando_api(){
//     const response = await fetch("http://127.0.0.1:8000/api/v1/turmas");
//     const data = await response.json();
//     return data;
// }

// async function mostrar_turmas() {
//     const turmas = await puxando_api();
//     const container = document.getElementById("btc-container");
//     turmas.forEach(turma => {
//         const turmaDiv = document.createElement('div');
//         turmaDiv.classList.add("turma");
//         turmaDiv.innerHTML = `
//             <h2>${turma.nome_turma}</h2>
//             <p>${turma.padrinho}</p>
//             <p>${turma.qtd_alunos}</p>
//             <p>${turma.laboratorio}</p>
//         `;
//         container.appendChild(turmaDiv);
//     })
// }

// mostrar_turmas()


async function puxar_api() {
    await axios.get("http://127.0.0.1:8000/api/v1/turmas").then((response) => {
        const turmas = response.data;
        const container = document.getElementById("btc-container")
        turmas.forEach(element => {
        const turmaDiv = document.createElement('div');
        turmaDiv.classList.add("turma");
        turmaDiv.innerHTML = `
            <h2>${element.nome_turma}</h2>
            <p>${element.padrinho}</p>
            <p>${element.qtd_alunos}</p>
            <p>${element.laboratorio}</p>
        `;
        container.appendChild(turmaDiv);
        }) 
    })
}

puxar_api()