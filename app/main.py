from app.knights.knight import Knight


def battle(knights_config: dict) -> dict:
    lancelot = Knight(**knights_config["lancelot"])
    arthur = Knight(**knights_config["arthur"])
    mordred = Knight(**knights_config["mordred"])
    red_knight = Knight(**knights_config["red_knight"])

    lancelot.prepare_for_battle()
    arthur.prepare_for_battle()
    mordred.prepare_for_battle()
    red_knight.prepare_for_battle()

    lancelot.hp -= mordred.power - lancelot.protection
    mordred.hp -= lancelot.power - mordred.protection

    if lancelot.hp <= 0:
        lancelot.hp = 0
    if mordred.hp <= 0:
        mordred.hp = 0

    arthur.hp -= red_knight.power - arthur.protection
    red_knight.hp -= arthur.power - red_knight.protection

    if arthur.hp <= 0:
        arthur.hp = 0
    if red_knight.hp <= 0:
        red_knight.hp = 0

    return {
        lancelot.name: lancelot.hp,
        arthur.name: arthur.hp,
        mordred.name: mordred.hp,
        red_knight.name: red_knight.hp,
    }
