class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        array=[]
        kelvin=celsius + 273.15
        fehrenheit=celsius*1.80+32.00
        array.append(kelvin,)
        array.append(fehrenheit)
        return array
        