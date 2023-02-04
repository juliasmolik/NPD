import pytest, sys
sys.path.insert(1, './')
import prepare_data, calculations


def test_filter_data(gdp_data = "../../data/gdp.csv", population_data = "../../data/population.csv", co2_data = "../../data/co2.csv"):
    
    df_gdp, df_population, df_co2 = prepare_data.filter_data(gdp_data, population_data, co2_data)
    
    gdp_output = [int(x) for x in sorted(list(set(df_gdp.columns[2:])))]
    population_output = [int(x) for x in sorted(list(set(df_population.columns[2:])))]
    co2_output = [int(x) for x in sorted(list(set(df_co2["Year"])))]
    
    result = sorted([1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014])
    
    assert gdp_output == population_output == co2_output == result

def test_create_data(gdp_data = "../../data/gdp.csv", population_data = "../../data/population.csv", co2_data = "../../data/co2.csv"):

    data = prepare_data.create_data(gdp_data, population_data, co2_data)
    
    data_output = sorted(list(set(data["Country Name"])))
    
    result = sorted(['Curacao', 'Dominica', 'Ireland', 'Syrian Arab Republic', 'Slovakia', 'Zimbabwe', 'Guinea', 'Ecuador', 'Saudi Arabia', 
              'Spain', 'Iraq', 'Mali', 'Bangladesh', 'United States Of America', 'Switzerland', 'Turks and Caicos Islands', 'Finland', 
              'Latvia', 'Somalia', 'Turkey', 'Turkmenistan', 'Cambodia', 'Australia', 'Croatia', 'Suriname', 'Congo', 'Ghana', 'Pakistan', 
              'Papua New Guinea', 'Colombia', 'Equatorial Guinea', 'El Salvador', 'Central African Republic', 'Thailand', 'Fiji', 
              'Tanganyika', 'Macau Special Adminstrative Region Of China', 'Islamic Republic Of Iran', 'Jamaica', 'Palau', 'Greece', 
              'Estonia', 'Armenia', 'Denmark', 'Chad', 'Hong Kong Special Adminstrative Region Of China', 'Bahrain', 'Nicaragua', 
              'Liberia', 'Netherlands', 'Serbia', 'Mauritius', 'Liechtenstein', 'Togo', 'Afghanistan', 'Brunei (Darussalam)', 'Cuba', 
              'Republic Of Korea', 'Maldives', 'Singapore', 'Uruguay', 'Plurinational State Of Bolivia', 'Belarus', 'Philippines', 
              'Poland', 'Nauru', 'Guinea Bissau', 'Italy (Including San Marino)', 'Bulgaria', 'Lebanon', 'Sri Lanka', 'Israel', 
              'Republic Of Moldova', 'Kazakhstan', 'Nigeria', 'Tuvalu', 'Eritrea', 'Greenland', 'Barbados', 'Tonga', 'Bermuda', 
              'Bhutan', 'Saint Lucia', 'Belize', 'Benin', 'Canada', 'Tajikistan', 'Tunisia', 'Kuwait', 'Sao Tome and Principe', 
              'Uzbekistan', 'Mongolia', 'Namibia', 'Viet Nam', 'Belgium', 'Qatar', 'Uganda', 'Niger', 'Slovenia', 'Bosnia and Herzegovina', 
              'Montenegro', 'China (Mainland)', 'Gabon', 'Faeroe Islands', 'Albania', 'Romania', 'Haiti', 'Macedonia', 'Germany', 
              'Trinidad and Tobago', 'Mexico', 'Mauritania', 'Portugal', 'Bahamas', 'Iceland', 'Vanuatu', 'Malaysia', 'Jordan', 
              'Djibouti', 'Gambia', 'India', 'Republic Of South Sudan', 'Guyana', 'Grenada', 'Senegal', 'Yemen', 'Azerbaijan', 
              'Ethiopia', 'Republic Of Cameroon', 'Samoa', 'Luxembourg', 'Burundi', 'South Africa', 'Democratic Republic Of The Congo (Formerly Zaire)', 
              'Lithuania', 'Norway', 'Morocco', 'Indonesia', 'New Caledonia', 'Peru', 'Russian Federation', 'Cyprus', 'Dominican Republic', 
              'Kiribati', 'Rwanda', 'Angola', 'Ukraine', 'Honduras', 'Cayman Islands', 'Seychelles', 'Solomon Islands', 'Aruba', 
              'Cote D Ivoire', 'Sweden', 'Brazil', 'Sudan', 'France (Including Monaco)', 'St. Kitts-Nevis', 'Egypt', 'Malawi', 
              'Gibraltar', 'Marshall Islands', 'Chile', 'Andorra', 'Malta', 'Guatemala', 'United Kingdom', 'Costa Rica', 'Czech Republic', 
              'Oman', 'New Zealand', 'Zambia', 'Democratic People S Republic Of Korea', 'Paraguay', 'Cape Verde', 'Hungary', 'Kenya', 
              'Antigua and Barbuda', 'Japan', 'Botswana', 'French Polynesia', 'Venezuela', 'Mozambique', 'Sierra Leone', 'Burkina Faso', 
              'St. Vincent and The Grenadines', 'British Virgin Islands', 'Comoros', 'Saint Martin (Dutch Portion)', 'Panama', 
              'United Arab Emirates', 'Madagascar', 'Lesotho', 'Nepal', 'Algeria', 'Georgia', 'Austria', 'Argentina'])
    
    assert data_output == result
    

def test_custom_filtering(gdp_data = "../../data/gdp.csv", population_data = "../../data/population.csv", co2_data = "../../data/co2.csv", start_year = 1994, end_year = 2014, file_name = "filtered_data"):
    
    filtered = prepare_data.custom_filtering(gdp_data, population_data, co2_data, start_year, end_year, file_name)
    
    data_output = sorted(list(set(filtered["Year"])))
    
    assert data_output[0] == start_year and data_output[-1] == end_year

def test_co2_per_capita(csv_file = "../../results/filtered_data.csv"):
    
    co2_per_capita = calculations.co2_per_capita(csv_file)
    
    co2_per_capita_output = sorted(list(set(co2_per_capita["CO2 per capita"])))
    
    result = sorted([0.007204997113878123, 0.007849283836364416, 0.007000589523328281, 0.011688109438735782, 0.005736262303630793,
              0.016019841687123573, 0.0070668118733601265, 0.009268533091683757, 0.007168732193479487, 0.009309380929281708,
              0.005651814565120118, 0.015013514792650477, 0.015545602735580063, 0.007559587088608297, 0.010651667888612418, 
              0.00787367223237649, 0.005665212397693284, 0.009208421171152323, 0.008024700404243126, 0.0073381975654578865,
              0.005771728030747707, 0.007361823243660796, 0.008333303472354107, 0.006396357085279023, 0.017405971863336204, 
              0.018355709554106987, 0.009375729477848989, 0.006110976268585432, 0.009923054174500413, 0.016254999566112607, 
              0.01660772876145329, 0.006795921356473071, 0.005554952018830345, 0.007072729621495931, 0.006682998530132288,
              0.010774305920538818, 0.007349003272835466, 0.016057128990882935, 0.005614115490375802, 0.00984230625594815,
              0.008494320428010438, 0.009210195610694118, 0.00816910013890913, 0.008757163397080088, 0.010756930198306244,
              0.00869211990880313, 0.011406428253765687, 0.011959977260916346, 0.007067120754032149, 0.006897065210647143, 
              0.007430541354643047, 0.006727979147199134, 0.008407002946784538, 0.00723081908774204, 0.009262759508109961, 
              0.008934768055325238, 0.007605245262708351, 0.009477626198937675, 0.00793878912875025, 0.005636580065217961, 
              0.007283036303038187, 0.006431808804188049, 0.007706208382733855, 0.008373699027650526, 0.006606565964155119, 
              0.007067381618893664, 0.012308324110616912, 0.007719860495805448, 0.006715995194151699, 0.008193605018478243,
              0.0071525818354018274, 0.006493259920258211, 0.007835725022363887, 0.007649599012954966, 0.01598570046939323, 
              0.0071423854907226025, 0.009244451378866482, 0.010288052646094838, 0.005538765742790055, 0.008178302973617274,
              0.005570509069631364, 0.006639992480098563, 0.008594412112434344, 0.008475093958235822, 0.007899861155248055, 
              0.007606741351036295, 0.019100724800119553, 0.01416235993371858, 0.007205930892786281, 0.009578799263572272, 
              0.01685641617435138, 0.007590123033188262, 0.008439437782010258, 0.007049154700199597, 0.016883923754545258, 
              0.016925718487460693, 0.007417922981565162, 0.006493392921372836, 0.009794302419188869, 0.007141868728677933,
              0.007548515557668876, 0.007473589971439752, 0.007976484607877359, 0.0065483658706364505, 0.0069033276942571655])

    assert co2_per_capita_output == result

def test_gdp_per_capita(csv_file = "../../results/filtered_data.csv"):
    
    gdp_per_capita = calculations.gdp_per_capita(csv_file)
    
    gdp_per_capita_output = sorted(list(set(gdp_per_capita["GDP per capita"])))
    
    result = sorted([102913.45084367364, 58883.959426596695, 48144.57912842962, 72208.93467433898, 149010.22489866475, 
              48659.598875323405, 86547.6708907265, 35351.36546068186, 101407.7640319337, 38952.034200557195, 
              74287.41337395462, 46641.64087548766, 64051.23221047213, 66111.72522700355, 43084.47246507163, 
              42578.76313556959, 77400.42236988738, 80988.13762308592, 54878.47100097867, 130655.63695973705, 
              74853.9387293539, 120422.13793415697, 79977.69708174931, 75882.03385603392, 91254.0347609688, 
              62583.1002034588, 43128.01410890911, 98431.8651810241, 87693.79006580987, 38542.715099709094, 
              99471.63889786311, 126096.61042540184, 85139.96044695447, 101524.14185198482, 65689.32145369108, 
              41631.438858784415, 98467.683993982, 90788.80048761438, 44197.61910139075, 51371.74080698357, 
              89260.7571041005, 96944.0956064873, 178864.85191378542, 50872.449268462515, 120000.14072985921, 
              85188.33602859033, 114374.24653641916, 70359.31910887982, 39150.03963080886, 119025.0572034666, 
              31476.06372218476, 42740.12818251488, 100600.56240758917, 66810.47852086792, 97019.18275274622, 
              76544.91708684727, 39169.359570150424, 36610.1683163197, 89859.86537287224, 57603.83602182599, 
              50444.3591236176, 53005.7339209178, 36629.030903662235, 44826.78907016581, 123678.70214327482, 
              110885.99137872111, 78631.6991111527, 39727.846671388244, 48440.1420151355, 41786.234141170105, 
              77117.126014204, 49470.39712596742, 47445.38108120509, 51032.34963531796, 48478.88325040911, 
              104287.38749845888, 93022.87514225378, 109419.74695310647, 82801.54346682134, 141192.53467301757, 
              81307.06836748298, 43933.235442736, 143264.0594325862, 74148.32007571861, 158130.45751887048, 
              105399.26049482402, 106935.48634197908, 85433.03027988657, 100289.24300217832, 112584.67627095825, 
              107475.32029797768, 76757.30021898718, 50134.89077349467, 56794.85015889518, 56284.16864780942, 
              34788.359851881905, 54245.45973729298, 173030.2082793633, 50155.9741273218, 97774.16207174277, 
              79345.75247257017, 101875.28407345986, 95221.85887203013, 79863.27908487529, 39933.51505648732])
    
    assert gdp_per_capita_output == result

def test_change_of_co2_emission(csv_file = "../../results/filtered_data.csv"):
    
    change_of_co2_emission = calculations.change_of_co2_emission(csv_file)
    
    change_of_co2_emission_output = sorted(list(set(change_of_co2_emission["Change of CO2 emission"])))
    
    result = sorted([-0.004937417915987492, -0.0035856254746637166, 0.0010212237038983757, -0.0012341400127076716, -0.0019735219607338126, 0.0013484638601190748, 0.0021959476347498345, 0.0010811210595726524, 0.0022697457457973, -0.0013344402172855586])
    
    assert change_of_co2_emission_output == result


def main():
    
    gdp_data = "../../data/gdp.csv"
    population_data = "../../data/population.csv"
    co2_data = "../../data/co2.csv"
    filtered_data = "../../results/filtered_data.csv"
    
    test_filter_data(gdp_data = gdp_data, population_data = population_data, co2_data = co2_data)
    test_create_data(gdp_data = gdp_data, population_data = population_data, co2_data = co2_data)
    test_custom_filtering(gdp_data = gdp_data, population_data = population_data, co2_data = co2_data, start_year = 1994, end_year = 2014, file_name = "filtered_data")
    test_co2_per_capita(csv_file = filtered_data)
    test_gdp_per_capita(csv_file = filtered_data)
    test_change_of_co2_emission(csv_file = filtered_data)

if(__name__ == "__main__"):
    
    pytest.main(["../../tests/test.py"])