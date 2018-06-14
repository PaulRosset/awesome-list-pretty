import React, { Component } from "react";
import { Header } from "./components/Header";
import { InstantSearch } from "react-instantsearch/dom";
import { Body } from "./components/Body";

class App extends Component {
  render() {
    return (
      <div className="App">
        <InstantSearch
          appId="W4TTTJ58U4"
          apiKey="f4e9e1d0bfe2d4348a852e23409d814c"
          indexName="dev_AWESOME"
        >
          <Header />
          <Body />
        </InstantSearch>
      </div>
    );
  }
}

export default App;
