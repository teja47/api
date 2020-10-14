import React, { Component } from 'react';
import axios from 'axios';
import {Container} from 'react-bootstrap'
import {Card,CardImg} from 'reactstrap';
class Posters extends Component {
  state={
    artical: { }
  }
  componentDidMount(){
    const  articalID= Math.floor(8 + Math.random() * (5-1));
    axios.get(`https://arereyyyapp.herokuapp.com/pos/${articalID}`)
    .then(res => {
      this.setState({
        artical: res.data
      });
    
    })
  }
    render(){
        return(
      
          <div className="margintop20 container ">
                <Container className="margintop20 black ">
    <Card className="black  col-md-8   margintop20 col-sm-12  img-responsive offset-lg-2 "   >
    <CardImg className=" "  src={this.state.artical.poster} />
</Card>
</Container>
          </div>
)
}
}

export default Posters