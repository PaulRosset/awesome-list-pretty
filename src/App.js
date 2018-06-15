import React, { Component } from "react";
import { Header } from "./components/Header";
import { InstantSearch } from "react-instantsearch/dom";
import { WrappedBody } from "./components/Body";
import { Authors } from "./components/Authors";

class App extends Component {
  render() {
    return (
      <div className="App">
        <InstantSearch appId="" apiKey="" indexName="">
          <Header />
          <WrappedBody />
          <Authors />
        </InstantSearch>
      </div>
    );
  }
}

export default App;
