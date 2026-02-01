import numpy as np
import matplotlib.pyplot as plt


def beregn_og_plott_rotter(n, x, y):
    """
    Løser likningen z^n = a (hvor a = x + iy) og plotter løsningene.

    Parametere:
    n (int): Graden av roten (må være et naturlig tall).
    x (float): Realdelen av a.
    y (float): Imaginærdelen av a.
    """

    print(f"\nLøser likningen z^{n} = {x} + {y}i")
    print("-" * 40)

    # --- STEG 1: Konvertering til polarform (Manuelt) ---
    # Vi har a på formen x + iy. Vi trenger radius (r) og vinkel (theta).
    # Krav: Ikke bruke abs() eller angle().

    # Regner ut modulus (lengden r) ved hjelp av Pytagoras: sqrt(x^2 + y^2)
    r_a = np.sqrt(x ** 2 + y ** 2)

    # Regner ut argumentet (vinkelen theta) ved hjelp av arctan2.
    # arctan2(y, x) håndterer alle kvadranter korrekt.
    theta_a = np.arctan2(y, x)

    # --- STEG 2: Finne de n røttene (De Moivres formel) ---
    # Den nye radiusen er n-te roten av den opprinnelige radiusen.
    ny_radius = r_a ** (1 / n)

    # Vi lagrer løsningene i lister for å kunne plotte dem senere
    realdeler = []
    imagdeler = []

    for k in range(n):
        # Formel for ny vinkel: (theta + 2*pi*k) / n
        # Vi legger til 2*pi*k for å rotere rundt sirkelen for hver løsning.
        ny_vinkel = (theta_a + 2 * np.pi * k) / n

        # Konverter tilbake til kartesisk form (x + iy) for å finne tallet
        z_real = ny_radius * np.cos(ny_vinkel)
        z_imag = ny_radius * np.sin(ny_vinkel)

        # Lagre verdiene til plotting
        realdeler.append(z_real)
        imagdeler.append(z_imag)

        # Printer løsningen pent til skjermen (z_k)
        # Vi lager et komplekst tall 'z' kun for visningens skyld
        z = z_real + 1j * z_imag
        print(f"Løsning z_{k}: {z:.4f}")

    # --- STEG 3: Plotting av løsningene ---
    plt.figure(figsize=(6, 6))

    # Tegner en hjelpe-sirkel for å vise at alle røttene ligger like langt fra sentrum
    sirkel = plt.Circle((0, 0), ny_radius, color='gray', fill=False, linestyle='--', alpha=0.5,
                        label=f'|z| = {ny_radius:.2f}')
    plt.gca().add_patch(sirkel)

    # Plotter selve punktene (løsningene)
    plt.scatter(realdeler, imagdeler, color='red', zorder=5, label='Løsninger')

    # Pynter på plottet med akser og rutenett
    plt.axhline(0, color='black', linewidth=1)  # x-akse
    plt.axvline(0, color='black', linewidth=1)  # y-akse
    plt.grid(True, linestyle=':', alpha=0.6)

    plt.title(f"Løsninger av $z^{n} = {x} + {y}i$")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.legend()

    # VIKTIG: Sørger for at 1 enhet på x-aksen er like lang som 1 enhet på y-aksen
    plt.axis('equal')

    # Viser plottet på skjermen
    plt.show()


# --- HOVEDPROGRAM (Kjøres når du starter filen) ---
if __name__ == "__main__":

    print("--- OBLIG 1: Røtter av komplekse tall ---")

    while True:
        try:
            # Henter input fra brukeren
            n_input = input("\nSkriv inn n (graden, heltall): ")
            n = int(n_input)

            x_input = input("Skriv inn realdelen til a (x): ")
            x = float(x_input)

            y_input = input("Skriv inn imaginærdelen til a (y): ")
            y = float(y_input)

            # Kjører funksjonen vår med tallene fra brukeren
            beregn_og_plott_rotter(n, x, y)

            # Spør om brukeren vil prøve igjen (for å få 2 eksempler)
            svar = input("\nVil du løse en likning til? (j/n): ")
            if svar.lower() != 'j':
                print("Avslutter programmet.")
                break

        except ValueError:
            print("Feil input! Pass på at n er et heltall og x/y er tall.")
