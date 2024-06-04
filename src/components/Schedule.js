import React, { useEffect, useState } from 'react';

const Schedule = () => {
    const [schedule, setSchedule] = useState([]);

    useEffect(() => {
        const year = '2024';
        const month = '06';
        fetch(`/api/schedule/${year}/${month}`)
            .then(response => response.json())
            .then(data => setSchedule(data.matches || []));
    }, []);

    return (
        <div>
            <h2>Schedule</h2>
            <ul>
                {schedule.map((match, index) => (
                    <li key={index}>
                        {match.home_team.name} vs {match.away_team.name} on {match.date}
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Schedule;
