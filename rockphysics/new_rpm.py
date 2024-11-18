import numpy as np
from rockphysics.RockPropertyModels import RockProperties, store_1d_trend_dict_to_hdf

class F3RockPropertyModel:
    def __init__(self, cfg, *args, **kwargs):
        self.cfg = cfg

    def create_1d_trends(self, z=None, store_in_hdf=True):
        if z is None:
            z = np.arange(self.cfg.cube_shape[-1] * self.cfg.digi)

        d = dict(
            z=z,
            shale_vp=self.calc_shale_vp(z),
            shale_vs=self.calc_shale_vs(z),
            shale_rho=self.calc_shale_rho(z),
            brine_sand_vp=self.calc_brine_sand_vp(z),
            brine_sand_vs=self.calc_brine_sand_vs(z),
            brine_sand_rho=self.calc_brine_sand_rho(z),
            oil_sand_vp=self.calc_oil_sand_vp(z),
            oil_sand_vs=self.calc_oil_sand_vs(z),
            oil_sand_rho=self.calc_oil_sand_rho(z),
            gas_sand_vp=self.calc_gas_sand_vp(z),
            gas_sand_vs=self.calc_gas_sand_vs(z),
            gas_sand_rho=self.calc_gas_sand_rho(z),
        )
        if store_in_hdf:
            store_1d_trend_dict_to_hdf(self.cfg, d, z)

        return d

    @staticmethod
    def calc_shale_rho(z):
        # Adjusted to match F3 block shale density trend
        return 2.2 + 0.00035 * z

    @staticmethod
    def calc_shale_vp(z):
        # Adjusted to match F3 block shale Vp trend
        return 1500 + 0.65 * z

    @staticmethod
    def calc_shale_vs(z):
        # Adjusted to match F3 block shale Vs trend
        return 800 + 0.45 * z

    @staticmethod
    def calc_brine_sand_rho(z):
        # Adjusted to match F3 block brine sand density trend
        return 2.3 + 0.0004 * z

    @staticmethod
    def calc_brine_sand_vp(z):
        # Adjusted to match F3 block brine sand Vp trend
        return 1800 + 0.75 * z

    @staticmethod
    def calc_brine_sand_vs(z):
        # Adjusted to match F3 block brine sand Vs trend
        return 950 + 0.5 * z

    @staticmethod
    def calc_oil_sand_rho(z):
        # Adjusted to match F3 block oil sand density trend
        return 2.15 + 0.00035 * z

    @staticmethod
    def calc_oil_sand_vp(z):
        # Adjusted to match F3 block oil sand Vp trend
        return 1700 + 0.7 * z

    @staticmethod
    def calc_oil_sand_vs(z):
        # Adjusted to match F3 block oil sand Vs trend
        return 920 + 0.48 * z

    @staticmethod
    def calc_gas_sand_rho(z):
        # Adjusted to match F3 block gas sand density trend
        return 2.0 + 0.0003 * z

    @staticmethod
    def calc_gas_sand_vp(z):
        # Adjusted to match F3 block gas sand Vp trend
        return 1600 + 0.65 * z

    @staticmethod
    def calc_gas_sand_vs(z):
        # Adjusted to match F3 block gas sand Vs trend
        return 900 + 0.45 * z

    def calc_shale_properties(self, z_rho, z_vp, z_vs):
        rho = self.calc_shale_rho(z_rho)
        vp = self.calc_shale_vp(z_vp)
        vs = self.calc_shale_vs(z_vs)
        shales = RockProperties(rho, vp, vs)
        return shales

    def calc_brine_sand_properties(self, z_rho, z_vp, z_vs):
        rho = self.calc_brine_sand_rho(z_rho)
        vp = self.calc_brine_sand_vp(z_vp)
        vs = self.calc_brine_sand_vs(z_vs)
        brine_sand = RockProperties(rho, vp, vs)
        return brine_sand

    def calc_oil_sand_properties(self, z_rho, z_vp, z_vs):
        rho = self.calc_oil_sand_rho(z_rho)
        vp = self.calc_oil_sand_vp(z_vp)
        vs = self.calc_oil_sand_vs(z_vs)
        oil_sand = RockProperties(rho, vp, vs)
        return oil_sand

    def calc_gas_sand_properties(self, z_rho, z_vp, z_vs):
        rho = self.calc_gas_sand_rho(z_rho)
        vp = self.calc_gas_sand_vp(z_vp)
        vs = self.calc_gas_sand_vs(z_vs)
        gas_sand = RockProperties(rho, vp, vs)
        return gas_sand
