// async function puxando_api() {
//     const response = await fetch("http://localhost:8000/api/v1/bandas");
//     const data = await response.json();
//     return data;
// }

// async function mostarr_banda() {
//     const bandas = await puxando_api();
//     const container = document.getElementById("bandasContainer");

//     bandas.fotEach(banda => {
    //         const bandaDiv = document.createElement('div');
//         bandaDiv.classList.add('banda');
//         bandaDiv.innerHTML = `
//         <h2>${banda.nome}</h2>
//         <p>${banda.qnt_integrantes}</p>
//         <p>${banda.tipo_musical}</p>
//         `;

//         container.appendChild(bandaDiv);
//     });
// }

// mostrar_banda()

//função para puxar api
async function puxar_api() {
    try {
        const response = await axios.get("http://localhost:8000/api/v1/bandas");
        const bandas = response.data;
        const container = document.getElementById("bandasContainer");

        bandas.forEach(element => {
            const bandaDiv = document.createElement('div');
            bandaDiv.classList.add('banda');
            bandaDiv.innerHTML = `
                <h2>${element.nome}</h2>
                <p>Integrantes: ${element.qnt_integrantes}</p>
                <p>Estilo: ${element.tipo_musical}</p>
            `;
            container.appendChild(bandaDiv);
        });

    } catch (error) {
        console.error("Erro ao puxar API:", error);
    }
}

// Chama a função assim que o script carregar
puxar_api();
