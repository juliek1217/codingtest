const axios = require('axios');

require('./callMock');

function cityWeather(city) {
    // Implement the function
    // You can use console.log for debugging

    // API url = `https://example.com/data/2.5/weather?...`
    // Use q parameter (city) at the end of the url in order to mock data correctly

    return new Promise((resolve, reject) => {

        // Implement the function - call http request
            resolve(object_to_be_returned);
        // Implement the function
    });
}

module.exports = {
    cityWeather
};
