import React from 'react';
import ReactDOM from 'react-dom';

import App from './app';


let token = (history.state || {}).token;
if (!token) {
  token = new URL(location.href).searchParams.get('token');
  if (!token) {
    token = prompt('Token');
  }
  history.replaceState({token}, '', '/');
}
ReactDOM.render(<App token={token} />, document.getElementById('root'));
