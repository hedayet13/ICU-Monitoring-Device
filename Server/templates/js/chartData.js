


var ctx1 = document.getElementById('myChart1').getContext('2d');
var ctx2= document.getElementById('myChart2').getContext('2d');
var ctx3 = document.getElementById('myChart3').getContext('2d');
var ctx4 = document.getElementById('myChart4').getContext('2d');
var ctx5 = document.getElementById('myChart5').getContext('2d');
var ctx6= document.getElementById('myChart6').getContext('2d');
var ctx7 = document.getElementById('myChart7').getContext('2d');
var ctx8 = document.getElementById('myChart8').getContext('2d');
var getData = $.get('/chartData');
getData.done(function (msg) {
        console.log(msg)
        var results= msg["data"]
        var myLineChart1 = new Chart(ctx1, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: results[0][2],
            datasets: [{
                label: 'Heart_Rate(BPM)',
                // backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: results[0][0]
            }]
        },
            options:{
            responsive: true,
                title:{
                    display: true,
                    text: "BED: 1 ",
                    fontSize: 15
                },
            scales:{
                yAxes:[
                    {
                        ticks:{
                            beginAtZero:true,
                            suggestedMax: 120
                        }
                    }
                ],
                xAxes:[{
                    ticks: {
                        display:false
                    }
                }]
            }
            }

        // Configuration options go here

    });
        var myLineChart2 = new Chart(ctx2, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: results[1][2],
            datasets: [{
                label: 'Heart_Rate(BPM)',
                // backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: results[1][0]
            },]
        },
            options:{
            responsive: true,
                title:{
                    display: true,
                    text: "BED: 2 ",
                    fontSize: 15
                },
            scales:{
                yAxes:[
                    {
                        ticks:{
                            beginAtZero:true,
                            suggestedMax: 120
                        }
                    }
                ],
                xAxes:[{
                    ticks: {
                        display:false
                    }
                }]
            }
            }

        // Configuration options go here

    });
        var myLineChart3 = new Chart(ctx3, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: results[2][2],
            datasets: [{
                label: 'Heart_Rate(BPM)',
                // backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: results[2][0]
            }]
        },
            options:{
            responsive: true,
                title:{
                    display: true,
                    text: "BED: 3 ",
                    fontSize: 15
                },
            scales:{
                yAxes:[
                    {
                        ticks:{
                            beginAtZero:true,
                            suggestedMax: 120
                        }
                    }
                ],
                xAxes:[{
                    ticks: {
                        display:false
                    }
                }]
            }
            }

        // Configuration options go here

    });
        var myLineChart4 = new Chart(ctx4, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: results[3][2],
            datasets: [{
                label: 'Heart_Rate(BPM)',
                // backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: results[3][0]
            }]
        },
            options:{
            responsive: true,
                title:{
                    display: true,
                    text: "BED: 4 ",
                    fontSize: 15
                },
            scales:{
                yAxes:[
                    {
                        ticks:{
                            beginAtZero:true,
                            suggestedMax: 120
                        }
                    }
                ],
                xAxes:[{
                    ticks: {
                        display:false
                    }
                }]
            }
            }

        // Configuration options go here

    });
        var myLineChart5 = new Chart(ctx5, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: results[4][2],
            datasets: [{
                label: 'Heart_Rate(BPM)',
                // backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: results[4][0]
            }]
        },
            options:{
            responsive: true,
                title:{
                    display: true,
                    text: "BED: 5 ",
                    fontSize: 15
                },
            scales:{
                yAxes:[
                    {
                        ticks:{
                            beginAtZero:true,
                            suggestedMax: 120
                        }
                    }
                ],
                xAxes:[{
                    ticks: {
                        display:false
                    }
                }]
            }
            }

        // Configuration options go here

    });
        var myLineChart6 = new Chart(ctx6, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: results[5][2],
            datasets: [{
                label: 'Heart_Rate(BPM)',
                // backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: results[5][0]
            }]
        },
            options:{
            responsive: true,
                title:{
                    display: true,
                    text: "BED: 6 ",
                    fontSize:15
                },
            scales:{
                yAxes:[
                    {
                        ticks:{
                            beginAtZero:true,
                            suggestedMax: 120
                        }
                    }
                ],
                xAxes:[{
                    ticks: {
                        display:false
                    }
                }]
            }
            }

        // Configuration options go here

    });
        var myLineChart7 = new Chart(ctx7, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: results[6][2],
            datasets: [{
                label: 'Heart_Rate(BPM)',
                // backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: results[6][0]
            }]
        },
            options:{
            responsive: true,
                title:{
                    display: true,
                    text: "BED: 7 ",
                    fontSize: 15
                },
            scales:{
                yAxes:[
                    {
                        ticks:{
                            beginAtZero:true,
                            suggestedMax: 120
                        }
                    }
                ],
                xAxes:[{
                    ticks: {
                        display:false
                    }
                }]
            }
            }

        // Configuration options go here

    });
        var myLineChart8 = new Chart(ctx8, {
        // The type of chart we want to create
        type: 'line',

        // The data for our dataset
        data: {
            labels: results[7][2],
            datasets: [{
                label: 'Heart_Rate(BPM)',
                // backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: results[7][0]
            }]
        },
            options:{
            responsive: true,
                title:{
                    display: true,
                    text: "BED: 8 ",
                    fontSize:15
                },
            scales:{
                yAxes:[
                    {
                        ticks:{
                            beginAtZero:true,
                            suggestedMax: 120
                        }
                    }
                ],
                xAxes:[{
                    ticks: {
                        display:false
                    }
                }]
            }
            }

        // Configuration options go here

    });

});