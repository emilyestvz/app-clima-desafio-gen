const form = document.getElementById('clima-form');
const resultado = document.getElementById('resultado');
form.onsubmit = async (e) => {
    e.preventDefault();
    resultado.innerHTML = '';
    const cidade = document.getElementById('cidade').value;
    try {
        const resp = await fetch('/clima', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cidade })
        });
        const data = await resp.json();
        if (data.erro) {
            resultado.innerHTML = `<div class='erro'>${data.erro}</div>`;
        } else if (data.opcoes) {
            // Se houver múltiplas cidades, mostra opções para o usuário escolher
            resultado.innerHTML = `<div class='result-box'><h2>Escolha a cidade:</h2>` +
                data.opcoes.map((op, i) =>
                    `<button class='cidade-opcao' data-lat='${op.latitude}' data-lon='${op.longitude}'>${op.name}${op.admin1 ? ', ' + op.admin1 : ''}${op.country ? ', ' + op.country : ''}</button>`
                ).join('<br>') + '</div>';
            document.querySelectorAll('.cidade-opcao').forEach(btn => {
                btn.onclick = async () => {
                    const lat = btn.getAttribute('data-lat');
                    const lon = btn.getAttribute('data-lon');
                    // Nova requisição passando lat/lon
                    const resp2 = await fetch('/clima', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ cidade, lat, lon })
                    });
                    const data2 = await resp2.json();
                    resultado.innerHTML = `
                        <div class="result-box">
                            <h2>Resultado ☀️</h2>
                            <p>🌆 <b>Cidade:</b> ${data2.cidade}</p>
                            <p>🌡️ <b>Temperatura:</b> ${data2.temperatura}°C</p>
                            <p>💨 <b>Vento:</b> ${data2.vento} km/h</p>
                            <p>☁️ <b>Condição:</b> ${data2.condicao} ${data2.cache ? '(cache)' : ''}</p>
                        </div>
                    `;
                };
            });
        } else {
            resultado.innerHTML = `
                <div class="result-box">
                    <h2>Resultado ☀️</h2>
                    <p>🌆 <b>Cidade:</b> ${data.cidade}</p>
                    <p>🌡️ <b>Temperatura:</b> ${data.temperatura}°C</p>
                    <p>💨 <b>Vento:</b> ${data.vento} km/h</p>
                    <p>☁️ <b>Condição:</b> ${data.condicao} ${data.cache ? '(cache)' : ''}</p>
                </div>
            `;
        }
    } catch (err) {
        resultado.innerHTML = `<div class='erro'>Erro ao buscar clima.</div>`;
    }
};
