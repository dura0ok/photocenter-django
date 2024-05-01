-- Автоматическое проставление скидки
CREATE OR REPLACE FUNCTION auto_set_print_discount()
RETURNS TRIGGER AS $$
DECLARE
    frame_count INTEGER;
    max_discount INTEGER;
    max_discount_id INTEGER;
BEGIN
    -- Получаем количество кадров для данного заказа
    SELECT SUM(frames.amount) INTO frame_count
    FROM frames
    WHERE print_order_id = NEW.print_order_id;

    -- Логируем количество кадров
    RAISE NOTICE 'Frame count for order % is %', NEW.print_order_id, frame_count;

    SELECT COALESCE(MAX(discount), 0) FROM print_discounts WHERE frame_count >= photo_amount into max_discount;


    SELECT id INTO max_discount_id
    FROM print_discounts
    WHERE discount = max_discount;

    UPDATE print_orders SET discount_id = max_discount_id WHERE id = NEW.print_order_id;



    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Создаем триггер, который будет вызывать функцию check_print_discount
CREATE OR REPLACE TRIGGER print_order_discount_check
BEFORE INSERT OR UPDATE ON frames
FOR EACH ROW
EXECUTE FUNCTION auto_set_print_discount();
