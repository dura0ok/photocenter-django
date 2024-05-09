CREATE OR REPLACE FUNCTION check_film_item_type() RETURNS TRIGGER AS
$$
DECLARE
    item_name TEXT;
BEGIN
    SELECT product_name INTO item_name from items where id = NEW.item_id;
    IF NOT lower(item_name) ~* 'пл[её]нка' THEN
        RAISE EXCEPTION 'Film should be with correct item';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER check_correct_film_item_type
    BEFORE INSERT OR UPDATE
    ON films
    FOR EACH ROW
EXECUTE FUNCTION check_film_item_type();
