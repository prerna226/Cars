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

select concat(cb.name,' ',cm.name,' ',cv.name) from car_brand cb 
inner join car_detail cd on cb.id = cd.brand_id
left join car_model cm on cb.id = cd.model_id
left join car_varient cv on cv.id = cd.varient_id

WHERE concat(cb.name,' ',cm.name,' ',cv.name) ILIKE '%' || searchKeyword || '%' LIMIT pageLimit OFFSET pageNumber
$BODY$;

ALTER FUNCTION public.get_car_detail(character varying)
    OWNER TO postgres;
