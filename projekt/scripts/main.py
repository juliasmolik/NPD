import argparse, sys, os, cProfile, pstats
import prepare_data, calculations, visualize
import cProfile, subprocess, pydot, io

def main():	

    parser = argparse.ArgumentParser(description='NPD Final Project by Julia Smolik')
    parser.add_argument('-g', action='store', dest='gdp_file', help='GDP data file', required=True)
    parser.add_argument('-p', action='store', dest='population_file', help='Population data file', required=True)
    parser.add_argument('-e', action='store', dest='emissions_file', help='CO2 emissions data file', required=True)
    parser.add_argument('-s', action='store', type = int, dest='start_year', help='Date range for analysis - start year')
    parser.add_argument('-k', action='store', type = int, dest='end_year', help='Date range for analysis - end year')
    parser.add_argument('-name', action='store', dest='output_name', help='Output file name')
    parser.add_argument('-v', action='store_true', dest='visualize', help='Data visualization with plots')

    args = parser.parse_args()

    if args.gdp_file == None: 
        print("Error, no GDP data file provided (see help; -h).")
        sys.exit(-1)
    if not os.path.isfile(args.gdp_file):
        print("The specified GDP file does not exist")
        sys.exit(-1) 

    if args.population_file == None:
        print("Error, no population data file provided (see help; -h).")
        sys.exit(-1)
    if not os.path.isfile(args.population_file):
        print("The specified population file does not exist")
        sys.exit(-1) 

    if args.emissions_file == None:
        print("Error, no CO2 emissions data file provided (see help; -h).")
        sys.exit(-1) 
    if not os.path.isfile(args.emissions_file):
        print("The specified CO2 emissions file does not exist")   
        sys.exit(-1)       
    
    if args.start_year != None and args.end_year != None:
        if args.start_year > args.end_year:
            print("The selected start year is greater than the end year.")
            sys.exit(-1)
    
    if args.output_name == None:
        output_name = "filtered_data"
    else:
        output_name = args.output_name
    
    if args.start_year == None:
        start_year = None
    else:
        start_year = args.start_year
    
    if args.end_year == None:
        end_year = None
    else:
        end_year = args.end_year
    
    gdp_data = args.gdp_file
    population_data = args.population_file
    co2_data = args.emissions_file

    path = '../results/'
    if not os.path.exists(path):
        os.makedirs(path)
    
    print("PREPARING THE DATA...")
    output_data_file = prepare_data.custom_filtering(gdp_data, population_data, co2_data, start_year, end_year, output_name)
    print("CONDUCTING CALCULATIONS...")
    co2_per_capita = calculations.co2_per_capita(path+"{}.csv".format(output_name))
    gdp_per_capita = calculations.gdp_per_capita(path+"{}.csv".format(output_name))
    change_of_co2_emission = calculations.change_of_co2_emission(path+"{}.csv".format(output_name))
    
    if args.visualize == True:
        print("VISUALIZING THE DATA...")
        visualize.visualize_co2_change(path+"tables/change_of_co2_emission.csv")
        visualize.visualize_co2_per_capita(path+"tables/co2_per_capita.csv")
        visualize.visualize_gdp_per_capita(path+"tables/gdp_per_capita.csv")
    
    print("ALL DONE.")
    


if(__name__ == "__main__"):

    path = '../results/profiler/'
    if not os.path.exists(path):
        os.makedirs(path)
        
    cProfile.run('main()', filename = path+"profiler.pstats")
    if os.path.isfile(path+"profiler.pstats"):
        subprocess.run("gprof2dot -f pstats {}profiler.pstats > {}graph.dot".format(path, path), shell=True)
        (graph,) = pydot.graph_from_dot_file("{}graph.dot".format(path))
        graph.write_png('{}graph.png'.format(path))
        s = io.StringIO()
        ps = pstats.Stats(path+"profiler.pstats", stream=s)
        ps.print_stats()

        with open(path+"profiler.txt", 'w') as f:
            f.write(s.getvalue())