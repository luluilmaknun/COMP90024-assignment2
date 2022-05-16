import React, { Component } from "react";
import descs from "../data/layerDescs/layerDescs.json";

class InfoPanel extends Component {
  constructor(props) {
    super(props);
    this.layerTitle = "Select a topic🍀";
    this.aurinDesc = "Select an Aurin analytic🍃";
    this.bodyText = "";
    this.bodyAurinText = "";
  }

  componentDidUpdate = (prevProps) => {
    let ENDPOINT;
    switch (this.props.currentLayer) {
      case "recycle":
        ENDPOINT = "http://backend-service:8081/api/tweet/recycling";
        this.layerTitle = "Recycling";
        break;
      case "electric":
        ENDPOINT = "http://backend-service:8081/api/tweet/electric_cars";
        this.layerTitle = "Electric Vehicles";
        break;
      case "solar":
        ENDPOINT = "http://backend-service:8081/api/tweet/solar";
        this.layerTitle = "Renewable Energy";
        break;
    }
    fetch(ENDPOINT)
      .then((response) => response.json())
      .then((data) => {
        for (let d of descs) {
          let dStr = JSON.stringify(d["name"]);
          if (dStr.includes(this.props.currentLayer)) {
            this.bodyText = d["body"];
          }
        }
        // prevent infinite loop re render
        if (prevProps.currentLayer !== this.props.currentLayer) {
          this.setState({});
        }
        if (prevProps.currentAnalysis !== this.props.currentAnalysis) {
          switch (this.props.currentAnalysis) {
            case "total_dwelings_with_mv":
              this.aurinDesc = "total dwellings with a motor vehicle";
              break;
            case "perperson_mv":
              this.aurinDesc = "Motor vehicles per person";
              break;
            case "perha_solar_installation":
              this.aurinDesc = "per hectare solar installations";
              break;
            case "perperson_solar_installation":
              this.aurinDesc = "Solar installations per person";
              break;
            case "percentage_national_parks":
              this.aurinDesc = "nationals parks percentage";
              break;
            case "ratio_agriculture_per_population":
              this.aurinDesc = "ratio of agriculture per population";
              break;
          }
          data = data["aurin"]["description"][this.props.currentAnalysis];
          this.bodyAurinText = data;
          this.setState({});
        } else {
          this.aurinDesc = "Select an Aurin analytic🍃";
          this.bodyAurinText = "";
        }
      });
  };

  render() {
    return (
      <div className="info-panel">
        <div className="infoTitle">
          <h3>{this.layerTitle}</h3>
        </div>
        <div className="spanWrap">
          <span>{this.bodyText}</span>
        </div>

        <div className="aurinTitle">
          <h3>{this.aurinDesc}</h3>
        </div>
        <div className="spanWrap">
          <span>{this.bodyAurinText}</span>
        </div>
      </div>
    );
  }
}

export default InfoPanel;
