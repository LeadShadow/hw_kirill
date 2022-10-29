# Необходимо реализовать функцию расчета цены на товар со скидкой discount_price.
# Функция принимает цену price и скидку discount — это дробное число от 0 до 1.
# Здесь, и в дальнейшем, мы под скидкой будем понимать коэффициент, который определяет размер от цены.
# И на этот размер мы понижаем итоговую цена товара. Логику функции необходимо прописать во
# внутренней функции apply_discount, используя объявление переменой price как nonlocal.

def discount_price(price, discount):
    def apply_discount():
        sum = 0
        nonlocal price, discount
        # 20% -> 0.8 20% - 0.2
        sum = price * discount
        return sum
    return apply_discount()


print(discount_price(100, 0.8))
