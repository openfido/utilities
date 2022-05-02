"""PIPELINE_NAME pipeline for OpenFIDO

TODO: copy the contents of the README.md file here.

"""

version = 1 # specify API version for this pipeline

NAME = "PIPELINE_NAME" # TODO: set this to your pipeline name
OPENFIDO_INPUT = os.getenv("OPENFIDO_INPUT")
OPENFIDO_OUTPUT = os.getenv("OPENFIDO_OUTPUT")

CONFIG = {
    # TODO list your configuration parameter names and values here
}

OPTIONS = {
    "DEBUG" : False,
    # TODO list your option names and values here   
}

try:

    if not OPENFIDO_INPUT:
        raise RuntimeError("OPENFIDO_INPUT not defined in the environment")
    if not OPENFIDO_INPUT.endswith("/"):
        OPENFIDO_INPUT += "/"

    if not OPENFIDO_OUTPUT:
        raise RuntimeError("OPENFIDO_OUTPUT not defined in the environment")
    if not OPENFIDO_OUTPUT.endswith("/"):
        OPENFIDO_OUTPUT += "/"

    # read the config.csv file
    with open(f"{OPENFIDO_INPUT}config.csv","r") as cfg:
        reader = csv.reader(cfg)
        def cast(x,astype):
            if astype is bool:
                try:
                    return int(x)
                except:
                    if x.lower() in ("yes","true","no","false"):
                        return x.lower() in ("yes","true")
                    raise
            else:
                return astype(x)
        for row in reader:
            row0 = row[0].lower()
            if row0 == "data":
                DATA = pd.read_csv(f"{OPENFIDO_INPUT}/{row[1]}")
            elif row0 in CONFIG.keys():
                print("CONFIG",CONFIG)
                if len(row) == 1:
                    CONFIG[row0] = True
                else:
                    CONFIG[row0] = cast(row[1],type(CONFIG[row0]))
            elif row0 in OPTIONS.keys():
                if len(row) == 1:
                    OPTIONS[row0] = True
                else:   
                    OPTIONS[row0] = cast(row[1],type(CONFIG[row0]))
            else:
                print(f"WARNING [address]: config.csv parameter {row[0]} is not valid",file=sys.stderr)        

    # TODO: process the input files and generate the output files

    exit(0) # success

except Exception as err:

    if DEBUG:
        raise
    print(f"ERROR [{NAME}]: {err}",file=sys.stderr)
    exit(1)
