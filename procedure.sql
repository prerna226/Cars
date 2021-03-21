-- FUNCTION: public.get_car_detail(character varying)

-- DROP FUNCTION public.get_car_detail(character varying);

CREATE OR REPLACE FUNCTION public.get_car_detail(
	searchkeyword character varying, pageLimit INT, pageNumber INT)
    RETURNS TABLE(namess character varying) 
    LANGUAGE 'sql'
    COST 100
    VOLATILE PARALLEL UNSAFE
    ROWS 1000

AS $BODY$

SELECT concat(cb.name,' ',cm.name,' ',cv.name) FROM 
car_brand cb INNER JOIN car_detail cd ON cb.id = cd.brand_id
LEFT JOIN car_model cm ON cm.id = cd.model_id
LEFT JOIN car_varient cv ON cv.id = cd.varient_id

WHERE concat(cb.name,' ',cm.name,' ',cv.name) ILIKE '%' || searchKeyword || '%' LIMIT pageLimit OFFSET pageNumber
$BODY$;

ALTER FUNCTION public.get_car_detail(character varying)
    OWNER TO postgres;
