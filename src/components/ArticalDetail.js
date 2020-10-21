import React, { Component } from 'react';
import axios from 'axios';
import MovieCast from "./MovieCast"
import { Card, CardBody, CardImg,CardText, CardTitle } from 'reactstrap';
import {Row,Container} from 'react-bootstrap'



class Movie extends Component {
  state={
    artical:[],
    cast:[],
    tes:[]
  }
  componentDidMount(){
      const articalID=this.props.match.params.articalID
    axios.get(`https://arereyyy-api.herokuapp.com/api${articalID}`)
    .then(res => {
      this.setState({
        artical: res.data
      })
      console.log(res.data)
      const test = this.state.artical.cast
      const arrays= test.split(",")
      this.setState({
          tes: arrays})
        }
     
  )}
  
   
  render(){
    if (!this.state.artical) return null;
    return(  
    <Container> 
      <Row className="black  margintop20"  >
         <Card className="btn-flat" >
            <CardTitle><h1 className="btn-flat">{this.state.artical.title}</h1></CardTitle>
            <CardImg top className=" col-12 col-md-8 col-lg-12  "  style={{width:200}} src={this.state.artical.image} ></CardImg>
           </Card> 
    <Card className="btn-flat" >
    <CardBody>
      <CardTitle>{this.state.artical.contentHead}</CardTitle>
      <CardText>
        {this.state.artical.content}
      </CardText>
    </CardBody>
  </Card>   
  <Card  className=" btn-flat " > 
  <CardBody className=" btn-flat " >
      <iframe className=" col-12 col-md-8 col-lg-12  "  src={this.state.artical.youtubeLink}/>
     </CardBody>
      </Card>
    </Row>
    <MovieCast data={this.state}/>
  
    </Container>
      )
}
}
export default Movie;
