SELECT tt.id, tt.name, tt.count
FROM (SELECT m.id, m.name, o.create_at, count(o.order_id) as count
	FROM member m
		INNER JOIN "order" o
		ON m.id = o.member_id
	GROUP BY m.id
	WHERE SUBSTR(o.created_at,1,6) = TO_CHAR(current_date - interval '1 month', 'yyyymm') AND o.status = 'Completed') as tt
WHERE tt.count >= 5;