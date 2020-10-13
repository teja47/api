import React, { Component } from 'react';
import {Button, Form,Input} from 'reactstrap';
class View extends Component {
  state={
    articals: []
  }

  
  render(){
      return(
       
   
              <div color="white">  
              
              <Form>
                  <Form label="email">
                      <Input />
                    
                  </Form>
                  <Form label="name">
                      <Input />
                    
                  </Form>
                  <Form label="content">
                      <Input />
                    
                  </Form>
                  <Button type="primary" htmlType="submit">submittt</Button>
              </Form>
                </div>  
          
      );
  }
}


export default View;
