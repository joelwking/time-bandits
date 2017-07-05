import * as Promise from 'bluebird';

const MSINONEDAY:number = 86400000;

function giveMeTwoDates(dateOne: string, dateTwo: string) {
  return new Promise((resolve, reject) => {
    // initialize varables
    let dateOneEpoch = Date.parse(dateOne);
    let dateTwoEpoch = Date.parse(dateTwo);
    let timeDelta:number;
    let numberOfWholeDays:number;
    let startStopRanges:any = [];
    let startTime: number;
    let endTime: number;

    if(dateOneEpoch < dateTwoEpoch){
      // Check for proper dates
      timeDelta = dateTwoEpoch - dateOneEpoch;
      numberOfWholeDays = Math.floor(timeDelta / MSINONEDAY);
      // Determine number of whole days
      startTime = dateOneEpoch;
      while(numberOfWholeDays > 0) {
        // Calculate the start and end time for whole days
        numberOfWholeDays -= 1;
        endTime = startTime + MSINONEDAY - 1;
        startStopRanges.push([`${startTime}`, `${endTime}`])
        startTime = endTime + 1;
      }
      let timeRemaining:number = startTime + timeDelta - (Math.floor(timeDelta/MSINONEDAY) * MSINONEDAY);
      // Calculate the remaining time
      startStopRanges.push([`${startTime}`, `${timeRemaining}`])
      return resolve(startStopRanges);
      // returns the start/stop dates and times based on initial dates and times
    } else {
      startStopRanges.push([`${dateOneEpoch}`, `${dateTwoEpoch}`]);
      return resolve(startStopRanges);
      // returns the origial dates and times without caculating times, because of invalid dates.
    };
  });
}

// Test data
var demos = [];
demos.push(["2017-05-25T09:00:00-0000", "2017-05-27T09:05:00-0000"]);
demos.push(["2017-03-05T19:00:00-0600", "2017-03-07T09:05:00-0600"]);
demos.push(["2017-03-05T19:00:00-0500", "2017-03-07T09:05:00-0500"]);
demos.push(["2017-06-05T19:00:00-0500", "2017-04-27T09:05:00-0500"]);

for(let demo in demos){
  giveMeTwoDates(demos[demo][0], demos[demo][1]).then((ranges) => {
    /* creates list of start and stop dates based on 24 hour windows to
    accommodate the ranges allowed by the Tetration API.  It only allows a
    24 hour time period to be quered per request.  The query accepts
    either iso8601 or epoch time values.
    */
    console.log(ranges);
    // Displays the epoch time ranges.
    for(let range of ranges) {
      // Displays the iso8601 values of the epoch time values.
      let start1 = new Date(parseInt(range[0]));
      let end1 = new Date(parseInt(range[1]));
      console.log(`${start1.toString()}  ${end1.toString()}`);
    }
  console.log('\n');
  })
}
