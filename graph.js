// Graph for Big O Notation blog post
// Rachel Curry
// March 7th, 2025

const xValues = [50,60,70,80,90,100,110,120,130,140,150];
const yValues = [7,8,8,9,9,9,10,11,14,14,15];

const bigOGraph = new Chart("bigOGraph", {
    type: "line",
    data: {
        labels: xValues,
        datasets: [{
          fill: false,
          pointRadius: 1,
          borderColor: "rgba(255,0,0,0.5)",
          data: yValues
        }]
      }
});