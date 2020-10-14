import React from 'react';
import axios from 'axios';
import Trailer from './corouselComponent'
import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader
class TrailerClass extends React.Component {

    state={
      artical: { },
      tes: []
      
    }
    componentDidMount(){
        const articalID=1
      axios.get(`http://arereyyyapp.herokuapp.com/trailers/${articalID}`)
      .then(res => {
        this.setState({
          artical: res.data
        });
        console.log(res.data)

            const test = this.state.artical.links
            const arrays= test.split(" ")
            this.setState({
                tes: arrays
            })      })
      
    }

render(){
    return (
        <div >
                   <Trailer  data={this.state.tes} />  
        </div>
    );
 }
}

export default TrailerClass