import React from "react";
import ReactDOM from "react-dom";

import Header from "./layout/Header";

class App extends React.Component {
  render() {
    return (
      <React.Fragment>
        <Header></Header>
      </React.Fragment>
    );
  }
}

ReactDOM.render(<App />, document.getElementById("app"));
