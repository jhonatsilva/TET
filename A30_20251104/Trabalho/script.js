// JSON com dados fictícios
const crimeData = [
    { year: 2024, month: "Janeiro", neighborhood: "Centro", crimeType: "furto", count: 120 },
    { year: 2024, month: "Janeiro", neighborhood: "Batel", crimeType: "roubo", count: 80 },
    { year: 2024, month: "Fevereiro", neighborhood: "Água Verde", crimeType: "furto", count: 100 },
    { year: 2024, month: "Março", neighborhood: "Santa Felicidade", crimeType: "outros", count: 50 },
    { year: 2024, month: "Abril", neighborhood: "Boqueirão", crimeType: "furto", count: 90 },
    { year: 2025, month: "Janeiro", neighborhood: "Centro", crimeType: "roubo", count: 110 },
    { year: 2025, month: "Fevereiro", neighborhood: "Batel", crimeType: "outros", count: 70 },
    { year: 2025, month: "Março", neighborhood: "Água Verde", crimeType: "furto", count: 95 },
    { year: 2025, month: "Abril", neighborhood: "Santa Felicidade", crimeType: "roubo", count: 60 },
    { year: 2025, month: "Maio", neighborhood: "Boqueirão", crimeType: "outros", count: 40 },
    { year: 2024, month: "Junho", neighborhood: "Centro", crimeType: "furto", count: 130 },
    { year: 2024, month: "Julho", neighborhood: "Batel", crimeType: "roubo", count: 85 },
    { year: 2024, month: "Agosto", neighborhood: "Água Verde", crimeType: "outros", count: 55 },
    { year: 2024, month: "Setembro", neighborhood: "Santa Felicidade", crimeType: "furto", count: 105 },
    { year: 2024, month: "Outubro", neighborhood: "Boqueirão", crimeType: "roubo", count: 75 },
    { year: 2025, month: "Novembro", neighborhood: "Centro", crimeType: "outros", count: 65 },
    { year: 2025, month: "Dezembro", neighborhood: "Batel", crimeType: "furto", count: 115 },
];

// Função para filtrar os dados com base nos filtros selecionados
function filterData() {
    const year = document.getElementById("year").value;
    const crimeType = document.getElementById("crime-type").value;
    const neighborhood = document.getElementById("neighborhood").value;

    return crimeData.filter(
        (data) =>
            (year === "" || data.year == year) &&
            (crimeType === "" || data.crimeType == crimeType) &&
            (neighborhood === "" || data.neighborhood == neighborhood)
    );
}

// Função para atualizar o gráfico
function updateChart() {
    const filteredData = filterData();
    const labels = filteredData.map((data) => `${data.neighborhood} (${data.month})`);
    const counts = filteredData.map((data) => data.count);

    crimeChart.data.labels = labels;
    crimeChart.data.datasets[0].data = counts;
    crimeChart.update();
}

// Configuração inicial do gráfico
const ctx = document.getElementById("crimeChart").getContext("2d");
const crimeChart = new Chart(ctx, {
    type: "bar",
    data: {
        labels: [],
        datasets: [
            {
                label: "Quantidade de Crimes",
                data: [],
                backgroundColor: "rgba(54, 162, 235, 0.6)",
                borderColor: "rgba(54, 162, 235, 1)",
                borderWidth: 1,
            },
        ],
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: "top",
            },
            title: {
                display: true,
                text: "Quantidade de Crimes por Bairro e Mês",
            },
        },
    },
});

// Adiciona eventos para atualizar o gráfico ao mudar os filtros
document.getElementById("year").addEventListener("change", updateChart);
document.getElementById("crime-type").addEventListener("change", updateChart);
document.getElementById("neighborhood").addEventListener("change", updateChart);