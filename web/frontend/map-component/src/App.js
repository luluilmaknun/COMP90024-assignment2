import React, { Component } from 'react'
import './styles.css'
import MapComponent from './components/map'
import AurinDataComponent from './components/AurinMapComponent'
import InfoPanel from './components/info-panel'
import Navbar from './components/navbar'
import Chart1 from './components/chart1'
import Chart2 from './components/chart2'
import Chart3 from './components/chart3'

class App extends Component {
  state = {
    currentLayer: null,
    currentAnalysis: null
  }

  handleAurinClick = e => {
    let currentAnalysis = ''
    currentAnalysis = e.target.value
    this.setState({ currentAnalysis })
  }

  handleClick = category => {
    let currentLayer = ''
    currentLayer = category
    this.setState({ currentLayer })
  }

  render () {
    return (
      <div id='wrapper'>
        <div className='box map'>
          <MapComponent currentLayer={this.state.currentLayer} />
          <Navbar
            currentLayer={this.state.currentLayer}
            handleClick={this.handleClick}
            handleAurinClick={this.handleAurinClick}
          />

          <AurinDataComponent
            currentAnalysis={this.state.currentAnalysis}
            currentLayer={this.state.currentLayer}
          />
        </div>
        <InfoPanel
          currentLayer={this.state.currentLayer}
          currentAnalysis={this.state.currentAnalysis}
        />
        <Chart3 currentLayer={this.state.currentLayer} />
        <Chart2
          currentLayer={this.state.currentLayer}
          currentAnalysis={this.state.currentAnalysis}
        />
      </div>
    )
  }
}

export default App
