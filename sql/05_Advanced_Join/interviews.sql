/*
Samantha interviews many candidates from different colleges using coding challenges and contests. 
Write a query to print the contest_id, hacker_id, name, and the sums of total_submissions, total_accepted_submissions, total_views, and total_unique_views for each contest sorted by contest_id. 
Exclude the contest from the result if all four sums are 0.

Note: A specific contest can be used to screen candidates at more than one college, but each college only holds 1 screening contest.

Input Format
- Contests
    contest_id : Integer
    hacker_id : Integer
    name : String
- Colleges 
    college_id : Integer
    contest_id : Integer
- Challenges
    challenge_id : Integer
    college_id : Integer
- View_Stats
    challenge_id : Integer
    total_views : Integer
    total_unique_views : Integer
- Submission_Stats
    challenge_id : Integer
    total_submissions : Integer
    total_accepted_submission : Integer

Sample Output
66406 17973 Rose 111 39 156 56
66556 79153 Angela 0 0 11 10
94828 80275 Frank 150 38 41 15

*/

WITH 
    Submission_Stats_Grp AS (
        SELECT challenge_id, 
            SUM(total_submissions) total_submissions, 
            SUM(total_accepted_submissions) total_accepted_submissions
        FROM Submission_Stats 
        GROUP BY challenge_id
        ),
    View_Stats_Grp AS (
        SELECT challenge_id, 
            SUM(total_views) total_views, 
            SUM(total_unique_views) total_unique_views
        FROM View_Stats 
        GROUP BY challenge_id
        )
SELECT 
    Contests.contest_id, Contests.hacker_id, Contests.name,
    SUM(Submission_Stats_Grp.total_submissions), 
    SUM(Submission_Stats_Grp.total_accepted_submissions),
    SUM(View_Stats_Grp.total_views), 
    SUM(View_Stats_Grp.total_unique_views)
FROM Contests
INNER JOIN Colleges 
    ON Colleges.contest_id = Contests.contest_id
INNER JOIN Challenges 
    ON Challenges.college_id = Colleges.college_id 
LEFT JOIN Submission_Stats_Grp 
    ON Submission_Stats_Grp.challenge_id = Challenges.challenge_id
LEFT JOIN View_Stats_Grp 
    ON View_Stats_Grp.challenge_id = Challenges.challenge_id
GROUP BY Contests.contest_id, Contests.hacker_id, Contests.name
HAVING 
    SUM(total_submissions) <> 0 OR SUM(total_accepted_submissions) <> 0 OR 
    SUM(total_views) <> 0 OR SUM(total_unique_views) <> 0
ORDER BY Contests.contest_id ASC;