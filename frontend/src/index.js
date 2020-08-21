import React from 'react';
import ReactDOM from 'react-dom';

import App from './app';


const token = prompt('Token');

ReactDOM.render(<App token={token} />, document.getElementById('root'));
