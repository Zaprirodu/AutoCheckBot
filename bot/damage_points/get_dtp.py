from cairosvg import svg2png

import damage_points_m, damage_points_l, damage_points_b
import damage_points_o, damage_points_f, damage_points_d

import fuction_all


# svg to png ахуеть
def svgtopng (points):

    type_name = fuction_all.find_point(points)  # Получает тип поинтов
    image = 'imageVIN\{0}.png'.format(fuction_all.dm_points(points).replace(" ", ""))  # Название картинки


    if type_name == 'damage_points_O':
        file = damage_points_o.get_svg(points)
        svg2png(bytestring=file, write_to=image)
    elif type_name == 'damage_points_L':
        file = damage_points_l.get_svg(points)
        svg2png(bytestring=file, write_to=image)
    elif type_name == 'damage_points_B':
        file = damage_points_b.get_svg(points)
        svg2png(bytestring=file, write_to=image)
    elif type_name == 'damage_points_M':
        file = damage_points_m.get_svg(points)
        svg2png(bytestring=file, write_to=image)
    elif type_name == 'damage_points_F':
        file = damage_points_f.get_svg(points)
        svg2png(bytestring=file, write_to=image)
    elif type_name == 'damage_points_D':
        file = damage_points_d.get_svg(points)
        svg2png(bytestring=file, write_to=image)

    return image




