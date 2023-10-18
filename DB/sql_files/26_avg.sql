-- GROUP BY 없이
SELECT AVG(pages) FROM books;
SELECT AVG(released_year) FROM books;

-- GROUP BY 있이
SELECT 
	author_fname, 
	author_lname,
	COUNT(*),
    AVG(pages),
    SUM(pages) / COUNT(*),
    AVG(released_year)
FROM books
GROUP BY author_lname, author_fname;