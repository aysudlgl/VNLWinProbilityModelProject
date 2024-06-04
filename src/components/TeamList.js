import React, { useEffect, useState } from 'react';

const TeamList = () => {
    const [teams, setTeams] = useState({});

    useEffect(() => {
        fetch('/api/teams')
            .then(response => response.json())
            .then(data => setTeams(data));
    }, []);

    return (
        <div>
            <h2>Teams</h2>
            <ul>
                {Object.keys(teams).map(team => (
                    <li key={team}>
                        {team}: {JSON.stringify(teams[team])}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default TeamList;
