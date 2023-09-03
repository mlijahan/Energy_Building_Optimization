import numpy as np

""" Heating Load Calculaion :
Q total = Q conductive + Q ventilation + Q miscellaneous"""

construction_leakage_level = int(input('please insert level of construction'))
design_temperature = int(input('please insert level of construction'))
exposed_surface_area_situation = int(input('please insert level of construction'))
height = int(input('please insert level of construction'))
envelopes_situation = int(input('please insert level of construction'))


class ConductiveHeatingLoad:

    def __int__(self, indoors_temperature, outdoors_temperature, envelop_area, insulating_conductivity,
                insulating_thickness, indoors_surface_coefficient, outdoors_surface_coefficient,
                thermal_resistance_air, total_heating_resistance, heating_insulation_resistance):

        self.IndoorsDesignTemperature = indoors_temperature
        self.OutdoorsTemperature = outdoors_temperature
        self.EnvelopArea = envelop_area
        self.InsulateCoefficient = list(insulating_conductivity)
        self.InsulatingThickness = list(insulating_thickness)
        self.IndoorsSurfaceCoefficient = indoors_surface_coefficient
        self.OutdoorsSurfaceCoefficient = outdoors_surface_coefficient
        self.ThermalResistanceAir = thermal_resistance_air
        self.TotalHeatingResistance = total_heating_resistance
        self.HeatingInsulationResistance = heating_insulation_resistance

    def conductive_load(self):
        q_conductivity = self.u_factor * np.array(self.EnvelopArea) * \
                              (self.IndoorsDesignTemperature - self.OutdoorsTemperature)

        return q_conductivity

    def u_factor(self):
        if self.HeatingInsulationResistance == 0:
            insulate_thickness = np.array(self.InsulatingThickness)
            insulate_coefficient = np.array(self.InsulateCoefficient)
            heating_insulation_resistance = sum(insulate_thickness / insulate_coefficient)
        else:
            heating_insulation_resistance = self.HeatingInsulationResistance

        total_heating_resistance = (1/self.IndoorsSurfaceCoefficient) + heating_insulation_resistance + \
                                        self.ThermalResistanceAir + (1/self.OutdoorsSurfaceCoefficient)

        heat_transfer_coefficient = 1 / total_heating_resistance

        return np.array(heat_transfer_coefficient)


class InfiltrationHeatingLoad:
    def __init__(self, building_exposed_area, air_temperature_difference, room_humidity_difference, area_unit_leakage,
                 infiltration_driving_force, infiltration_air_flow_rate):

        self.BuildingExposedArea = building_exposed_area
        self.AirTemperatureDifference = air_temperature_difference
        self.HumidityDifference = room_humidity_difference
        self.Area_Unit_Leakage = area_unit_leakage
        self.InfiltrationDriving_force = infiltration_driving_force
        self.InfiltrationAirFlowRate = infiltration_air_flow_rate

    def air_temperature_diff(self, indoor_temperature, outdoor_temperature):
        self.AirTemperatureDifference = indoor_temperature - outdoor_temperature
        return self.AirTemperatureDifference

    def area_leakage(self):
        if construction_leakage_level == 1:
            self.Area_Unit_Leakage = 0.7
        elif construction_leakage_level == 2:
            self.Area_Unit_Leakage = 1.4
        elif construction_leakage_level == 3:
            self.Area_Unit_Leakage = 2.8
        elif construction_leakage_level == 4:
            self.Area_Unit_Leakage = 5.6
        else:
            self.Area_Unit_Leakage = 10.4
        return self.Area_Unit_Leakage

    def infiltration_driving_force_value(self):
        if design_temperature == 1:
            if height == 1:
                self.InfiltrationDriving_force = 0.06
            elif height == 2:
                self.InfiltrationDriving_force = 0.061
            elif height == 3:
                self.InfiltrationDriving_force = 0.065
            elif height == 4:
                self.InfiltrationDriving_force = 0.069
            elif height == 5:
                self.InfiltrationDriving_force = 0.072
            elif height == 6:
                self.InfiltrationDriving_force = 0.075
            else:
                self.InfiltrationDriving_force = 0.079
        elif design_temperature == 2:
            if height == 1:
                self.InfiltrationDriving_force = 0.031
            elif height == 2:
                self.InfiltrationDriving_force = 0.032
            elif height == 3:
                self.InfiltrationDriving_force = 0.034
            elif height == 4:
                self.InfiltrationDriving_force = 0.036
            elif height == 5:
                self.InfiltrationDriving_force = 0.039
            elif height == 6:
                self.InfiltrationDriving_force = 0.041
            else:
                self.InfiltrationDriving_force = 0.043
        elif design_temperature == 3:
            if height == 1:
                self.InfiltrationDriving_force = 0.035
            elif height == 2:
                self.InfiltrationDriving_force = 0.038
            elif height == 3:
                self.InfiltrationDriving_force = 0.042
            elif height == 4:
                self.InfiltrationDriving_force = 0.046
            elif height == 5:
                self.InfiltrationDriving_force = 0.050
            elif height == 6:
                self.InfiltrationDriving_force = 0.051
            else:
                self.InfiltrationDriving_force = 0.058
        elif design_temperature == 4:
            if height == 1:
                self.InfiltrationDriving_force = 0.040
            elif height == 2:
                self.InfiltrationDriving_force = 0.043
            elif height == 3:
                self.InfiltrationDriving_force = 0.049
            elif height == 4:
                self.InfiltrationDriving_force = 0.055
            elif height == 5:
                self.InfiltrationDriving_force = 0.061
            elif height == 6:
                self.InfiltrationDriving_force = 0.068
            else:
                self.InfiltrationDriving_force = 0.074
        return self.InfiltrationDriving_force

    def evaluation_exposed_surface_area(self):
        if envelopes_situation == 1:
            self.BuildingExposedArea = int(input('Please Insert Gross surface area'))
        if envelopes_situation == 2:
            self.BuildingExposedArea = int(input('Please Insert Ceiling or wall area  Gross wall area (including '
                                                 'fenestration area Exclude Roof area'))
        if envelopes_situation == 3:
            self.BuildingExposedArea = int(input('Please Insert Common wall area'))
        if envelopes_situation == 4:
            self.BuildingExposedArea = int(input('Please Insert Gross area Exclude Exterior wall area Exclude '
                                                 'Exterior wall rea'))
        if envelopes_situation == 5:
            self.BuildingExposedArea = int(input('Please Insert Floor area Exclude Crawlspace wall area'))
        if envelopes_situation == 6:
            self.BuildingExposedArea = int(input('Please Insert Crawlspace wall area Exclude Floor area'))
        if envelopes_situation == 7:
            self.BuildingExposedArea = int(input('Please Insert Above-grade basement wall area Exclude Floor area'))
        else:
            self.BuildingExposedArea = int(input('Please Insert Gross surface area Exclude Slab area'))
        return self.Area_Unit_Leakage

    def infiltration_rate_flow(self):
        self.InfiltrationAirFlowRate = self.Area_Unit_Leakage * self.BuildingExposedArea *\
                                       self.InfiltrationDriving_force
        return self.InfiltrationAirFlowRate

    def sensible_heating_load(self, specific_heat_of_dry_air=0.24, air_density=1.2):
        sensible_heat = specific_heat_of_dry_air * air_density * self.InfiltrationAirFlowRate *\
                        self.AirTemperatureDifference
        return sensible_heat

    def humidity_diff(self, indoor_humidity, outdoor_humidity):
        self.HumidityDifference = indoor_humidity - outdoor_humidity
        return self.HumidityDifference

    def lateral_heating_load(self, latent_heat_vaporization_water0c=597, air_density=1.2):
        lateral_heat = latent_heat_vaporization_water0c * air_density * self.InfiltrationAirFlowRate * \
                        self.HumidityDifference
        return lateral_heat


class VentilationHeatingLoad:

    def __init__(self, building_surface_area, building_floor_area, air_temperature_difference, room_humidity_difference,
                 required_ventilation_flow_rate, number_bedroom):

        self.BuildingSurfaceArea = building_surface_area  # all above-grade surface area that separates
        # the outdoors from conditioned or semi-conditioned space
        self.BuildingFloorArea = building_floor_area
        self.AirTemperatureDifference = air_temperature_difference
        self.HumidityDifference = room_humidity_difference
        self.RequiredVentilationFlowRate = required_ventilation_flow_rate
        self.NumberBedroom = number_bedroom

    def air_temperature_diff(self, indoor_temperature, outdoor_temperature):
        self.AirTemperatureDifference = indoor_temperature - outdoor_temperature
        return self.AirTemperatureDifference

    def ventilation_flow_rate(self):
        self.RequiredVentilationFlowRate = (0.15 * self.BuildingFloorArea) + 3.5*(self.NumberBedroom+1)

    def sensible_ventilation_heating_load(self, specific_heat_of_dry_air=0.24, air_density=1.2):
        sensible_heat = specific_heat_of_dry_air * air_density * self.RequiredVentilationFlowRate * \
                        self.AirTemperatureDifference
        return sensible_heat

    def humidity_diff(self, indoor_humidity, outdoor_humidity):
        self.HumidityDifference = indoor_humidity - outdoor_humidity
        return self.HumidityDifference

    def lateral_ventilation_heating_load(self, latent_heat_vaporization_water0c=597, air_density=1.2):
        lateral_heat = latent_heat_vaporization_water0c * air_density * self.RequiredVentilationFlowRate * \
                       self.HumidityDifference
        return lateral_heat


class MiscellaneousHeatingLoad:
    def __init__(self, building_surface_area, depth_foundation_below_grade, path_length_wall_below_grade,
                 wall_depth, shortest_width_house, heat_loss_coefficient):

        self.BuildingSurfaceArea = building_surface_area  # all above-grade surface area that separates
        # the outdoors from conditioned or semi-conditioned space
        self.DepthFoundationBelowGrade = depth_foundation_below_grade
        self.PathLengthWallBelowGrade = path_length_wall_below_grade
        self.WallDepth = wall_depth
        self.ShortestWidthHouse = shortest_width_house
        self.HeatLossCoefficient = heat_loss_coefficient

    def heat_loss_below_grade(self):
        pass

    def heat_loss_through_basement(self):
        pass


