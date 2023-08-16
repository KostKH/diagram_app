$(function () {

    var barOptions = {
        responsive: true
    };
    let data_element = document.getElementById("plan_fact_data").innerHTML;
    let plan_fact = JSON.parse(data_element);
    let canvases = document.getElementsByClassName("chartjs-render-monitor");
    for (let el of canvases) {
        let ctx2 = el.getContext("2d");
        let city = el.id
        let barData = {
            labels: plan_fact[city]['year'],
            datasets: [
                {
                    label: "План",
                    backgroundColor: 'rgba(220, 220, 220, 0.5)',
                    pointBorderColor: "#fff",
                    data: plan_fact[city]['plan']
                },
                {
                    label: "Факт",
                    backgroundColor: 'rgba(26,179,148,0.5)',
                    borderColor: "rgba(26,179,148,0.7)",
                    pointBackgroundColor: "rgba(26,179,148,1)",
                    pointBorderColor: "#fff",
                    data: plan_fact[city]['fact']
                }
            ]
        };
        new Chart(ctx2, {type: 'bar', data: barData, options:barOptions});
    };
});
