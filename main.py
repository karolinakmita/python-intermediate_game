from src.dragon_class import Dragon

dragon1 = Dragon('Wawelski')
print(dragon1.name)

dragon1.change_position(10, 20)
print(f"x= {dragon1.x}, y= {dragon1.y}")

dragon1.move(10, 0, 0, 20)
print(f"x= {dragon1.x}, y= {dragon1.y}")

dragon1.move(10, 15, 0, 0)
print(f"x= {dragon1.x}, y= {dragon1.y}")

dragon1.move(0, 15, 5, 0)
print(f"x= {dragon1.x}, y= {dragon1.y}")

dragon1.move(0, 0, 0, 5)
print(f"x= {dragon1.x}, y= {dragon1.y}")

print(dragon1.lifepoints)

print(f"Smok zaatakował {dragon1.attack()} tyle punktów życia")

dragon1.dragon_demage(10)
dragon1.dragon_demage(20)
dragon1.dragon_demage(30)
dragon1.dragon_demage(40)
dragon1.dragon_demage(50)


