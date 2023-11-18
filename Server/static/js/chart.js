function renderChart(ctx, chartData, chartTitle) {



    // Sample data
    // const chartData = {{ chart_data | safe }};
    // const chartTitle = "{{ chart_title|safe }}";

    // ... (其余的JavaScript代码，不需要改变)

    // Render the chart
    const chart = new Chart(ctx, {
        type: "line",
        data: {
            datasets: [
                {
                    label: chartTitle,
                    data: chartData,
                    fill: false,
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.3
                },
            ],
        },
        options: {
            responsive: true,
            scales: {
                xAxes: [
                    {
                        type: "time",
                        time: {
                            unit: "day",
                            round: "day",
                            displayFormats: {
                                day: "MMM D",
                            },
                        },
                    },
                ],
                yAxes: [
                    {
                        ticks: {
                            beginAtZero: true,
                        },
                    },
                ],
            },
        },
    });

}
