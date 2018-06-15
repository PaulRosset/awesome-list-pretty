import React, { Component } from "react";
import { Header } from "./components/Header";
import { InstantSearch } from "react-instantsearch/dom";
import { WrappedBody } from "./components/Body";
import { Authors } from "./components/Authors";

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
          <WrappedBody />
          <Authors />
        </InstantSearch>
      </div>
    );
  }
}

export default App;
