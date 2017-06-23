public class TableModel {
    private Integer index;
    private String start;
    private String end;

    // getters & setters. Kind of optional in this instance. Public variables would be OK

    public Integer getIndex() {
        return index;
    }

    public void setIndex(Integer index) {
        this.index = index;
    }

    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }

    public String getEnd() {
        return end;
    }

    public void setEnd(String end) {
        this.end = end;
    }
}

=================

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.List;

public List<TableModel> splitIntoDays(String start, String end) throws ParseException {
    // Optional row index will allow the user to “click” on a specific row (future)
    int i = 0;
    List<TableModel> result = new ArrayList<>();

    // create an instance of parser with the correct structure. To handle time zones,
    // the format string would be “yyyy-MM-dd’T’HH:mm:ssZ” and the table row model would
    // be expanded to include a TZ instance variable. Web UI isn’t supporting TZ, so
    // assume a common TZ
    SimpleDateFormat iso8601 = new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ss");

    // create start and end values for math, count operations, tic in msec
    long startTime = iso8601.parse(start).getTime();
    long endTime = iso8601.parse(end).getTime();

    // quick sanity check – this will be a bug many years from now.
    if (endTime > startTime) {

      /* loop from start, while less than end, and increment by a day (in msec)
      each iteration will take the loop’s slice time and convert back to a start time, and end time
      string via the parser and create a row for our table (i.e. list element).
      The end time should not be the same as the next start time otherwise we will get duplicate
      records from Tetration.
      */
      for (long timeslice = startTime; timeslice < endTime; timeslice += 86400000) {
        TableModel row = new TableModel();
        row.setStart(iso8601.format(new Date(timeslice)));
        row.setEnd(iso8601.format(new Date(timeslice + 86399999)));
        row.setIndex(i++);
        result.add(row);
      }

      // finally replace the last page's end time with the user provided value since it could be a partial day
      result.get(i - 1).setEnd(end);
    } else {

      // Error: Create a result with one row to inform the user of the problem. For fun, include
      // the number of days we are going back in time
      TableModel errr = new TableModel();
      errr.setStart("!Error: End before Start");
      errr.setIndex(-1);
      errr.setEnd(String.format("Days: %d", (endTime - startTime)/1000/3600/24));
      result.add(errr);
    }
    return result;
    // The caller is left to handle any input validation problems that were leaked through.
    // Because the web ui does not allow direct user input, this should be minimal.
}
