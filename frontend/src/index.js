import React from 'react';
import ReactDOM from 'react-dom';
import "antd/dist/antd.css";
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import { createStore, compose, applyMiddleware } from 'redux';
import { Provider } from 'react-redux'
import reducer from './store/reducers/auth'
import thunk from 'redux-thunk'

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose
const store = createStore(reducer, composeEnhancers(
  applyMiddleware(thunk)
));
const app = (
  <Provider store={store}>
    <App/>
  </Provider>
)

ReactDOM.render(app, document.getElementById('root'));
registerServiceWorker();
