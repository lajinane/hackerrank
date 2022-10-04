/*
Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard! 
Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. 
Order your output in descending order by the total number of challenges in which the hacker earned a full score. 
If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.

- hackers
    hacker_id : Integer
    name : String

- difficulty
    difficulty_level : Integer
    score : Integer

- challenges
    challenge_id : Integer
    hacker_id : Integer
    difficulty_level : Integer

- submissions
    submission_id : Integer
    hacker_id : Integer
    challenge_id : Integer
    score : Integer
*/

SELECT h.hacker_id, h.name
FROM hackers h
JOIN submissions s
    ON s.hacker_id = h.hacker_id
JOIN challenges c
    ON c.challenge_id = s.challenge_id
JOIN difficulty d
    ON d.difficulty_level = c.difficulty_level
-- compare the score of the same difficulty level
WHERE s.score = d.score 
    AND d.difficulty_level = c.difficulty_level
GROUP BY h.hacker_id, h.name
HAVING COUNT(h.hacker_id) > 1
ORDER BY COUNT(h.hacker_id) DESC, h.hacker_id ASC;