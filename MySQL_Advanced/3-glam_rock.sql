-- SQL script that lists all Glam rock bands from the database, ordered by lifespan
-- The Glam rock bands should be listed by lifespan in descending order
-- The lifespan of a band is the difference between the year they formed and the year they split
-- The output should be band_name and lifespan
SELECT DISTINCT band_name, IFNULL(split, 2020)- formed as lifespan
FROM metal_bands WHERE FIND_IN_SET('Glam rock', style)
ORDER BY lifespan DESC
