import React, { Component } from "react";
import "../styles.css";
import "ol/ol.css";
import "ol-ext/dist/ol-ext.css";
import TileLayer from "ol/layer/Tile";
import { Map, View } from "ol";
import { fromLonLat } from "ol/proj";
import Layer from "ol/layer/Layer";
import VectorLayer from "ol/layer/Vector";
import VectorSource from "ol/source/Vector";
import Source from "ol/source/Source";
import GeoJSON from "ol/format/GeoJSON";
import XYZ from "ol/source/XYZ";
import Style from "ol/style/Style";
import Fill from "ol/style/Fill";
import Stroke from "ol/style/Stroke";
//import Legend from 'ol-ext/control/Legend'
import regionData from "../data/simple.geojson";
import Legend from "ol-ext/legend/Legend";
import Legend_control from "ol-ext/control/Legend";
import { scaleQuantile } from "d3-scale";

class MapComponent extends Component {
  constructor(props) {
    super(props);

    this.map = new Map({
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

    let style = new Style({
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
      style: style
    });

    this.legend = new Legend({
      margin: 0,
      title: "total tweets",
    });
  }

  componentDidMount = () => {
    this.map.setTarget("map-container");
    this.map.addLayer(this.mapLayer);
    this.map.addControl(
      new Legend_control({
        legend: this.legend,
        collapsible: false,
      })
    );
  };

  componentDidUpdate = () => {
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
        data = data["output"];
        var storage = [];
        this.mapLayer
          .getSource()
          .getFeatures()
          .forEach(function (f) {
            for (let d of data) {
              if (String(d.region) == f.getProperties()["Area"].toLowerCase()) {
              
                f.set("pos", d.POS);
                f.set("neu", d.NEU);
                f.set("neg", d.NEG);
                f.set("total", d._TOTAL);
                storage.push(d._TOTAL);
                
              }
            }
          });

        var colour_scale = scaleQuantile()
          .domain(storage)
          .range(["#ffff0050", "#ff7f0050", "#ff000050"]);

        let chloro = (colour_scale) => {
          return function (feature) {
            (feature.getProperties())
            let fill = new Fill();
            let num = parseFloat(feature.getProperties()['total']).toFixed(2);
            fill.setColor(colour_scale(num));
            return new Style({
              fill: fill,
              stroke: new Stroke({
                color: "black",
              }),
            });
          };
        };
        (colour_scale.quantiles())
        this.mapLayer.setStyle(chloro(colour_scale));
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
      });
  };

  render() {
    return <div id="map-container"></div>;
  }
}
export default MapComponent;
