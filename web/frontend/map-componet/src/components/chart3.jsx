import React, { Component } from "react";
import Chart from "react-apexcharts";

class Chart3 extends Component {
  constructor(props) {
    super(props);
    this.chartDiv = <span>Click on a topic in the sidebar...</span>;
    this.options = {
      chart: {
        id: "basic-chart",
      },
      dataLabels: {
        enabled: true,
      },
      xaxis: {
        categories: ["Negative", "Neutral", "Positive"],
      },
      stroke: {
        curve: "straight",
      },
      grid: {
        row: {
          colors: ["#f3f3f3", "transparent"], // takes an array which will be repeated on columns
          opacity: 0.5,
        },
      },
    };
    this.series = [];
  }

  componentDidUpdate = (prevProps) => {
    document.querySelector(".ch3wrapper").style.paddingTop = "0%";
    let ENDPOINT;
    switch (this.props.currentLayer) {
      case "recycle":
        ENDPOINT = "http://127.0.0.1:8081/api/tweet/recycling";
        break;
      case "electric":
        ENDPOINT = "http://127.0.0.1:8081/api/tweet/electric_cars";
        break;
      case "solar":
        ENDPOINT = "http://127.0.0.1:8081/api/tweet/solar";
    }
    fetch(ENDPOINT)
      .then((response) => response.json())
      .then((data) => {
        console.log(data)
        data = data["output"];
        this.series = [];
        for (let blk of data) {
          var series = {
            name: blk["region"],
            data: [blk["NEG"], blk["NEU"], blk["POS"]],
          };
          if (this.series.length !== 4) {
            this.series.push(series);
          }
        }
        if (prevProps.currentLayer !== this.props.currentLayer) {
          this.chartDiv = (
            <Chart
              options={this.options}
              series={this.series}
              type="line"
              width="100%"
              height="150%"
            />
          );
          this.setState({}); // force re render
        }
      });
  };

  render() {
    return (
      <div className="box chart2">
        <div className="ch3wrapper">{this.chartDiv}</div>
      </div>
    );
  }
}

export default Chart3;
