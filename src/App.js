import React, { Component } from 'react';
import { Route} from 'react-router-dom'

import ArticalView from './components/ArticalView';
import Movie from './components/ArticalDetail';
import Casty from './components/cast';
import Test from './components/test';
class App extends Component {
 

  
  render(){
    return(
      <div className="black" >
   
     
       
      <Route  path='/' exact component={ArticalView} />
       <Route  path='/:articalID'exact  component={Movie} />
      <Route  path='/cast/:articalNAME'exact  component={Casty} />
      <Route path='/test'exact component={Test}/>
  
     
   
   
     </div>
    );
}
}
export default App;
