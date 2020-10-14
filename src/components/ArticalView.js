import React, { Component } from 'react';
import axios from 'axios';
import Pass from './Pass'
import Posters from "./postersComponent";
class ArticalView extends Component {
  state={
    articals: []
  }
  componentDidMount(){
    axios.get('https://arereyyyapp.herokuapp.com/api')
    .then(res => {
      this.setState({
        articals: res.data
      });
     console.log(res.data)

    })
  }
  render(){
      return(
        <div>
          <Posters/>
        <div className="margintop10">
         <Pass data={this.state.articals}  />
        </div>
        </div>
   
                
          
      );
  }
}


export default ArticalView;
