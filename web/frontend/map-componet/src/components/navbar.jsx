import React, { Component } from "react";
import car from "../assets/assets/electric-car (1).png";
import solar from "../assets/assets/solar-panel (1).png";
import rcycle from "../assets/assets/triangular-arrows-sign-for-recycle (1).png";
import compassAll from "../assets/assets/compass-assets/all.png";
import compassN from "../assets/assets/compass-assets/N.png";
import compassE from "../assets/assets/compass-assets/E.png";
import compassS from "../assets/assets/compass-assets/S.png";
import compassW from "../assets/assets/compass-assets/W.png";
import whiteCar from "../assets/white trial/electric-car (3).png";
import whiteSolar from "../assets/white trial/solar-panel (4).png";
import whiteRcycle from "../assets/white trial/rcyclew.png";

class Navbar extends Component {
  constructor(props) {
    super(props);

    this.carPic = car;
    this.solarPic = solar;
    this.recycuclePic = rcycle;
    this.compassCurrent = compassAll;
    this.defaultOption = "aurin analytic";
    this.analysis1 = "";
    this.analysis2 = "";
  }

  componentDidUpdate = (prevProps) => {
    switch (this.props.currentLayer) {
      case "solar":
        this.analysis1 = "perha_solar_installation";
        this.analysis2 = "perperson_solar_installation";
        break;
      case "electric":
        this.analysis1 = "total_dwelings_with_mv";
        this.analysis2 = "perperson_mv";
        break;
      case "recycle":
        this.analysis1 = "percentage_national_parks";
        this.analysis2 = "ratio_agriculture_per_population";
    }

    switch (this.props.currentRegion) {
      case "North":
        this.compassCurrent = compassN;
        break;
      case "East":
        this.compassCurrent = compassE;
        break;
      case "South":
        this.compassCurrent = compassS;
        break;
      case "West":
        this.compassCurrent = compassW;
        break;
      default:
        this.compassCurrent = compassAll;
    }
    if (prevProps.currentLayer !== this.props.currentLayer) {
      this.value = this.defaultOption;
      var selEl = document.getElementById("selectbox");
      selEl.options[0].selected = true;
      this.setState({});
    }
  };

  changeEvent = (e) => {
    this.props.handleAurinClick(e);
    this.value = e.target.value;
    this.setState({});
  };

  render() {
    return (
      <div id="map-sidebar">
        <div id="select-list-wrapper">
          <select id="selectbox" onChange={(e) => this.changeEvent(e)}>
            <option value={this.defaultOption}>{this.defaultOption}</option>
            <option value={this.analysis1}>{this.analysis1}</option>
            <option value={this.analysis2}>{this.analysis2}</option>
          </select>
        </div>
        <ul id="legend">
          <li>
            <img
              src={this.carPic}
              onClick={() => {
                this.handleImgClick("car");
                this.props.handleClick("electric");
              }}
            />
          </li>
          <li>
            <img
              src={this.solarPic}
              onClick={() => {
                this.handleImgClick("solar");
                this.props.handleClick("solar");
              }}
            />
          </li>
          <li className="list-rc">
            <img
              src={this.recycuclePic}
              onClick={() => {
                this.handleImgClick("recycle");
                this.props.handleClick("recycle");
              }}
            />
          </li>
        </ul>
        <div className="compass-wrapper">
          <img src={this.compassCurrent} alt="" />
        </div>
      </div>
    );
  }

  handleImgClick = (type) => {
    if ("car" == type) {
      this.carPic = whiteCar;
    } else {
      this.carPic = car;
    }
    if ("solar" == type) {
      this.solarPic = whiteSolar;
    } else {
      this.solarPic = solar;
    }
    if ("recycle" == type) {
      this.recycuclePic = whiteRcycle;
    } else {
      this.recycuclePic = rcycle;
    }
  };
}

export default Navbar;
