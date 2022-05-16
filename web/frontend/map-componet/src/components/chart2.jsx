import React, { Component } from "react";
import Chart from "react-apexcharts";

class Chart2 extends Component {
  constructor(props) {
    super(props);

    this.chartDiv2 = (
      <span>
        Click on the Aurin data drop down... 
      </span>
    );
    this.options = {
      chart: {
        type: "bar",
        height: 350,
      },
      plotOptions: {
        bar: {
          borderRadius: 4,
          horizontal: true,
        },
      },
      dataLabels: {
        enabled: true,
      },
      legend: {
        show: false,
      },
      tooltip: {
        enabled: false,
      },
      xaxis: {
        categories: ["east", "north", "south", "west"],
      },
    };

    this.series = [];
  }

  com

  componentDidUpdate = (prevProps) => {
    this.chartDiv2 = ''
    document.querySelector(".ch2wrapper").style.paddingTop = "0%";
    let ENDPOINT;
    switch (this.props.currentLayer) {
      case "recycle":
        ENDPOINT = "http://backend-service:8081/api/tweet/recycling";
        break;
      case "electric":
        ENDPOINT = "http://backend-service:8081/api/tweet/electric_cars";
        break;
      case "solar":
        ENDPOINT = "http://backend-service:8081/api/tweet/solar";
    }
    fetch(ENDPOINT)
      .then((response) => response.json())
      .then((data) => {
        var analysis = this.props.currentAnalysis;
        var json = data["aurin"]["result"];
        this.series = [];
        var dataStore = [];
        Object.keys(json).forEach((k) => {
          let data = {
            data: [{ x: k, y: parseFloat(json[k][analysis]).toFixed(2) }],
          };
          this.series.push(data);
        });

        if (prevProps.currentAnalysis !== this.props.currentAnalysis) {
          this.chartDiv2 = (
            <Chart
              options={this.options}
              series={this.series}
              type="bar"
              width="100%"
              height="150%"
            />
          );
          this.setState({});
        }
      });
  };

  render() {
    return (
      <div className="box chart3">
        <div className="ch2wrapper">{this.chartDiv2}</div>
      </div>
    );
  }
}
export default Chart2;
