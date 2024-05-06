CREATE OR REPLACE FUNCTION calculate_print_orders_price(order_id BIGINT)
RETURNS BIGINT AS $$
DECLARE
    total_price INTEGER := 0;
    discount_amount INTEGER := 0;
BEGIN

    SELECT COALESCE(SUM(frames.amount * print_prices.price), 0)
    INTO total_price
    FROM frames
    JOIN print_orders ON frames.print_order_id = print_orders.id
    JOIN print_prices ON frames.print_price_id = print_prices.id
    WHERE print_orders.order_id = calculate_print_orders_price.order_id;


    SELECT COALESCE(SUM(print_discounts.discount), 0)
    INTO discount_amount
    FROM print_orders
    JOIN print_discounts ON print_orders.discount_id = print_discounts.id
    WHERE print_orders.order_id = calculate_print_orders_price.order_id;

    total_price := total_price - (total_price * discount_amount / 100);

    RETURN total_price;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION calculate_service_orders_price(order_id BIGINT)
RETURNS BIGINT AS $$
DECLARE
    total_price INTEGER := 0;
BEGIN
    SELECT COALESCE(SUM(service_types.price * service_orders.count), 0)
    INTO total_price
    FROM service_orders
    JOIN service_types_outlets ON service_orders.service_type_id = service_types_outlets.id
    JOIN service_types ON service_types_outlets.service_type_id = service_types.id
    WHERE service_orders.order_id = calculate_service_orders_price.order_id;

    RETURN total_price;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION calculate_sale_orders_price(order_id BIGINT)
RETURNS BIGINT AS $$
DECLARE
    total_price INTEGER := 0;
BEGIN
    SELECT COALESCE(SUM(items.price * sale_orders.amount), 0)
    INTO total_price
    FROM sale_orders
    JOIN items ON sale_orders.item_id = items.id
    WHERE sale_orders.order_id = calculate_sale_orders_price.order_id;

    RETURN total_price;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION calculate_film_development_orders_price(order_id BIGINT)
RETURNS BIGINT AS $$
DECLARE
    total_price INTEGER := 0;
BEGIN

    SELECT COALESCE(SUM(st.price * so.count), 0) INTO total_price
    FROM service_orders so
    JOIN public.service_types st on so.service_type_id = st.id
    WHERE st.name = 'Проявка плёнки' AND so.order_id = calculate_film_development_orders_price.order_id;
    RAISE NOTICE 'LALA % % %', total_price, calculate_film_development_orders_price.order_id, total_price;
    RETURN total_price;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION update_order_price(order_id BIGINT, new_price BIGINT)
RETURNS VOID AS $$
BEGIN
    UPDATE orders
    SET total_amount_price = new_price
    WHERE id = update_order_price.order_id;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION apply_client_discount_to_order(order_id BIGINT, order_total BIGINT)
RETURNS BIGINT AS $$
DECLARE
    client_discount INTEGER := 0;
    client_num BIGINT;
BEGIN
    SELECT client_id INTO client_num FROM orders where id = order_id;

    SELECT discount
    INTO client_discount
    FROM clients
    WHERE id = client_num;

    RAISE NOTICE 'Active discount is % for id: % and order id %', client_discount, client_num, order_id;
    RETURN order_total - (order_total * client_discount / 100);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION calculate_order_price(order_id BIGINT)
RETURNS BIGINT AS $$
DECLARE
    total_price INTEGER := 0;
BEGIN
    SELECT calculate_print_orders_price(order_id) + total_price INTO total_price;
    RAISE NOTICE '%', total_price;

    SELECT calculate_service_orders_price(order_id) + total_price INTO total_price;
    RAISE NOTICE '%', total_price;

    SELECT calculate_sale_orders_price(order_id) + total_price INTO total_price;
    RAISE NOTICE '%', total_price;

    SELECT calculate_film_development_orders_price(order_id) + total_price INTO total_price;
    RAISE NOTICE '%', total_price;

    RAISE NOTICE 'BEFORE DISCOUNT %', total_price;

    RETURN apply_client_discount_to_order(order_id, total_price);
END;
$$ LANGUAGE plpgsql;


-- For service_orders table
CREATE OR REPLACE FUNCTION update_price_trigger()
RETURNS TRIGGER AS $$
BEGIN
    PERFORM update_order_price(NEW.order_id, calculate_order_price(NEW.order_id));
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create triggers on all related orders tables to call the update_price_trigger function
CREATE OR REPLACE TRIGGER update_price_trigger_for_orders
AFTER INSERT OR UPDATE OR DELETE
ON public.sale_orders
FOR EACH ROW
EXECUTE FUNCTION update_price_trigger();

CREATE OR REPLACE TRIGGER update_price_trigger_for_print_orders
AFTER INSERT OR UPDATE OR DELETE
ON public.print_orders
FOR EACH ROW
EXECUTE FUNCTION update_price_trigger();

CREATE OR REPLACE TRIGGER update_price_trigger_for_service_orders
AFTER INSERT OR UPDATE OR DELETE
ON public.service_orders
FOR EACH ROW
EXECUTE FUNCTION update_price_trigger();