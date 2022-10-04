/*
Harry Potter and his friends are at Ollivander's with Ron, finally replacing Charlie's old broken wand.

Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each non-evil wand of high power and age. 

Write a query to print the id, age, coins_needed, and power of the wands that Ron's interested in, sorted in order of descending power. If more than one wand has same power, sort the result in order of descending age.

- wands 
    id : Integer
    code : Integer
    coins_needed : Integer
    power : Integer (the higher the power, the better the wand is)

- wands_property 
    code : Integer
    age : Integer
    is_evil : Integer (0 or 1)
*/

SELECT w.id, p.age, w.coins_needed, w.power
FROM wands w
JOIN wands_property p
    ON p.code = w.code
WHERE 
    -- non-evil wand
    p.is_evil = 0 AND 
    -- minimum coins needed for the same code and age
    w.coins_needed = (
        SELECT MIN(w2.coins_needed) 
        FROM wands w2 
        JOIN wands_property p2 
            ON p2.code = w2.code
        WHERE p.age = p2.age AND w.power = w2.power
        )
ORDER BY w.power DESC, p.age DESC;