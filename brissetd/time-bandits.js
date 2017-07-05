"use strict";
exports.__esModule = true;
var Promise = require("bluebird");
var MSINONEDAY = 86400000;
function giveMeTwoDates(dateOne, dateTwo) {
    return new Promise(function (resolve, reject) {
        // initialize varables
        var dateOneEpoch = Date.parse(dateOne);
        var dateTwoEpoch = Date.parse(dateTwo);
        var timeDelta;
        var numberOfWholeDays;
        var startStopRanges = [];
        var startTime;
        var endTime;
        if (dateOneEpoch < dateTwoEpoch) {
            // Check for proper dates
            timeDelta = dateTwoEpoch - dateOneEpoch;
            numberOfWholeDays = Math.floor(timeDelta / MSINONEDAY);
            // Determine number of whole days
            startTime = dateOneEpoch;
            while (numberOfWholeDays > 0) {
                // Calculate the start and end time for whole days
                numberOfWholeDays -= 1;
                endTime = startTime + MSINONEDAY - 1;
                startStopRanges.push(["" + startTime, "" + endTime]);
                startTime = endTime + 1;
            }
            var timeRemaining = startTime + timeDelta - (Math.floor(timeDelta / MSINONEDAY) * MSINONEDAY);
            // Calculate the remaining time
            startStopRanges.push(["" + startTime, "" + timeRemaining]);
            return resolve(startStopRanges);
            // returns the start/stop dates and times based on initial dates and times
        }
        else {
            startStopRanges.push(["" + dateOneEpoch, "" + dateTwoEpoch]);
            return resolve(startStopRanges);
            // returns the origial dates and times without caculating times, because of invalid dates.
        }
        ;
    });
}
// Test data
var demos = [];
demos.push(["2017-05-25T09:00:00-0000", "2017-05-27T09:05:00-0000"]);
demos.push(["2017-03-05T19:00:00-0600", "2017-03-07T09:05:00-0600"]);
demos.push(["2017-03-05T19:00:00-0500", "2017-03-07T09:05:00-0500"]);
demos.push(["2017-06-05T19:00:00-0500", "2017-04-27T09:05:00-0500"]);
for (var demo in demos) {
    giveMeTwoDates(demos[demo][0], demos[demo][1]).then(function (ranges) {
        /* creates list of start and stop dates based on 24 hour windows to
        accommodate the ranges allowed by the Tetration API.  It only allows a
        24 hour time period to be quered per request.  The query accepts
        either iso8601 or epoch time values.
        */
        console.log(ranges);
        // Displays the epoch time ranges.
        for (var _i = 0, ranges_1 = ranges; _i < ranges_1.length; _i++) {
            var range = ranges_1[_i];
            // Displays the iso8601 values of the epoch time values.
            var start1 = new Date(parseInt(range[0]));
            var end1 = new Date(parseInt(range[1]));
            console.log(start1.toString() + "  " + end1.toString());
        }
        console.log('\n');
    });
}
