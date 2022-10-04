/*
Julia conducted a 15 days of learning SQL contest. The start date of the contest was March 01, 2016 and the end date was March 15, 2016.

Write a query to print total number of unique hackers who made at least 1 submission each day (starting on the first day of the contest), and find the hacker_id and name of the hacker who made maximum number of submissions each day. 
If more than one such hacker has a maximum number of submissions, print the lowest hacker_id. The query should print this information for each day of the contest, sorted by the date.

- hackers
    hacker_id : Integer
    name : String

- submissions
    submission_date : Date
    submission_id : Integer
    hacker_id : Integer
    score : Integer

Sample Output
2016-03-01 4 20703 Angela
2016-03-02 2 79722 Michael
2016-03-03 2 20703 Angela
2016-03-04 2 20703 Angela
2016-03-05 1 36396 Frank
2016-03-06 1 20703 Angela

Explanation

On March 01, 2016 : 
-There are 4 unique hackers who made at least one submission each day (today). 
The hacker 20703 Angela is considered to be the hacker who made maximum number of submissions on this day.

On March 02, 2016 :
- There are 4 hackers made submissions, but only 2 of them submit every day (today and yesterday), so there are 2 unique hackers who made at least one submission each day.

On March 05, 2016 :
- There are 4 hackers made submissions. Now only 1 submitted each day (until this current day) and that is 20703 Angela. 
36396 Frank made 2 submissions, one of them On March 05 with the highest score.
*/

SELECT 
    s.submission_date, 
    (
        -- Count the hackers who submitted on submission_date
        SELECT COUNT(DISTINCT hacker_id)
        FROM submissions s1
        WHERE submission_date = s.submission_date
        -- And only if they had submitted in all previous days
        -- By counting the unique previous days they participated in, which should equal to the difference between submission's date and the first day of the competition
        AND (   
            SELECT COUNT(DISTINCT submission_date)
            FROM submissions
            WHERE hacker_id = s1.hacker_id
            AND submission_date < s.submission_date
        ) = DATEDIFF(s.submission_date, '2016-03-01')
    ) uniqe_hackers,
    (
        SELECT hacker_id
        FROM submissions
        WHERE submission_date = s.submission_date
        GROUP BY hacker_id
        ORDER BY COUNT(submission_id) DESC, hacker_id ASC
        LIMIT 1
    ) top_hacker,
    (
        SELECT name 
        FROM hackers
        WHERE hacker_id = (SELECT top_hacker)
    ) top_hacker_name
FROM (
    SELECT submission_date 
    FROM submissions 
    GROUP BY submission_date) s
ORDER BY s.submission_date ASC;
