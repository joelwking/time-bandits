/*
  Simple program to demonstrate generating list of 24-hour queries needed to
  overcome limitations in Tetration external API. Uses basic date/time functions
  from libc -- everything done in main() to minimize clutter.
  
  Ignore timezone since full ISO 8601 determines UTC time? When environment 
  variable TZ not set, seems a little wonky...*usually* works ;)

  To build: gcc -o basic_query -lc basic_query.c
  To run:   basic_query first_time last_time outfile

  where first_time, last_time are in full ISO 8601 format (eg 2017-03-27T09:23:37-0400). 
  Outfile contains sequence of pairs of times needed for Tetration queries to cover original span.

  For kicks, each line has the pair three times: epoch in hexadecimal,
  epoch in decimal, and ISO 8601...for example, in out_query.txt:


  Time span   2017-03-27T05:43:17-0700  2017-05-27T14:33:53-0700
  Epoch Time  1490618597  1495920833
 
  Query    0:  1490618597  1490704997    2017-03-27T12:43:17+0000  2017-03-28T12:43:17+0000  
  Query    1:  1490704997  1490791397    2017-03-28T12:43:17+0000  2017-03-29T12:43:17+0000  
  Query    2:  1490791397  1490877797    2017-03-29T12:43:17+0000  2017-03-30T12:43:17+0000  
  (etc etc)


  which was produced by running 

  ./basic_query 2017-03-27T05:43:17-0700 2017-05-27T14:33:53-0700 out_query.txt 

*/


#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
#include <string.h>

//#define _DEBUG_

void dump_tm(FILE *outfile, struct tm *Time);  // utility to pretty print tm struct

int main(int argc, char **argv)
{
    int iter;
    struct tm Time1, Time2; 
    struct tm *time_buff;
    char *status;
    char *Format = "%Y-%m-%dT%H:%M:%S%z";    //or "%FT%T%z" also works
    time_t rawtime1, rawtime2, current_raw, next_raw;
    FILE *outfile;
    // used to convert epoch times to ISO 8601
    char dbuff[256];
    int nchar;

    
    if (argc<4) {
	fprintf(stderr,"%s first_time last_time outfile\n",argv[0]);
	fprintf(stderr,"   where times are given in full ISO 8601 format\n");
	fprintf(stderr,"   e.g. 2017-03-27T09:23:37-0400\n");
	return 0;
    }

    if (NULL == (outfile = fopen(argv[3],"w"))) {
	fprintf(stderr,"Fatal error opening file %s for output\n",argv[3]);
	return -1;
    }
    
    if (NULL == (status = strptime(argv[1], Format, &Time1))) {
	fprintf(stderr,"Fatal error parsing first time: %s\n",argv[1]);
	return -2;
    }
    rawtime1 = timegm(&Time1);

#ifdef _DEBUG_    
    fprintf(stdout,"Return status %s\n",status);
    dump_tm(stdout, (struct tm *) &Time1);
    nchar = strftime(dbuff, 256, Format, &Time1);
    fprintf(stdout,"#bytes %3d: %s\n\n",nchar,dbuff);
#endif
    
    if (NULL == (status = strptime(argv[2], Format, &Time2))) {
	fprintf(stderr,"Fatal error parsing last time: %s\n",argv[2]);
	return -3;
    }
    rawtime2 = timegm(&Time2);

#ifdef _DEBUG_
    fprintf(stdout,"Return status %s\n",status);
    dump_tm(stdout, (struct tm *) &Time1);
    nchar = strftime(dbuff, 256, Format, &Time1);
    fprintf(stdout,"#bytes %3d: %s\n\n",nchar,dbuff);
#endif

    current_raw = rawtime1;
    iter = 0;
    fprintf(outfile,"Time span   %s  %s\n",argv[1],argv[2]);
    fprintf(outfile,"Epoch Time  %10ld  %10ld\n",rawtime1,rawtime2);
    fprintf(outfile,"\n");
    while (current_raw<rawtime2) {
	next_raw = current_raw + 24*60*60;
	if (next_raw>rawtime2) next_raw = rawtime2;
	fprintf(outfile,"Query %4d:  ",iter);
	fprintf(outfile,"%10ld  %10ld    ",current_raw,next_raw);
	time_buff = gmtime(&current_raw);
	nchar = strftime(dbuff, 256, Format, time_buff);
	fprintf(outfile,"%s  ",dbuff);
	time_buff = gmtime(&next_raw);
	nchar = strftime(dbuff, 256, Format, time_buff);
	fprintf(outfile,"%s  ",dbuff);
	fprintf(outfile,"\n");
	current_raw = next_raw;
	iter++;
    }

    return 0;
    
}

void dump_tm(FILE *outfile, struct tm *Time)
{
    fprintf(outfile,"=>   %d  %d  %d\n",Time->tm_year,Time->tm_mon,Time->tm_mday);
    fprintf(outfile,"=>  tm_sec    %d\n",Time->tm_sec);	        /* seconds after the minute [0-60] */
    fprintf(outfile,"=>  tm_min    %d\n",Time->tm_min);	        /* minutes after the hour [0-59] */
    fprintf(outfile,"=>  tm_hour   %d\n",Time->tm_hour);	/* hours since midnight [0-23] */
    fprintf(outfile,"=>  tm_mday   %d\n",Time->tm_mday);	/* day of the month [1-31] */
    fprintf(outfile,"=>  tm_mon    %d\n",Time->tm_mon);	        /* months since January [0-11] */
    fprintf(outfile,"=>  tm_year   %d\n",Time->tm_year);	/* years since 1900 */
    fprintf(outfile,"=>  tm_wday   %d\n",Time->tm_wday);	/* days since Sunday [0-6] */
    fprintf(outfile,"=>  tm_yday   %d\n",Time->tm_yday);	/* days since January 1 [0-365] */
    fprintf(outfile,"=>  tm_isdst  %d\n",Time->tm_isdst);	/* Daylight Savings Time flag */
    fprintf(outfile,"=>  tm_gmtoff %ld\n",Time->tm_gmtoff);	/* long  offset from CUT in seconds */
    fprintf(outfile,"=>  *tm_zone  %s\n",Time->tm_zone);	/* char  timezone abbreviation */
}
