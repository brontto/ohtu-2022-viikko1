"""unitestit tarvis toimia"""
import unittest

from varasto import Varasto

class TestVarasto(unittest.TestCase):
    """testiluokka varastolle"""
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """kontruktori testi"""
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """testataan tässäki jotain"""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """lisätään saldoa"""
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """lisäys pienentää vapaata tilaa"""
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """otetaanki taas välillä"""
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """otetaan ja katotaan tilaa"""
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_virheellinen_tilavuus(self):
        """virhe tilavuudessa"""
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_virheellinen_alku_saldo(self):
        """virhe alkusaldossa"""
        self.varasto = Varasto(10, -1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_virhellinen_saldo_suhteessa_tilavuuteen(self):
        """tilavuuskin huomoidaan"""
        self.varasto = Varasto(10, 15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_virheellinen_lisays(self):
        """lisätään väärä määrä"""
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_virheellinen_lisays_liikaa(self):
        """lisää varastoon liikaa"""
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_virheellinen_otto_maara_miinuksella(self):
        """otetaan väärin"""
        self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_otetaan_yli(self):
        """otetaan liikaa"""
        self.varasto.lisaa_varastoon(5)
        self.assertAlmostEqual(self.varasto.ota_varastosta(10), 5)

    def test_str(self):
        """tulostus"""
        self.assertEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")
