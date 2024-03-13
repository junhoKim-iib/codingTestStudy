def solution(price, money, count):
    total = (price + (price * count)) / 2  * count

    return (total - money) if total > money else 0