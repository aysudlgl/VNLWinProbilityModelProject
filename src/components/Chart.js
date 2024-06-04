import React from 'react';
import { Bar } from 'react-chartjs-2';

const Chart = ({ predictions }) => {
    const data = {
        labels: predictions.map(prediction => prediction.match),
        datasets: [
            {
                label: 'Home Predictability',
                data: predictions.map(prediction => prediction.homeWinProb),
                backgroundColor: 'rgba(75, 192, 192, 0.6)',
            },
            {
                label: 'Away Predictability',
                data: predictions.map(prediction => prediction.awayWinProb),
                backgroundColor: 'rgba(153, 102, 255, 0.6)',
            },
        ],
    };

    return (
        <div>
            <h2>Predictability Chart</h2>
            <Bar data={data} />
        </div>
    );
};

export default Chart;
