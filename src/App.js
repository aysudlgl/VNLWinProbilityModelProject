import React, { useState, useEffect } from 'react';
import TeamList from './components/TeamList';
import Schedule from './components/Schedule';
import Predictions from './components/Predictions';
import Chart from './components/Chart';

const App = () => {
    const [teams, setTeams] = useState({});

    useEffect(() => {
        fetch('/api/teams')
            .then(response => response.json())
            .then(data => setTeams(data));
    }, []);

    return (
        <div>
            <h1>Volleyball Predictor</h1>
            <TeamList />
            <Schedule />
            <Predictions teams={teams} />
            <Chart predictions={teams} />
        </div>
    );
};

export default App;
