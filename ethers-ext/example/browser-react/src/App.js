import React, { Component } from 'react';
import Header from "./components/Header"
import './App.css';


class App extends Component {
  constructor(props){
    super(props);
    this.state = {
      header: {
        currentNetwork: 'Baobab',
        currentAccount: '',
      },
    }
  }

  render() {
    console.log('App render');
    return (
      <div className="App">
        <Header 
          network={this.state.header.currentNetwork}
          account={this.state.header.currentAccount}
          onChangeAccount={function(accounts){
            this.setState({header:{
              currentNetwork: 'Baobab',
              currentAccount: accounts[0]
            }});
          }.bind(this)}
        >
        </Header>
      </div>
    );
  }
}

export default App;