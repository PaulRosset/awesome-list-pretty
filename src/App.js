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
          appId={process.env.REACT_APP_APPID}
          apiKey={process.env.REACT_APP_API_KEY}
          indexName={process.env.REACT_APP_INDEX_NAME}
          refresh={true}
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
