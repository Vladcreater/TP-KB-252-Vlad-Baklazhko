def calc_disc(num_a, num_b, num_c):
return (num_b ** 2) - (4 * num_a * num_c)
coeff_a = float(input("Введіть a: "))
coeff_b = float(input("Введіть b: "))
coeff_c = float(input("Введіть c: "))
discriminant_value = calc_disc(coeff_a, coeff_b, coeff_c)
print("Дискримінант =", discriminant_value)
