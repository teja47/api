import React from 'react';
import {Route,Switch} from 'react-router-dom';
import ArticalView from './ArticalView';
import ArticalDetail from './ArticalDetail';
import Casty from './cast';


const BaseRouter =() =>(


        <ul>
            <li>
            <Route  path='/' exact component={ArticalView} />

            </li>
            <li>
            <Route  path='/:articalID'exact  component={ArticalDetail} />
            </li>
            <li>
            <Route  path='/:articalNAME'exact  component={Casty} />
            </li>
        </ul>
      
      
       
        
        
 

);
export default BaseRouter;