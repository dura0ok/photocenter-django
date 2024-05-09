-- Автоматическое проставление скидки
CREATE OR REPLACE FUNCTION auto_set_print_discount()
    RETURNS TRIGGER AS
$$
DECLARE
    frame_count     INTEGER;
    max_discount    INTEGER;
    max_discount_id INTEGER;
BEGIN
    RAISE NOTICE '%', NEW;
    -- Получаем количество кадров для данного заказа
    SELECT SUM(frames.amount)
    INTO frame_count
    FROM frames
    WHERE print_order_id = NEW.print_order_id;

    -- Логируем количество кадров
    RAISE NOTICE 'Frame count for order % is %', NEW.print_order_id, frame_count;

    SELECT id, COALESCE(MAX(discount), 0)
    FROM print_discounts
    WHERE frame_count >= photo_amount
    group by id
    into max_discount_id, max_discount;

    RAISE NOTICE 'Max discount is % for id %', max_discount, max_discount_id;

    UPDATE print_orders SET discount_id = max_discount_id WHERE id = NEW.print_order_id;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Создаем триггер, который будет вызывать функцию check_print_discount
CREATE OR REPLACE TRIGGER print_order_discount_check
    AFTER INSERT OR UPDATE
    ON frames
    FOR EACH ROW
EXECUTE FUNCTION auto_set_print_discount();
