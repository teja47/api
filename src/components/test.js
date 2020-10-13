import React, { Component } from 'react';
import axios from 'axios';
import Pass from './Pass'
import Posters from "./postersComponent";
import View from './view'
class Expenses extends Component {
  state={
    articals: []
  }
  componentDidMount(){
    axios.post('http://127.0.0.1:8000/expenses/')
    .then(res => {
      this.setState({
        articals: res.data
      });
     console.log(this.state.articals)

    })
  }

  render(){
      return(
          <View />
      )
  }

}

export default Expenses