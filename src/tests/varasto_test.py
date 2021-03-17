import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_virheellinen_alkutilavuus_nollataan(self):
        v = Varasto(-10)
        self.assertAlmostEqual(v.tilavuus, 0)

    def test_virheellinen_alkusaldo_nollataan(self):
        v = Varasto(10, -10)
        self.assertAlmostEqual(v.saldo, 0)

    def test_ylimaarainen_alkusaldo_hukkuu(self):
        v = Varasto(10, 20)
        self.assertAlmostEqual(v.saldo, 10)

    def test_negatiivinen_lisays_ei_huomioida(self):
        saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, saldo)

    def test_liika_lisays_tayttaa_maksimiin(self):
        self.varasto.lisaa_varastoon(5000)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_negatiivinen_otto_palauttaa_nolla(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1), 0)

    def test_yli_saldon_ottaminen_palauttaa_kaiken(self):
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(self.varasto.ota_varastosta(5000), 5)

    def test_yli_saldon_ottaminen_nollaa_saldon(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(5000)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_tostring(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")