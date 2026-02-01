import numpy as np
import matplotlib.pyplot as plt


def beregn_og_plott_rotter(n, x, y):
    """
    Løser likningen z^n = a, der a = x + iy.

    Parametere:
    n (int): Graden av roten (naturlig tall).
    x (float): Realdelen av a.
    y (float): Imaginærdelen av a.

    Returnerer:
    None (printer svar og viser plott).
    """

    # 1. Konverter a til polarform MANUELT (uten abs/angle)
    # Regner ut modulus (lengden r) ved hjelp av Pytagoras
    # Regner ut argumentet (vinkelen phi) ved hjelp av arctan2
    # arctan2 håndterer kvadranter korrekt, i motsetning til vanlig arctan
    modulus_a = np.sqrt(x ** 2 + y ** 2)
    argument_a = np.arctan2(y, x)

    # Liste for å lagre løsningene
    losninger = []

    print(f"Løser likningen z^{n} = {x} + {y}i")
    print("-" * 40)

    # 2. Finn alle n røttene ved hjelp av De Moivres formel
    # Den nye radiusen er n-te roten av den opprinnelige modulusen
    ny_radius = modulus_a ** (1 / n)

    for k in range(n):
        # Den nye vinkelen for løsning nummer k
        # Vi legger til k * 2*pi for å rotere rundt sirkelen
        ny_vinkel = (argument_a + 2 * np.pi * k) / n

        # Konverter tilbake til kartesisk form (x + iy)
        real_del = ny_radius * np.cos(ny_vinkel)
        imag_del = ny_radius * np.sin(ny_vinkel)

        # Setter sammen til et kompleks tall
        z = real_del + 1j * imag_del
        losninger.append(z)

        # Printer løsningen pent formatert
        print(f"Løsning z_{k}: {z:.4f}")

    # 3. Plotting av løsningene
    # Henter ut real- og imaginærdeler for plotting
    realdeler = [np.real(z) for z in losninger]
    imagdeler = [np.imag(z) for z in losninger]

    plt.figure(figsize=(6, 6))

    # Tegner en sirkel for å vise at alle løsningene ligger på samme radius
    sirkel = plt.Circle((0, 0), ny_radius, color='gray', fill=False, linestyle='--', alpha=0.5,
                        label=f'|z| = {ny_radius:.2f}')
    plt.gca().add_patch(sirkel)

    # Plotter selve punktene (løsningene)
    plt.scatter(realdeler, imagdeler, color='red', zorder=5, label='Løsninger')

    # Pynter på plottet
    plt.axhline(0, color='black', linewidth=1)  # x-akse
    plt.axvline(0, color='black', linewidth=1)  # y-akse
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.title(f"Løsninger av $z^{n} = {x} + {y}i$")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.legend()

    # Sørger for at aksene har samme skala (så sirkelen ser rund ut)
    plt.axis('equal')
    plt.show()


# --- HOVEDPROGRAM / EKSEMPLER ---

# Eksempel 1: z^3 = 8 (Real: 8, Imag: 0)
# Her forventer vi løsninger spredt 120 grader, der en av dem er tallet 2.
print("EKSEMPEL 1:")
beregn_og_plott_rotter(n=3, x=8, y=0)

print("\n" + "=" * 50 + "\n")

# Eksempel 2: z^4 = -1 + i
# Her er a et komplekst tall i 2. kvadrant.
print("EKSEMPEL 2:")
beregn_og_plott_rotter(n=4, x=-1, y=1)
