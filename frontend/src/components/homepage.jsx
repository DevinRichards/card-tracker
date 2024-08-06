import React from 'react';
import { Link } from 'react-router-dom';

const Homepage = () => {
    return (
        <div>
            <h1>Welcome to Card Tracker</h1>
            <p>This is your one-stop solution for tracking your card collection.</p>
            <div>
                <Link to="/login">Login</Link>
            </div>
            <div>
                <Link to="/register">Register</Link>
            </div>
        </div>
    );
};

export default Homepage;
