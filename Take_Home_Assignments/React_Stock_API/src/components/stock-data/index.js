
import React, { Component } from "react";
import "./index.css";

export default class StockData extends Component {
  constructor(props) {
    super(props);
    this.state = {
      input : "",
      data : {},
      fetch_count: 0
    }
  }

  handleChange = (e) => {
    this.setState({input: e.target.value})
  }

  trim = (input) => {
    let start = 0
    while (input[start] === '0') start++
    return input.substring(start)
  }

  handleUpdate = () =>  {
    const input = this.trim(this.state.input)
    const url = `https://jsonmock.hackerrank.com/api/stocks?date=${input}`
    fetch(url).then(res => res.json()).then(data => {
      this.setState(
        {data: data.data.length ? data.data[0] : {},
        fetch_count: this.state.fetch_count+1
      })
    })
  }

  render() {
    const has_result = this.state.fetch_count && !this.state.data.open ? (<div className="mt-50 slide-up-fade-in" id="no-result" data-testid="no-result">"No Results Found"</div>) : (null)

    const has_stock_data = this.state.data.open ? (<ul className="mt-50 slide-up-fade-in styled" id="stockData" data-testid="stock-data">
    <li className="py-10">Open: {this.state.data.open}</li>
    <li className="py-10">Close: {this.state.data.close}</li>
    <li className="py-10">High: {this.state.data.high}</li>
    <li className="py-10">Low: {this.state.data.low}</li>
  </ul>) : (null)

    return (
      <div className="layout-column align-items-center mt-50">
        <section className="layout-row align-items-center justify-content-center">
          <input type="text" onChange= {this.handleChange} className="large" placeholder="5-January-2000" id="app-input" data-testid="app-input"/>
          <button className="" id="submit-button" data-testid="submit-button" onClick={this.handleUpdate}>Search</button>
        </section>
        {has_stock_data}
        {has_result}
      </div>
    );
  }
}
