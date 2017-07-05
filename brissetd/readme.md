# Typescript

The code was written in Typescript and is compiled using tsc (typescript compiler)
and generates plain Javascript code (time-bandits.js).
The Javascript code 'time-bandits.js' is then executed in a Node.js environment.

## Sample Output
```
$ tsc time-bandits.ts
$ node time-bandits.js

[ [ '1495702800000', '1495789199999' ],
  [ '1495789200000', '1495875599999' ],
  [ '1495875600000', '1495875900000' ] ]
Thu May 25 2017 04:00:00 GMT-0500 (CDT)  Fri May 26 2017 03:59:59 GMT-0500 (CDT)
Fri May 26 2017 04:00:00 GMT-0500 (CDT)  Sat May 27 2017 03:59:59 GMT-0500 (CDT)
Sat May 27 2017 04:00:00 GMT-0500 (CDT)  Sat May 27 2017 04:05:00 GMT-0500 (CDT)


[ [ '1488762000000', '1488848399999' ],
  [ '1488848400000', '1488899100000' ] ]
Sun Mar 05 2017 19:00:00 GMT-0600 (CST)  Mon Mar 06 2017 18:59:59 GMT-0600 (CST)
Mon Mar 06 2017 19:00:00 GMT-0600 (CST)  Tue Mar 07 2017 09:05:00 GMT-0600 (CST)


[ [ '1488758400000', '1488844799999' ],
  [ '1488844800000', '1488895500000' ] ]
Sun Mar 05 2017 18:00:00 GMT-0600 (CST)  Mon Mar 06 2017 17:59:59 GMT-0600 (CST)
Mon Mar 06 2017 18:00:00 GMT-0600 (CST)  Tue Mar 07 2017 08:05:00 GMT-0600 (CST)


[ [ '1496707200000', '1493301900000' ] ]
Mon Jun 05 2017 19:00:00 GMT-0500 (CDT)  Thu Apr 27 2017 09:05:00 GMT-0500 (CDT)
```
