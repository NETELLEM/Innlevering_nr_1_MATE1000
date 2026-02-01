# Importerer nødvendige biblioteker: NumPy for matematikk og Matplotlib for plotting
import numpy as np
import matplotlib.pyplot as plt


# Funksjon som løser likningen z^n = a og plotter røttene i det komplekse planet
def beregn_og_plott_rotter(n, x, y):
    # 1. Konverterer tallet a = x + iy til polarform (radius og vinkel)
    r_a = np.sqrt(x ** 2 + y ** 2)
    theta_a = np.arctan2(y, x)

    # 2. Beregner den nye radiusen (n-te roten av lengden r_a)
    ny_radius = r_a ** (1 / n)

    # Lister for å lagre koordinatene til de n løsningene
    realdeler = []
    imagdeler = []

    print(f"\nLøser likningen z^{n} = {x} + {y}i")

    # 3. Løkke for å finne alle n røttene ved bruk av De Moivres formel
    for k in range(n):
        # Beregner vinkelen for løsning nummer k (deler sirkelen i n like deler)
        ny_vinkel = (theta_a + 2 * np.pi * k) / n

        # Konverterer tilbake til kartesisk form (x og y) for å finne punktet
        z_real = ny_radius * np.cos(ny_vinkel)
        z_imag = ny_radius * np.sin(ny_vinkel)

        # Lagrer og skriver ut resultatet
        realdeler.append(z_real)
        imagdeler.append(z_imag)

        z = z_real + 1j * z_imag
        print(f"Løsning z_{k}: {z:.4f}")

    # 4. Plotting av resultatene
    plt.figure(figsize=(6, 6))

    # Tegner en hjelpesirkel for å vise at alle røttene ligger på samme radius
    sirkel = plt.Circle((0, 0), ny_radius, color='gray', fill=False, linestyle='--', alpha=0.5)
    plt.gca().add_patch(sirkel)

    # Plotter selve punktene
    plt.scatter(realdeler, imagdeler, color='red', zorder=5, label='Røtter')

    # Pynter på plottet med akser, rutenett og tittel
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.grid(True, linestyle=':', alpha=0.6)

    plt.title(f"Løsninger av z^{n} = {x} + {y}i")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.axis('equal')  # Sikrer at sirkelen ser rund ut (samme skalering på aksene)
    plt.show()


# Hovedprogram som kjører loopen der brukeren kan skrive inn tall
if __name__ == "__main__":
    while True:
        try:
            n_input = input("\nSkriv inn n (heltall): ")
            n = int(n_input)

            x_input = input("Skriv inn x (realdel): ")
            x = float(x_input)

            y_input = input("Skriv inn y (imaginærdel): ")
            y = float(y_input)

            beregn_og_plott_rotter(n, x, y)

            svar = input("\nVil du løse en likning til? (j/n): ")
            if svar.lower() != 'j':
                break

        except ValueError:
            print("Feil input. Pass på at n er heltall og x/y er tall.")
