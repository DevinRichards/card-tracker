import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Login from './components/Login';
import Register from './components/Register';

function App() {
    return (
        <Router>
            <div>
                <Switch>
                    <Route path="/login" component={Login} />
                    <Route path="/register" component={Register} />
                    <Route path="/" exact component={Home} />
                </Switch>
            </div>
        </Router>
    );
}

function Home() {
    return <h2>Home Page</h2>;
}

export default App;
