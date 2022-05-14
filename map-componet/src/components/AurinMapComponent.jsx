import React, { Component } from "react";
import XYZ from "ol/source/XYZ";
import VectorLayer from "ol/layer/Vector";
import VectorSource from "ol/source/Vector";
import { Map, View } from "ol";
import { fromLonLat } from "ol/proj";
import GeoJSON from "ol/format/GeoJSON";
import TileLayer from "ol/layer/Tile";
import Legend from "ol-ext/legend/Legend";
import Legend_control from "ol-ext/control/Legend";
import regionData from "../data/simple.geojson";
import Style from "ol/style/Style";
import Fill from "ol/style/Fill";
import Stroke from "ol/style/Stroke";
import { scaleQuantile } from "d3-scale";

class AurinDataComponent extends Component {
  constructor(props) {
    super(props);
    this.aurinMap = new Map({
      target: null,
      layers: [
        new TileLayer({
          source: new XYZ({
            url: "https://{1-4}.basemaps.cartocdn.com/rastertiles/light_all/{z}/{x}/{y}.png",
          }),
          visible: true,
          title: "Carto Light",
        }),
      ],
      view: new View({
        center: fromLonLat([144.9, -38.0]),
        extent: [15673240.6666, -4856130.3986, 16755588.9871, -4179815.5723],
        zoom: 8,
      }),
    });

    this.style = new Style({
      fill: new Fill({
        color: "rgba(193, 229, 232,0.4)",
      }),
      stroke: new Stroke({
        color: "rgb(2, 120, 204)",
      }),
    });

    this.mapLayer = new VectorLayer({
      source: new VectorSource({
        url: regionData,
        format: new GeoJSON(),
      }),
      style: this.style
    });

    this.legend = new Legend({
      margin: 0,
      title: "Aurin Analysis",
    });
  }

  componentDidMount = () => {
    this.aurinMap.setTarget("aurin-component");
    this.aurinMap.addLayer(this.mapLayer);
    this.aurinMap.addControl(
      new Legend_control({
        legend: this.legend,
        collapsible: false,
      })
    );
  };

  componentDidUpdate = (prevProps) => {
   
    if (this.props.currentLayer !== prevProps.currentLayer) {
      this.mapLayer.setStyle(this.style)
      this.legend.setTitle('Aurin Analysis')
      this.legend.getItems().clear()
    }
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
        var analysis = this.props.currentAnalysis;
        var storage = [];
        var json = data["aurin"]["result"];
        this.mapLayer
          .getSource()
          .getFeatures()
          .forEach((f) => {
            Object.keys(json).forEach((k) => {
              if (f.getProperties()["Area"].toLowerCase() == k) {
                f.set(analysis, json[k][analysis]);
                storage.push(json[k][analysis]);
              }
            });
          });
        var colour_scale = scaleQuantile()
          .domain(storage)
          .range(["#ffff0050", "#ff7f0050", "#ff000050"]);

        let chloro = (colour_scale, analysis) => {
          return function (feature) {
            let fill = new Fill();
            let num = parseFloat(feature.getProperties()[analysis]).toFixed(2);
            fill.setColor(colour_scale(num));
            return new Style({
              fill: fill,
              stroke: new Stroke({
                color: "black",
              }),
            });
          };
        };
        if (prevProps.currentAnalysis !== this.props.currentAnalysis) {
          this.mapLayer.setStyle(chloro(colour_scale, analysis));
          this.legend.setTitle(analysis);
          if (this.legend.getItems().getArray().length !== 3) {
            this.legend.addItem({
              title: " < " + parseFloat(colour_scale.quantiles()[0]).toFixed(3),
              typeGeom: "polygon",
              style: new Style({
                fill: new Fill({
                  color: "yellow",
                }),
              }),
            });
            this.legend.addItem({
              title:
                " > " +
                parseFloat(colour_scale.quantiles()[0]).toFixed(3) +
                " & " +
                " < " +
                parseFloat(colour_scale.quantiles()[1]).toFixed(3),
              typeGeom: "polygon",
              style: new Style({
                fill: new Fill({
                  color: "orange",
                }),
              }),
            });
            this.legend.addItem({
              title: " > " + parseFloat(colour_scale.quantiles()[1]).toFixed(3),
              typeGeom: "polygon",
              style: new Style({
                fill: new Fill({
                  color: "red",
                }),
              }),
            });
          }
        }
      });
  };

  render() {
    return <div id="aurin-component"></div>;
  }
}

export default AurinDataComponent;
